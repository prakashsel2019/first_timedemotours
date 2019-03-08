from testdata import constants as dataval

class RegPage:
    def __init__(self, driver):
        self.driver = driver
        self.cl_reg_tab = "//a[contains(text(),'REGISTER')]"
        self.fn_txt_bx_name = "//input[@name='firstName']"
        self.ln_txt_bx_name = "//input[@name='lastName']"
        self.ph_txt_bx_name = "//input[@name='phone']"
        self.add_txt_bx_name = "//input[@name='address1']"
        self.cty_txt_bx_name = "//input[@name='city']"
        self.stat_txt_bx_name = "//input[@name='state']"
        self.pcode_txt_bx_name = "//input[@name='postalCode']"
        self.email_txt_bx_name = "//input[@id='email']"
        self.pwd_txt_bx_name = "//input[@name='password']"
        self.cpwd_txt_bx_name = "//input[@name='confirmPassword']"
        self.submit_btn_name = "//input[@name='register']"

    def click_on_registor_tab(self):
        self.driver.find_element_by_xpath(self.cl_reg_tab).click()

    def enter_firstname(self):
        self.driver.find_element_by_xpath(self.fn_txt_bx_name).send_keys(dataval.FN)

    def enter_lastname(self):
        self.driver.find_element_by_xpath(self.ln_txt_bx_name).send_keys(dataval.LN)

    def enter_phonenumber(self):
        self.driver.find_element_by_xpath(self.ph_txt_bx_name).send_keys(dataval.PH)

    def enter_address(self):
        self.driver.find_element_by_xpath(self.add_txt_bx_name).send_keys(dataval.ADD)

    def enter_city(self):
        self.driver.find_element_by_xpath(self.cty_txt_bx_name).send_keys(dataval.CITY)

    def enter_state(self):
        self.driver.find_element_by_xpath(self.stat_txt_bx_name).send_keys(dataval.ST)

    def enter_pincode(self):
        self.driver.find_element_by_xpath(self.pcode_txt_bx_name).send_keys(dataval.PC)

    def enter_email(self):
        self.driver.find_element_by_xpath(self.email_txt_bx_name).send_keys(dataval.EMAIL)

    def enter_password(self):
        self.driver.find_element_by_xpath(self.pwd_txt_bx_name).send_keys(dataval.PWD)

    def enter_con_password(self):
        self.driver.find_element_by_xpath(self.cpwd_txt_bx_name).send_keys(dataval.CPWD)

    def click_on_sumbit(self):
        self.driver.find_element_by_xpath(self.submit_btn_name).click()

