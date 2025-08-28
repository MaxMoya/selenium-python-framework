
from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self):
        log = self.getLogger()
        homepage= HomePage(self.driver)
        homepage.getName().send_keys("Max")
        homepage.getEmail().send_keys("email@host.com")
        homepage.getCheckBox().click()
        self.selectOptionByText(homepage.getGender(), "Male")

        homepage.submitForm().click()

        alertText = homepage.getSuccessMessage().text

        assert ("Success" in alertText)
        self.driver.refresh()

    '''@pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param'''

