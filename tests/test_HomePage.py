import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomeData import HomeData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_form_submission(self, getData):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        homepage.enter_name().send_keys(getData["name"])
        log.info("First name is " + getData["name"])
        homepage.enter_email().send_keys(getData["email"])
        # dropdown.select_by_index(1)
        self.select_dropdown_by_visible_text(homepage.select_gender_dropddown(),getData["gender"])
        time.sleep(3)
        homepage.submit_button().click()
        message = homepage.success_message_get().text
        assert 'success' in message
        self.driver.refresh()

    # @pytest.fixture(params=[("Saud Malik", "saudmk30@gmail.com", "Male"),("Jane Doe", "jd@gmail.com", "Female")]) this is through tuples
    # @pytest.fixture(params=[{"name": "Saud Malik", "email": "saudmk30@gmail.com", "gender": "Male"}, {"name": "Jane Doe", "email": "jd@gmail.com", "gender": "Female"}]) # this is through dictionary (key value pair)
    @pytest.fixture(params=HomeData.test_home_data)
    def getData(self, request):
        return request.param
