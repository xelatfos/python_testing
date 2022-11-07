import allure
import pytest

from domain.group import Group

def test_modify_groups(app):
    with pytest.allure.step("Modifying first group"):
        app.main_page.menu_groups.click()
        app.main_page.chk_grp_first.click()
        app.main_page.btn_edit_group.click()
        app.main_page.fill_grp(Group("name11","",""))
        app.main_page.btn_grp_update.click()

    # MainPage().logout()
