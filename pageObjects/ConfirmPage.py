from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfirmPage:

    btn_checkout = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    fld_country = (By.CSS_SELECTOR, "#country")
    dyn_country = (By.CSS_SELECTOR, ".suggestions > ul > li > a")
    chk_icecream = (By.CSS_SELECTOR, "[for='checkbox2']")
    btn_purchase = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
    fld_success = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")


    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        return self.driver.find_element(*ConfirmPage.btn_checkout)

    def country_field(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(ConfirmPage.fld_country))

    def dynamic_countries(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(ConfirmPage.dyn_country))

    def icecream(self):
        return self.driver.find_element(*ConfirmPage.chk_icecream)

    def purchase(self):
        return self.driver.find_element(*ConfirmPage.btn_purchase)

    def success(self):
        return self.driver.find_element(*ConfirmPage.fld_success)

