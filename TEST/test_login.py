from time import sleep

from LIBRARY.lib import Generic_code
from LIBRARY.Excel import read_locators,read_headers,read_data
from pytest import mark
from POM.Login_page import Login_Page
from POM.Sales_Details_page import Sales_details

headers=read_headers("test_login_positive","Test_data")
data=read_data("test_login_positive","Test_data")

@mark.parametrize(headers,data)
def test_login(_driver,login_id,password,mobile_num):
    s=Generic_code(_driver)
    logpage=Login_Page(_driver)
    sales_page = Sales_details(_driver)

    try:
        logpage.login(login_id)
        logpage.pword(password)
        logpage.log_btn()
        logpage.new_applctn()
        sleep(2)
        sales_page.enter_mob_num(mobile_num)
        sleep(2)
        sales_page.fetch_btn()
        sleep(2)
        sales_page.ok_btn()
    except Exception as e:
        print(f"Test failed for user {login_id} with error: {str(e)}")
        raise
        # except Exception as es:
        # print(f"Test failed for Sales Details page for monile number{mobile_number} :{str(e)}")
        # raise

# def test_sales_details_page(_driver,headers,data,mobile_number):
#     s=Generic_code(_driver)
#     sales_page=Sales_Deatils(_driver)
#     try:
#         sales_page.Proposers_Details(mobile_number)
#         sales_page.fetch_btn()
#         sales_page.ok_btn()
#     except Exception as e:
#         print(f"Test failed for Sales Details page for monile number{mobile_number} :{str(e)}")
#         raise
