import allure
import pytest
from selene.support.conditions import have
from domain.user import User

def test_del_group(app):
    with allure.step("Deleting a group"):
        app.main_page.menu_groups.click()
        app.main_page.chk_grp_first.click()
        app.main_page.btn_del_group.click()


def test_del_groups(app):
    with allure.step("Deleting all groups"):
        app.main_page.menu_groups.click()
        # also we can use enumerate() here
        for index, chk in zip(range(3), app.main_page.chk_grp_all):
            chk.click()
        app.main_page.btn_del_group.click()
