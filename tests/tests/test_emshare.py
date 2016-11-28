from wtframework.wtf.web.page import PageFactory
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER, WTF_CONFIG_READER
from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.utils.test_utils import do_and_ignore
from tests.pages.signin_page import SignInPage
from tests.pages.emshare_page import EmSharePage
import unittest

class EmShare(WTFBaseTest):
	base_url = WTF_CONFIG_READER.get("baseurl")
	emshare_url = base_url+'modules/index.php?pkg=emshare&contr=emshare'

	def teardown(self):
		do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver()) 

	def test_00_post_without_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.post_without_signin())

	def test_01_goto_signup_from_emshare_without_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.goto_signup_from_emshare_without_signin())		

	def test_02_goto_my_page_from_emshare_without_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.goto_my_page_from_emshare_without_signin())

	def test_03_comment_without_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.comment_without_signin())

	def test_04_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.base_url+'modules/index.php?pkg=account&contr=account')
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signin())

	def test_post_text_sharing(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.post_text_sharing())

	def test_comment(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.comment())

		#manual-check invite email manually
	'''def test_invite_friends(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.invite_friends())'''

	def test_signup_from_emshare(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.signup_from_emshare())

	def test_goto_my_page_from_emshare(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.goto_my_page_from_emshare())

	def test_preview_youtube_video_before_posting(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.preview_youtube_video_before_posting())

	def test_preview_vimeo_video_before_posting(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.preview_vimeo_video_before_posting())

	def test_post_sharing_with_youtube_url(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.post_sharing_with_youtube_url())

	def test_post_sharing_with_vimeo_url(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.post_sharing_with_vimeo_url())

	def test_post_empty_sharing(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.post_empty_sharing())

	def test_empty_comment(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.emshare_url)
		emshare_page = PageFactory.create_page(EmSharePage)
		self.assertTrue(emshare_page.empty_comment())
	