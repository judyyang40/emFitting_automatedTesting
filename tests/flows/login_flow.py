from tests.pages.signin_page import SignInPage
from wtframework.wtf.web.page import PageFactory


# You can use flow functions to group together a set of calls you make frequently
# so you can reuse them between tests.

def login(username, password, webdriver):

    webdriver.get("http://ec2-52-9-175-55.us-west-1.compute.amazonaws.com/signin.php")
    signin_page = PageFactory.create_page(SignInPage, webdriver)
    signin_page(username, password)

    return signin_page

