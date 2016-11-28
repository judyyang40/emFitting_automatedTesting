from wtframework.wtf.web.page import PageFactory
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER, WTF_CONFIG_READER
from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.utils.test_utils import do_and_ignore
from tests.pages.index_page import IndexPage
from tests.pages.signin_page import SignInPage
import unittest

class Index(WTFBaseTest):
	base_url = WTF_CONFIG_READER.get("baseurl")
	index_url = base_url+'modules/index.php?pkg=main&contr=main'

	def teardown(self):
		do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver()) 

	def test_00_goto_signin_from_emshare(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_signin_from_emshare())

	def test_01_goto_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_signin())

	def test_02_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.base_url+'modules/index.php?pkg=account&contr=account')
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signin())

	def test_no_signin_link_after_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.no_signin_link_after_signin())

	def test_click_home_logo(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.click_home_logo())

	def test_search_in_navigation_bar(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.search_in_navigation_bar())

	def test_goto_home(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_home())

	def test_goto_tryon(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_tryon())

	def test_goto_shop(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_shop())

	def test_goto_emshare(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_emshare())

	def test_goto_me(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_me())

	def test_view_demo(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.view_demo())

	def test_goto_shopping_cart(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_shopping_cart())

	def test_goto_face_tryon(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_face_tryon())

	def test_goto_hand_tryon(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_hand_tryon())

	def test_goto_soho_shop(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_soho_shop())

	def test_goto_glasses_category(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_glasses_category())

	def test_click_product_in_shop(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.click_product_in_shop())

	def test_goto_amazon(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_amazon())

	def test_profile_pic_in_emshare(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.profile_pic_in_emshare())

	def test_goto_me_from_emshare(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_me_from_emshare())

	def test_goto_emshare(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.index_url)
		index_page = PageFactory.create_page(IndexPage)
		self.assertTrue(index_page.goto_emshare())
