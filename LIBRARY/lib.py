from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

def _wait(func):
    def wrapper(*args,**kwargs):
        instance,locators=args
        w=WebDriverWait(instance.driver,10)
        v=visibility_of_element_located(locators)
        w.until(v,message=f"element not found{locators}")
        return func(*args,**kwargs)
    return wrapper

def wait_cls(cls):
    for key,value in cls.__dict__.items():
        if callable(value) and key!="__init__":
            setattr(cls,key,_wait(value))
    return cls
@wait_cls
class Generic_code:
    def __init__(self,driver):
        self.driver=driver
    def value(self,locator,/):
        self.driver.find_element(*locator)
    def click_element(self,locator,/):
        self.driver.find_element(*locator).click()

    def enter_text(self,locator,/,*,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def select_item(self,locator,/,*,item):
        element=self.driver.find_element(*locator)
        select=Select(element)
        select.select_by_visible_text(item)
