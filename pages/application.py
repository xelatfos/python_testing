from selene import config, browser
from selene.support.jquery_style_selectors import s

from domain.user import User
from pages.MainPage import MainPage

class Application(object):
    def __init__(self):
        self.login_inp = s("input[name='user']")
        self.passw_inp = s("input[name='pass']")
        self.login_btn = s("input[type=submit]")

    def open(self):
        browser.open_url("/addressbook/")
        return self

    def login_as(self, user):
        self.login_inp.set(user.login)
        self.passw_inp.set(user.password)
        self.login_btn.click()
        return MainPage()