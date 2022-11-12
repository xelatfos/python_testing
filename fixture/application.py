from selene import config, browser
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s

from model.user import User
from fixture.session import SessionHelper
from pages.MainPage import MainPage

class Application(object):
    """fixture object"""

    def __init__(self):
        self.login_inp = s("input[name='user']")
        self.passw_inp = s("input[name='pass']")
        self.login_btn = s("input[type=submit]")
        self.browser = browser
        self.browser.open_url("/addressbook/")
        self.main_page = MainPage()
        self.session = SessionHelper(self)
        self.tid = 0
    def next_tid(self):
        self.tid += 1
        return str(self.tid).rjust(3,'0')
    def open(self):
        self.browser.open_url("/addressbook/")
        return self

    def login_as(self, user):
        self.login_inp.set(user.login)
        self.passw_inp.set(user.password)
        self.login_btn.click()
        return MainPage()
    def admin_login(self, admin = User("admin", "secret", "(admin)")):
       (self.
        open().
        login_as(admin).ava_txt.
        should(have.exact_text(admin.fullName))
        )
       if not browser.should(have.url("http://localhost/addressbook/")):
            self.browser.take_screenshot()
       return MainPage()
    def destroy(self):
        #pass
        self.browser.close()
    def is_valid(self):
        try:
            self.browser.driver().current_url
            return True
        except:
            return False