import pytest
from pages.loginpage import LoginPage
from pages.Flightbkpage import Flight_book
@pytest.mark.usefixtures("test_setup")
class Test_Flightbook:
    def test_lgin(self):
        driver = self.driver
        LP = LoginPage(driver)
        LP.click_on_signin_button()
        LP.enter_username()
        LP.enter_password()
        LP.click_log_in()

    def test_flight_book(self):
        driver = self.driver
        FB = Flight_book(driver)
        FB.slct_trip_type()
        FB.slct_passenger_count()
        FB.slct_origin_place()
        FB.slct_month()
        FB.slct_day()
        FB.slct_destination_place()
        FB.slct_class_type()
        FB.click_find_flight_button()


    def test_logout(self):
        driver = self.driver
        driver.find_element_by_xpath("//a[contains(text(),'SIGN-OFF')]").click()