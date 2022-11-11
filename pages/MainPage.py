from selene.support.conditions import have
from selene.support.jquery_style_selectors import s, ss

from model import user, group
from model.group import Group
global gr_num

class MainPage(object):
    gr_num = None
    def __init__(self):
        self.ava_txt = s("form[name='logout'] b")
        self.ava_lout = s("//a[.='Logout']")
        self.menu_groups = s("//a[.='groups']")
        self.btn_add_group = s("[name='new']")

        self.btn_del_group = s("[name='delete']")
        self.btn_edit_group = s("[name='edit']")
        self.btn_group_page = s("// a[.='group page']")

        self.grp_name = s("[name='group_name']")
        self.grp_header = s("[name='group_header']")
        self.grp_footer = s("[name='group_footer']")
        self.btn_grp_enter = s("[name='submit']")
        self.chk_grp_first = s("[name='selected[]']")
        self.chk_grp_all = ss("[name='selected[]']")
        self.chk_grp_cnt = len(self.chk_grp_all)
        self.grp_head = s("div[id='content'] h1")
        self.btn_grp_update = s("[name='update']")
        self.grp_msg = s(".msgbox")
    def fill_grp(self, group):
        self.grp_name.set(group.name)
        self.grp_header.set(group.header)
        self.grp_footer.set(group.footer)
    def grp_cnt(self):
        self.menu_groups.click()
        self.chk_grp_all = ss("[name='selected[]']")
        self.chk_grp_cnt = len(self.chk_grp_all)
        global gr_num
        gr_num = self.chk_grp_cnt
        return self

    def group_del(self, index=0):
        self.menu_groups.click()
        self.chk_grp_all[index].click()
        self.btn_del_group.click()
        self.grp_cnt()
        return self
    def group_create(self, group):
        self.menu_groups.click()
        self.btn_add_group.click()
        self.grp_head.should(have.exact_text("Groups"))
        self.fill_grp(group)
        self.btn_grp_enter.click()
        self.grp_msg.should(have.text("A new group has been entered into the address book."))
        self.grp_cnt()
        return self

    def group_mod(self, group, index=0):
        self.menu_groups.click()
        self.chk_grp_all[index].click()
        self.btn_edit_group.click()
        self.fill_grp(group)
        self.btn_grp_update.click()
    def logout(self):
        self.ava_lout.click()