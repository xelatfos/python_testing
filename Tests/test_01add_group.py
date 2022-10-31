from selene.support.conditions import have

from domain.group import Group
from domain.user import User

def test_add_groups(app):
    admin = User("admin", "secret", "(admin)")
    (app.session.
     admin_login().
     ava_txt.
     should(have.exact_text(admin.fullName))
     )

    app.main_page.group_create(Group("name", "header", "footer"))
    app.main_page.group_create(Group("", "", ""))

    app.session.logout()
    # MainPage().logout()
