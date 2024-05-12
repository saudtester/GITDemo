import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures('setup') # we will use this fixture from a parent class instead
class TestOne(BaseClass):

    # driver: webdriver.Chrome = None

    def test_e2e(self):
        log = self.get_logger()
        # making an object of the class which will store the objects of the page
        homepage = HomePage(self.driver)
        # checkoutpage = CheckoutPage(self.driver)
        # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        # homepage.click_shop().click()
        log.info("getting all the card titles")
        checkoutpage = homepage.click_shop()
        # products = self.driver.find_elements(By.XPATH, '//div[@class = "card h-100"]')
        products = checkoutpage.get_products()
        log.info("Going through all the products to search Blackberry")
        for product in products:
            text = product.find_element(By.XPATH, "div/h4/a").text
            if text == 'Blackberry':
                product.find_element(By.XPATH, "div[2]/button").click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*=btn-primary]").click()
        self.driver.find_element(By.XPATH, "//button[@class = 'btn btn-success']").click()
        log.info("Typing the word India")
        self.driver.find_element(By.ID, "country").send_keys('ind')
        self.verify_link("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.CLASS_NAME, 'checkbox-primary').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[class = "btn btn-success btn-lg"]').click()
        class_name = 'alert-dismissible'
        actual_text = self.driver.find_element(By.CLASS_NAME, class_name).text
        assert 'Success! Thasdfnk you!' in actual_text
        self.driver.get_screenshot_as_file('success.png')

        time.sleep(3)


