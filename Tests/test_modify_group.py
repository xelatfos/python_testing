from random import randrange

import allure
import allure_pytest
import pytest
from conftest import fixture, app
from model.group import Group

testdata = [(Group("", "", "footer11"),lambda x : x*0),
            (Group("name11", "", ""), lambda x: randrange(x)),
            (Group("name11", "header11", "footer11"),lambda x: x//2),
            (Group("", "", ""), lambda x: randrange(x)),
            (Group("", "header11", ""),lambda x: x-1),
            ]

@allure.sub_suite(f"Modifying random parametrized groups ")
@pytest.mark.parametrize('group', testdata, ids = [repr(x[0]) for x in testdata])
def test_modify_groups_random(app, group):
    with allure.step(f"Modifying {repr(group)} group"):
        gr_num = app.main_page.grp_cnt().chk_grp_cnt
        app.main_page.group_mod(group[0],group[1](gr_num)) # first
        assert app.main_page.grp_cnt().chk_grp_cnt == gr_num

