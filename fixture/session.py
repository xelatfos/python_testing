from selene.support.conditions import have

from domain.user import User
from pages.MainPage import MainPage


class SessionHelper:
    def __init__(self, app):
        self.app = app
    def login_as(self):
        pass
    def logout(self):
        pass
    def admin_login(self, admin = User("admin", "secret", "(admin)")):
       (self.
       app.
        open().
        login_as(admin).ava_txt.
        should(have.exact_text(admin.fullName))
        )
       if not self.app.browser.should(have.url("http://localhost/addressbook/")):
            self.app.browser.take_screenshot()
       return self.app.main_page
    def logout(self):
        self.app.main_page.logout()