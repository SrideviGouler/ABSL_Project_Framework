from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from pytest import fixture
from datetime import datetime
import pytest
import os
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",dest="browser",default="chrome")
    parser.addoption("--env",action="store",dest="env",default="Test")
    parser.addoption("--timeout",action="store",dest="Max_timeout",default=10)
#--

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir=os.path.join(os.path.dirname(__file__),"REPORTS")
    now=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath=f"{report_dir}/reports_{now}.html"

class Test_Configurations:
    url="https://leappreprod.adityabirlasunlifeinsurance.com/preprod/#/login"
    log_id="IN076761"
    password = "str"


class Stage_configurations:
    url = "https://leappreprod.adityabirlasunlifeinsurance.com/preprod/#/login"
    log_id = "IN076761"
    password = "str"
@fixture
def _config(request):
    env_var=request.config.option.env.upper()
    if env_var=="TEST":
        return Test_Configurations
    elif env_var=="STAGE":
        return Stage_configurations
    else:
        raise Exception("Unknown Env")

@fixture
def _driver(_config,request):
    browser_class=request.config.option.browser.upper()
    if browser_class=="CHROME":
        driver=Chrome()
    elif browser_class=="FIREFOX":
        driver=Firefox()
    elif browser_class=="EDGE":
        driver=Edge()
    else:
        raise Exception(f"{browser_class} not supported")
    driver.maximize_window()
    driver.get(_config.url)
    yield driver
    driver.close()


