
# from LIBRARY.lib import Generic_code
# from LIBRARY.Excel import read_locators
#
#
# class Sales_Deatils:
#     _locators=read_locators("Locators")
#
#     def _init_(self,driver):
#         self.driver=driver
#         self.s=Generic_code(self.driver)
#
#     def enter_mob_num(self,mobile_num):
#         try:
#
#             self.s.enter_text(self._locators["txt_mblno"],value=mobile_num)
#         except Exception as e:
#             raise Exception(f"Error entering mobile number :{str(e)}")
#
#     def fetch_btn(self):
#         try:
#             self.s.click_element(self._locators["btn_fetch_detail"])
#         except Exception as e:
#             raise Exception(f"Error clicking Fetch details button:{str(e)} ")
#
#     def ok_btn(self):
#         try:
#             self.s.click_element(self._locators["btn_OK"])
#         except Exception as e:
#             raise Exception(f"Error clicking ok button:{str(e)}")

from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from LIBRARY.lib import Generic_code
from LIBRARY.Excel import read_locators
from selenium.webdriver.common.by import By

class Sales_details:
    _locators=read_locators("Locators")
    def _init_(self,driver):
        self.driver=driver
        self.s = Generic_code(self.driver)


    def enter_mob_num(self, mobile_num):
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








    # def enter_code(self):
    #     a=self.s.value(self._locators["txt_enter_code"])
    #     # bank_name = a.get_attribute('value')
    #     try:
    #         w = WebDriverWait(self.driver, 10)
    #         v = visibility_of_element_located(a)
    #         w.until(v, message=f"element not found locators")
    #
    #         # if bank_name == "ZW1816 - Bank of Maharashtra":
    #         #     print("ZW1816 - Bank of Maharashtra")
    #         # else:
    #         #     print(f"Unexpected bank name: {bank_name}")
    #     except Exception as e:
    #         print(f"Error occurred: {str(e)}")
    #         raise
    #
    # def bank_cust_id(self,cust_id):
    #     try:
    #         self.s.enter_text(self._locators["txt_bank_cust_id"], value=cust_id)
    #     except Exception as e:
    #         print(f"Bank customer Id not match : {str(e)}")
    #         raise e
    #
    #
    # def continue_btn(self):
    #     try:
    #         self.s.click_element(self._locators["btn_continue"])
    #     except Exception as e:
    #         print(f"continue button click failed : {str(e)}")
    #         raise e