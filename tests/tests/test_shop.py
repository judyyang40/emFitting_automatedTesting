from wtframework.wtf.web.page import PageFactory
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER, WTF_CONFIG_READER
from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.utils.test_utils import do_and_ignore
from tests.pages.signin_page import SignInPage
from tests.pages.shop_page import ShopPage
import unittest

class Shop(WTFBaseTest):
	base_url = WTF_CONFIG_READER.get("baseurl")
	shop_url = base_url+'modules/index.php?pkg=shop&contr=shop'

	def teardown(self):
		do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver()) 

	'''def test_01_save_review_without_items(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.save_review_without_items())
		
	def test_11signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.base_url+'modules/index.php?pkg=account&contr=account')
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signin())'''

	def test_filter_brand_macy(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.shop_url)
		shop_page = PageFactory.create_page(ShopPage)
		self.assertTrue(shop_page.filter_brand_macy())

