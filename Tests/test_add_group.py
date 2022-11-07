from selene.support.conditions import have

from domain.group import Group
from domain.user import User

def test_add_groups(app):
    app.main_page.group_create(Group("name1", "header2", "footer3"))
    app.main_page.group_create(Group("name", "header", "footer"))
    app.main_page.group_create(Group("", "", ""))
    # MainPage().logout()
