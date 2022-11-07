import pytest
import allure

from domain.group import Group


def test_add_groups(app):
    with pytest.allure.step("Adding a new group"):
        app.main_page.group_create(Group("name1", "header2", "footer3"))
        app.main_page.group_create(Group("name", "header", "footer"))
        app.main_page.group_create(Group("", "", ""))
    # MainPage().logout()
