from selene.support.conditions import have

from domain.group import Group
from domain.user import User
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage


def test_add_group():
    admin = User("admin", "secret", "(admin)")
    (LoginPage().
     open().
     login_as(admin).ava_txt.
     should(have.exact_text(admin.fullName))
     )
    group = Group("name", "header", "footer")
    MainPage().group_create(group)
    # MainPage().logout()