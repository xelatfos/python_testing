from selene.support.conditions import have
from selene.support.jquery_style_selectors import s, ss

from domain import user, group


class MainPage(object):
    def __init__(self):
        self.ava_txt = s("form[name='logout'] b")
        self.ava_lout = s("//a[.='Logout']")
        self.menu_groups = s("//a[.='groups']")
        self.btn_add_group = s("[name='new']")

        self.btn_del_group = s("[name='delete']")
        self.btn_edit_group = s("[name='edit']")
        self.grp_name = s("[name='group_name']")
        self.grp_header = s("[name='group_header']")
        self.grp_footer = s("[name='group_footer']")
        self.btn_grp_enter = s("[name='submit']")
        self.chk_grp_first = s("[name='selected[]']")
        self.chk_grp_all = ss("[name='selected[]']")
        self.grp_head = s("div[id='content'] h1")
        self.grp_msg = s(".msgbox")
    def group_create(self, group):
        self.menu_groups.click()
        self.btn_add_group.click()
        self.grp_head.should(have.exact_text("Groups"))
        self.grp_name.set(group.name)
        self.grp_header.set(group.header)
        self.grp_footer.set(group.footer)
        self.btn_grp_enter.click()
        self.grp_msg.should(have.text("A new group has been entered into the address book."))
        return self
    def logout(self):
        self.ava_lout.click()