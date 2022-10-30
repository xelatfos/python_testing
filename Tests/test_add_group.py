import pytest
from selene.support.conditions import have

from domain.group import Group
from domain.user import User
from pages.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
def test_add_group(app):
    admin = User("admin", "secret", "(admin)")
    (app.main_page.ava_txt.
     should(have.exact_text(admin.fullName))
     )
    group = Group("name", "header", "footer")
    app.main_page.group_create(group)
    # MainPage().logout()