from testdata import constants as dataval

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.clk_sigin_btn = "//a[contains(text(),'SIGN-ON')]"
        self.sun_txt_bx_name = "//input[@name='userName']"
        self.spwd_txt_bx_name = "//input[@name='password']"
        self.clk_login_btn = "//input[@value='Login']"


    def click_on_signin_button(self):
        self.driver.find_element_by_xpath(self.clk_sigin_btn).click()

    def enter_username(self):
        self.driver.find_element_by_xpath(self.sun_txt_bx_name).send_keys(dataval.UN)

    def enter_password(self):
        self.driver.find_element_by_xpath(self.spwd_txt_bx_name).send_keys(dataval.SPWD)

    def click_log_in(self):
        self.driver.find_element_by_xpath(self.clk_login_btn).click()

    def dummy(self):
        pass
