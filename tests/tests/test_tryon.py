from wtframework.wtf.web.page import PageFactory
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER, WTF_CONFIG_READER
from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.utils.test_utils import do_and_ignore
from tests.pages.signin_page import SignInPage
from tests.pages.tryon_page import TryonPage
import unittest

class Tryon(WTFBaseTest):
	base_url = WTF_CONFIG_READER.get("baseurl")
	tryon_url = base_url+'modules/index.php?pkg=tryon&contr=tryon'

	def teardown(self):
		do_and_ignore(lambda: WTF_WEBDRIVER_MANAGER.close_driver()) 

	def test_01_save_review_without_items(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.save_review_without_items())

	def test_02_save_review_without_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.save_review_without_signin())

	def test_03_view_all_results_without_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.view_all_results_without_signin())

	def test_08_save_tryon_without_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.save_tryon_without_signin())

	def test_09_share_tryon_without_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.share_tryon_without_signin())

	def test_07_view_result_and_items(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.view_result_and_items())

	def test_04_save_settings_without_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.save_settings_without_signin())
		
	def test_05_upload_photo_without_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.upload_photo_without_signin())
		
	def test_06_take_snapshot_without_signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.take_snapshot_without_signin())

	def test_10_goto_item_from_view_result(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.goto_item_from_view_result())
		
	def test_11signin(self):
		webdriver = WTF_WEBDRIVER_MANAGER.new_driver()
		webdriver.get(self.base_url+'modules/index.php?pkg=account&contr=account')
		signin_page = PageFactory.create_page(SignInPage)
		self.assertTrue(signin_page.signin())

	def test_choose_tryon_pic(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.choose_tryon_pic())

	def test_choose_tryon_items(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.choose_tryon_items())

	def test_use_up_arrow(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.use_up_arrow())

	def test_use_grow_icon(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.use_grow_icon())

	def test_use_right_rotate_icon(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.use_right_rotate_icon())

	def test_clear_tryon_items(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.clear_tryon_items())

	def test_filter_gender_male(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.filter_gender_male())

	def test_filter_brand_soho(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.filter_brand_soho())

	def test_search_for_items(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.search_for_items())

	def test_show_category_necklace(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.show_category_necklace())

	def test_show_dropdown(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.show_dropdown())

	def test_delete_tryon_item_from_dropdown(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.delete_tryon_item_from_dropdown())

	def test_save_tryon_item_position(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.save_tryon_item_position())

	def test_drag_tryon_item(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.drag_tryon_item())

	def test_drag_to_resize_tryon_item(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.drag_to_resize_tryon_item())

	def test_save_shirt_ratio_with_positioning_of_other_dragged_item(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.save_shirt_ratio_with_positioning_of_other_dragged_item())	

	def test_save_shirt_positioning_and_ratio(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.save_shirt_positioning_and_ratio())		

	def test_move_item_to_top_from_dropdown(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.move_item_to_top_from_dropdown())		

	def test_move_item_to_bottom_from_dropdown(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.move_item_to_bottom_from_dropdown())		

	def test_switch_to_hand(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.switch_to_hand())

	def test_switch_back_to_face_from_hand(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.switch_back_to_face_from_hand())

	def test_delete_tryon_item_from_current(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.delete_tryon_item_from_current())

	def test_choose_tryon_item_without_photo(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.choose_tryon_item_without_photo())

	def test_save_settings_without_tryon_items(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.save_settings_without_tryon_items())

	def test_quick_view(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.quick_view())

	def test_save_tryon(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.save_tryon())

	def test_tutorial(self):
		webdriver = WTF_WEBDRIVER_MANAGER.get_driver()
		webdriver.get(self.tryon_url)
		tryon_page = PageFactory.create_page(TryonPage)
		self.assertTrue(tryon_page.tutorial())