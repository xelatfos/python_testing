import allure
import pytest
from selene.support.conditions import have
from model.user import User
from random import randrange


@allure.suite("Deleting a random group")
@allure.description("""
Deleting a random group
Checking the groups number after deletion
""")
def test_del_group(app):
    with allure.step("Deleting a group"):
        gr_num = app.main_page.grp_cnt().chk_grp_cnt
        app.main_page.group_del(randrange(gr_num))
        assert app.main_page.grp_cnt().chk_grp_cnt == gr_num -1

@allure.suite("Deleting all the rest groups")
def test_del_groups(app):
    gr_num = app.main_page.grp_cnt().chk_grp_cnt
    with allure.step("Deleting all groups"):
     # also we can use enumerate() here
        for index, chk in zip(range(5), app.main_page.chk_grp_all):
            chk.click()
        app.main_page.btn_del_group.click()
    assert app.main_page.grp_cnt().chk_grp_cnt == gr_num -5
    allure.dynamic.title('After a successful group deletion , the title was replaced with this line.')


def test_del_rest_groups(app):
    with allure.step("Deleting all groups"):
        gr_num = app.main_page.grp_cnt().chk_grp_cnt
        # also we can use enumerate() here
        for chk in app.main_page.chk_grp_all:
            chk.click()
        app.main_page.btn_del_group.click()
        assert app.main_page.grp_cnt().chk_grp_cnt == 0
