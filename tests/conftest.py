import time

import pytest
from selenium import webdriver
driver = None

def pytest_addoption(parser):  # giving our browser name as a command line option
    parser.addoption(  # giving the name of the option, if no option name in command line
        # then it will be considered as 'chrome
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption('--browser_name')
    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        driver = webdriver.Firefox()
    elif browser_name == 'IE':
        print('IE driver')
    else:
        driver = webdriver.Chrome()
    # Navigate to the desired URL
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # Maximize the browser window
    driver.maximize_window()

    # Attach the WebDriver to the test class
    request.cls.driver = driver

    # Allow tests to run
    yield

    # Close the WebDriver after tests are done
    time.sleep(3)
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)

