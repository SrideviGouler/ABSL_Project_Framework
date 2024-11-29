from LIBRARY.lib import Generic_code
from LIBRARY.Excel import read_locators,read_headers,read_data
from pytest import mark
from POM.Login_page import Login_Page
headers=read_headers("test_login_positive","Test_data")
data=read_data("test_login_positive","Test_data")
@mark.parametrize(headers,data)
def test_login(_driver,login_id,password):
    s=Generic_code(_driver)
    logpage=Login_Page(_driver)
    try:
        logpage.login(login_id)
        logpage.pword(password)
        logpage.log_btn()
        logpage.new_applctn()
    except Exception as e:
        print(f"Test failed for user {login_id} with error: {str(e)}")
        raise

