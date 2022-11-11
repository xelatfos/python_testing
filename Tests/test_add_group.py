import pytest
import allure
import random
import string
from model.group import Group

from model.group import Group

def rnd_str(pre, max_len):
    sym = string.ascii_letters + string.digits  + " "*10 # + string.punctuation - known issue here
    return pre.join(random.choice(sym) for i in range(random.randrange(max_len)))

testdata = [
    Group(name,head,foot)
    for name in ["", rnd_str('name ', 10)]
    for head in ["", rnd_str('head ', 10)]
    for foot in ["", rnd_str('foot ', 10)]
]
@allure.step(f"Adding new group: {[repr(x) for x in testdata]} step top")
@allure.title("Adding new groups step")
@pytest.mark.parametrize('group', testdata, ids = [repr(x) for x in testdata])
def test_add_groups(app, group):
    with allure.step("Adding new groups"):
        gr_num = app.main_page.grp_cnt().chk_grp_cnt
        app.main_page.group_create(group)
    assert app.main_page.grp_cnt().chk_grp_cnt == gr_num+1
    # MainPage().logout()
