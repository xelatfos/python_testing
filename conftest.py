import json
import os.path
import pytest
from fixture.application import Application
from fixture.db import DbFixture

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None or not fixture.is_valid():
        fixture = Application()
        fixture.admin_login()
    # elif not fixture.is_valid():
    #     fixture = Application()
    #     fixture.admin_login()

    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    fixture = Application()

    def fin():
        fixture.session.logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption('--target'))['db']
    dbfixture = DbFixture(host=db_config['host'],
                          name=db_config['name'],
                          user=db_config['user'],
                          password=db_config['password']
                          )

    def fin():
        dbfixture.destroy()

    request.addfinalizer(fin)
    return dbfixture


def pytest_collection_modifyitems(items):
    """Modifies test items in place to ensure test modules run in a given order."""
    MODULE_ORDER = ["test_add_group", "test_modify_group", "test_del_group", "test_db_match"]
    module_mapping = {item: item.module.__name__ for item in items}

    sorted_items = items.copy()
    # Iteratively move tests of each module to the end of the test queue
    for module in MODULE_ORDER:
        sorted_items = [it for it in sorted_items if module_mapping[it] != module] + [
            it for it in sorted_items if module_mapping[it] == module
        ]
    items[:] = sorted_items


def pytest_addoption(parser):
    parser.addoption("--target", action="store", default="target.json")
