# -*- coding: utf-8 -*-
import pytest
from selene.api import *
from selene.browser import *
# pytest -sv tests --tb=short
from pages.LoginPage import LoginPage
from domain.user import User
from pages.MainPage import MainPage

# @pytest.mark.skip
def test_admin_login(admin = User("admin", "secret", "(admin)")):
   (LoginPage().
    open().
    login_as(admin).ava_txt.
    should(have.exact_text(admin.fullName))
    )
   if not browser.should(have.url("http://localhost/addressbook/")):
        browser.take_screenshot()
   MainPage().logout()
    #assert u == "https://dev18.nj1.nymbus.com/frontoffice/#/customer/search"