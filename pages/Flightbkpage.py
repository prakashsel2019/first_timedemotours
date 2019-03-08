
class Flight_book:
    def __init__(self, driver):
        self.driver = driver
        self.select_trip_type = "//input[@value='oneway']"
        self.select_pgr_count = "//select[@name='passCount']/option[1]"
        self.select_from_place = "//select[@name='fromPort']/option[@value='London']"
        self.select_mon = "//select[@name='fromMonth']/option [contains (text(), 'April')]"
        self.select_dy = "//select[@name='fromDay']/option[@value='4']"
        self.select_to_place = "//select[@name='toPort']/option [@value='New York']"
        self.select_cls = "//font[contains(text(),'Economy class ')]"
        self.clk_find_flghts = "//input[@name='findFlights']"

    def slct_trip_type(self):
        self.driver.find_element_by_xpath(self.select_trip_type).click()

    def slct_passenger_count(self):
        self.driver.find_element_by_xpath(self.select_pgr_count).click()

    def slct_origin_place(self):
        self.driver.find_element_by_xpath(self.select_from_place).click()

    def slct_month(self):
        self.driver.find_element_by_xpath(self.select_mon).click()

    def slct_day(self):
        self.driver.find_element_by_xpath(self.select_dy).click()

    def slct_destination_place(self):
        self.driver.find_element_by_xpath(self.select_to_place).click()

    def slct_class_type(self):
        self.driver.find_element_by_xpath(self.select_cls).click()

    def click_find_flight_button(self):
        self.driver.find_element_by_xpath(self.clk_find_flghts).click()



        # def test_flightbooking(self):
        #     driver.find_element_by_xpath("//input[@value='oneway']").click()
        #     driver.find_element_by_xpath("//select[@name='passCount']/option[1]").click()
        #     driver.find_element_by_xpath("//select[@name='fromPort']/option[@value='London']").click()
        #     driver.find_element_by_xpath("//select[@name='fromMonth']/option [contains (text(), 'April')]").click()
        #     driver.find_element_by_xpath("//select[@name='fromDay']/option[@value='4']").click()
        #     driver.find_element_by_xpath("//select[@name='toPort']/option [@value='New York']").click()
        #     driver.find_element_by_xpath("//font[contains(text(),'Economy class ')]").click()
        #     driver.find_element_by_xpath("//input[@name='findFlights']").click()
        #     time.sleep(5)
        #     driver.find_element_by_xpath("//input[@value='Blue Skies Airlines$631$273$14:30']").click()
        #     driver.find_element_by_xpath("//input[@name='reserveFlights']").click()
        #     time.sleep(5)