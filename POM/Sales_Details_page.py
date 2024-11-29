

from selenium.webdriver.support.wait import WebDriverWait

from LIBRARY.lib import Generic_code
from LIBRARY.Excel import read_locators


class Sales_Deatils:
    _locators=read_locators("Locators")

    def _init_(self,driver):
        self.driver=driver
        self.s=Generic_code(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def enter_mob_num(self,mobile_num):
        try:

            self.s.enter_text(self._locators["txt_mblno"],value=mobile_num)
        except Exception as e:
            raise Exception(f"Error entering mobile number :{str(e)}")

    def fetch_btn(self):
        try:
            self.s.click_element(self._locators["btn_fetch_detail"])
        except Exception as e:
            raise Exception(f"Error clicking Fetch details button:{str(e)} ")

    def ok_btn(self):
        try:
            self.s.click_element(self._locators["btn_OK"])
        except Exception as e:
            raise Exception(f"Error clicking ok button:{str(e)}")
