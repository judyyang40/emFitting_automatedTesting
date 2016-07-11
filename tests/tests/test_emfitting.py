from wtframework.wtf.web.page import PageFactory
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER, WTF_CONFIG_READER
from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.utils.test_utils import do_and_ignore
from tests.flows.signin_flows import signin_flow
from tests.pages.signin_page import SignInPage
from tests.pages.tryon_page import TryOnPage
from tests.pages.shop_page import ShopPage
from tests.pages.PageIndex1 import PageIndex1
from tests.pages.emShare_page import EmShare
from tests.pages.fashion_page import Fashion
from tests.pages.userprofile_page import UserProfile
from tests.pages.home_page import HomePage
import unittest

class Test(WTFBaseTest):
	base_url = WTF_CONFIG_READER.get("baseurl")

	def teardown(self):
		do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver()) 

	def test_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.base_url+'signin.php')
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signin_test())

	def test_home(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.base_url+'index-1.php')
		home_page = PageFactory.create_page(HomePage)
		self.assertTrue(home_page.home_test())

	def test_tryon(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		#signin_page = signin_flow("aaa@gmail.com", "123456", webdriver)
		webdriver.get(self.base_url+'tryonindex.php')
		tryon_page = PageFactory.create_page(TryOnPage)
		self.assertTrue(tryon_page.tryon_test())

	def test_shop(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		#signin_page = signin_flow("aaa@gmail.com", "123456", webdriver)
		webdriver.get(self.base_url+'Shop.php')
		shop_page = PageFactory.create_page(ShopPage)
		self.assertTrue(shop_page.shop_test())

	def test_emShare(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.base_url+'SHARE.php')
		emShare_page = PageFactory.create_page(EmShare)
		self.assertTrue(emShare_page.emShare_test())

	def test_fashion(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.base_url+'Fashion%20News.php')
		fashion_page = PageFactory.create_page(Fashion)
		self.assertTrue(fashion_page.fashion_test())

	def test_userprofile(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		signin_page = signin_flow("aaa@gmail.com", "123456", webdriver)
		webdriver.get(self.base_url+'My.php')
		my_page = PageFactory.create_page(UserProfile)
		self.assertTrue(my_page.userprofile_test())