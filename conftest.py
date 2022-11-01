import pytest
from fixture.application import Application
fixture = None
@pytest.fixture(scope = "session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.admin_login()
    elif not fixture.is_valid():
        fixture = Application()
        fixture.admin_login()

    return fixture
@pytest.fixture(scope = "session", autouse=True)
def stop(request):
    fixture = Application()
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
def pytest_collection_modifyitems(items):
    """Modifies test items in place to ensure test modules run in a given order."""
    MODULE_ORDER = ["test_add_group", "test_modify_group", "test_del_group"]
    module_mapping = {item: item.module.__name__ for item in items}

    sorted_items = items.copy()
    # Iteratively move tests of each module to the end of the test queue
    for module in MODULE_ORDER:
        sorted_items = [it for it in sorted_items if module_mapping[it] != module] + [
            it for it in sorted_items if module_mapping[it] == module
        ]
    items[:] = sorted_items