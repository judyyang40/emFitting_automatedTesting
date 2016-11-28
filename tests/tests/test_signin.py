from wtframework.wtf.web.page import PageFactory
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER, WTF_CONFIG_READER
from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.utils.test_utils import do_and_ignore
from tests.pages.signin_page import SignInPage
import unittest

class SignIn(WTFBaseTest):
	base_url = WTF_CONFIG_READER.get("baseurl")
	signin_url = base_url+'modules/index.php?pkg=account&contr=account'

	def teardown(self):
		do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver()) 

	def test_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.signin_url)
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signin())

	def test_signin_with_incorrect_password(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.signin_url)
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signin_with_incorrect_password())

	def test_signup(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.signin_url)
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signup())

	def test_signup_with_bad_email(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.signin_url)
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signup_with_bad_email())

	def test_signup_with_unmatching_passwords(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.signin_url)
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signup_with_unmatching_passwords())

	def test_signup_with_existing_email(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.signin_url)
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signup_with_existing_email())

	def test_signup_with_short_password(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.signin_url)
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signup_with_short_password())

	def test_forgot_password(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.signin_url)
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.forgot_password())

	def test_send_reset_password_email(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.signin_url)
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.send_reset_password_email())

	def test_send_reset_password_email_with_bad_email(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.signin_url)
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.send_reset_password_email_with_bad_email())

