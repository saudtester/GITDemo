from selenium.webdriver.common.by import By
from selenium import webdriver


class CheckoutPage:

    getproducts = (By.XPATH, '//div[@class = "card h-100"]')
    # getting the driver from the test case class

    def __init__(self, driver):
        self.driver = driver

    def get_products(self):
        return self.driver.find_elements(*CheckoutPage.getproducts)
