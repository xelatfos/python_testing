from selene.support.conditions import have

from domain.group import Group
from domain.user import User

def test_modify_groups(app):
    admin = User("admin", "secret", "(admin)")
    (app.session.
     admin_login().
     ava_txt.
     should(have.exact_text(admin.fullName))
     )
    app.main_page.menu_groups.click()
    app.main_page.chk_grp_first.click()
    app.main_page.btn_edit_group.click()
    app.main_page.fill_grp(Group(name="name11"))
    app.main_page.btn_grp_update.click()

    app.session.logout()
    # MainPage().logout()
