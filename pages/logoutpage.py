class Log_out:
    def __init__(self, driver):
        self.driver = driver
        self.clk_log_out_btn="//a[contains(text(),'SIGN-OFF')]"


    def click_log_out_button(self):
        self.driver.find_element_by_xpath(self.clk_log_out_btn).click()