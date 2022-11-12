import allure
import pytest
from selene.support.conditions import have
from model.user import User
from random import randrange

pytestmark = [allure.suite("Groups testing"), allure.sub_suite("Deleting the groups")]
# @allure.suite("Groups testing")
# @allure.sub_suite("Deleting the groups")
@allure.description("""
Deleting a random group
Checking the groups number after deletion
""")
def test_del_group(app):
    gr_num = app.main_page.grp_cnt().chk_grp_cnt
    allure.dynamic.title(f".{app.next_tid()} Deletion a random group step")
    app.main_page.group_del(randrange(gr_num))
    assert app.main_page.grp_cnt().chk_grp_cnt == gr_num - 1

# @allure.suite("Groups testing")
# @allure.sub_suite("Deleting the groups")
def test_del_groups(app):
    gr_num = app.main_page.grp_cnt().chk_grp_cnt
    # also we can use enumerate() here
    allure.dynamic.title(f".{app.next_tid()} Deletion of {gr_num} groups step")
    for index, chk in zip(range(5), app.main_page.chk_grp_all):
        chk.click()
    app.main_page.btn_del_group.click()
    assert app.main_page.grp_cnt().chk_grp_cnt == gr_num - 5
# @allure.suite("Groups testing")
# @allure.sub_suite("Deleting the groups")
def test_del_rest_groups(app):
    gr_num = app.main_page.grp_cnt().chk_grp_cnt
    allure.dynamic.title(f".{app.next_tid()} Deletion of rest {gr_num} group step")
    for index, chk in enumerate(app.main_page.chk_grp_all):
        chk.click()
    app.main_page.btn_del_group.click()
    assert app.main_page.grp_cnt().chk_grp_cnt == 0
