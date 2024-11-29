from LIBRARY.lib import Generic_code
from LIBRARY.Excel import read_locators

class Login_Page:
    _locators=read_locators("Locators")
    def __init__(self,driver):
        self.driver=driver
        self.s=Generic_code(self.driver)

    def login(self,login_id):

        try:
            self.s.enter_text(self._locators["txt_login_id"],value=login_id)
        except Exception as e:
            raise Exception(f"Error login ID: {str(e)}")


    def pword(self,pwd):
        try:
            self.s.enter_text(self._locators["txt_pwd"],value=pwd)
        except Exception as e:
            raise Exception(f"Error entering password: {str(e)}")

    def log_btn(self):
        try:
            self.s.click_element(self._locators["btn_login"])
        except Exception as e:
            raise Exception(f"Error clicking login button: {str(e)}")


    def new_applctn(self):
        try:
            self.s.click_element(self._locators["clk_New_Appn"])
        except Exception as e:
            raise Exception(f"Error clicking new application: {str(e)}")

