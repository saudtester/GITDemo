from selenium.webdriver.common.by import By
from selenium import webdriver
from pageObjects.CheckoutPage import CheckoutPage

class HomePage:
    shop = (By.LINK_TEXT, "Shop")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.XPATH, "//input[@name='email']")
    gender = (By.ID, 'exampleFormControlSelect1')
    submit = (By.CSS_SELECTOR, "input[value='Submit']")
    success_message = (By.CLASS_NAME, 'alert.alert-success.alert-dismissible')
    getproducts = (By.XPATH, '//div[@class = "card h-100"]')

    # getting the driver from the test case class
    def __init__(self, driver):
        self.driver = driver

    def click_shop(self):
        # we use * for argument unpacking so tuple will be passed as two arguments not one
        self.driver.find_element(*HomePage.shop).click()
        checkoutPage = CheckoutPage(self.driver) #everytime we click on shop it will take to the checkout page so we'll initiate checkout page object here
        return checkoutPage

    def enter_name(self):
        return self.driver.find_element(*HomePage.name)

    def enter_email(self):
        return self.driver.find_element(*HomePage.email)

    def select_gender_dropddown(self):
        return self.driver.find_element(*HomePage.gender)

    def success_message_get(self):
        return self.driver.find_element(*HomePage.success_message)

    def submit_button(self):
        return self.driver.find_element(*HomePage.submit)

    def get_products(self):
        return self.driver.find_elements(*HomePage.getproducts)
