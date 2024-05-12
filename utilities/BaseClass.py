import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage


@pytest.mark.usefixtures('setup')  # now we can inherit this class in other classes and this
# fixture will be utilized for each without the need for declaring it each time
class BaseClass:

    def verify_link(self, text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_dropdown_by_visible_text(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        # argument below will capture the file name of the test case
        # logger = logging.getLogger(__name__) #it is for default name
        logger = logging.getLogger(loggerName) #this will give us the name of the child method which will call it
        filehandler = logging.FileHandler('logs.log')  # it will save the log file to filehandler object
        # format is an industry accepted format
        Format = logging.Formatter('%(asctime)s :%(levelname)s :%(name)s :%(message)s')
        filehandler.setFormatter(Format)
        logger.addHandler(filehandler)  # it passed the log file info to the addhandler method
        # add handler needs to know the file location and log format
        logger.setLevel(logging.DEBUG)  # it will set the level from Info to critical
        return logger



# pass pass is a keyword in python which does nothing
