import pytest
import allure
from model.group import Group

from model.group import Group
from utils.rand import rnd_str

testdata = [
    Group(name,head,foot)
    for name in ["", rnd_str('name ', 10)]
    for head in ["", rnd_str('head ', 10)]
    for foot in ["", rnd_str('foot ', 10)]
]

@allure.suite("Groups testing")
@allure.sub_suite("Adding a new parametrized groups")
@pytest.mark.parametrize('group', testdata, ids = [repr(x) for x in testdata])
def test_add_groups(app, group):
    gr_num = app.main_page.grp_cnt().chk_grp_cnt
    allure.dynamic.title(f".{gr_num} Adding a new group {repr(group)}")
    app.main_page.group_create(group)
    assert app.main_page.grp_cnt().chk_grp_cnt == gr_num+1
    # MainPage().logout()
