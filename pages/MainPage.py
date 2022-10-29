from selene.support.jquery_style_selectors import s


class MainPage(object):
    def __init__(self):
        self.ava_txt = s("form[name='logout'] b")
        self.ava_btn = s(".avatar")
        self.ava_fullName_mnu = s("span[text=\"header.fullName\"] span[class='dnTextFixedWidthText ng-binding']")
        self.teller_mnu = s("#menu-teller")
        self.search_inp = s("input[type='search']")
        self.create_cust_btn = s("button[data-test-id='action-addNewCustomer']")
    def open_ava_menu(self):
        self.ava_btn.click()
        return self
    def cust_create(self, cust):
        self.login_inp.set(user.login)
        self.passw_inp.set(user.password)
        self.login_btn.click()