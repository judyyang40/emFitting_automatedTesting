from tests.pages.signin_page import SignInPage
from wtframework.wtf.web.page import PageFactory


# You can use flow functions to group together a set of calls you make frequently
# so you can reuse them between tests.

def signin_flow(username, password, webdriver):

    webdriver.get("https://qa.emfitting.com/signin.php")
    signin_page = PageFactory.create_page(SignInPage, webdriver)
    signin_page.signin(username, password)

    return signin_page

