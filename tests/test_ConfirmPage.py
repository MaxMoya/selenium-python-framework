from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


'''class TestConfirmPage(BaseClass):

    def test_confirmpage(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        confirmpage = checkoutpage.checkOutItems()

        confirmpage.checkout().click()
        confirmpage.country_field().send_keys("united")
        countries = confirmpage.dynamic_countries()
        for country in countries:
            if country.text == "United States of America":
                country.click()
                break


        confirmpage.icecream().click()
        confirmpage.purchase().click()
        assert "Success" in confirmpage.success().text'''


class TestConfirmPage(BaseClass):

    def test_confirmpage(self):
        # Initialize the logger
        log = self.getLogger()
        log.info("Starting the test to confirm checkout page functionality.")

        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        confirmpage = checkoutpage.checkOutItems()

        log.info("Navigating to the checkout confirmation page.")
        confirmpage.checkout().click()

        log.info("Typing 'united' into the country field.")
        confirmpage.country_field().send_keys("united")

        countries = confirmpage.dynamic_countries()

        log.info("Iterating through the country suggestions.")
        for country in countries:
            if country.text == "United States of America":
                log.info(f"Found and selecting country: {country.text}")
                country.click()
                break

        log.info("Clicking the checkbox and purchase button.")
        confirmpage.icecream().click()
        confirmpage.purchase().click()

        success_message = confirmpage.success().text
        log.info(f"Checking for success message: '{success_message}'")

        assert "Success" in success_message
        log.info("Test completed successfully. Success message confirmed.")
