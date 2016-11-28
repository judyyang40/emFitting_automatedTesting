from wtframework.wtf.web.page import PageObject, InvalidPageError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from wtframework.wtf.web.webdriver import WTF_CONFIG_READER
from wtframework.wtf.config import WTF_TIMEOUT_MANAGER
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TryonPage(PageObject):
	base_url = WTF_CONFIG_READER.get("baseurl")
	require_signin_xpath = "//div[contains(text(), 'You need to sign in before using this function.')]"
	require_tryon_pic_xpath = "//b[contains(text(), 'Please select the pictures you want to try!')]"
	require_tryon_item_xpath = "//b[contains(text(), 'Please select a try on merchandise!')]"
	login_xpath = "//h2[contains(text(), 'Login')]"

	def _validate_page(self, webdriver):
		if not self.base_url+'modules/index.php?pkg=tryon&contr=tryon' in webdriver.current_url:
			raise InvalidPageError("This page did not pass page validation.")

	def choose_tryon_pic(self):
		tryon_pic = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shichuantpl_id4694")), 'Timed Out')
		tryon_pic.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "phone")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def choose_tryon_items(self):
		tryon_pic = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shichuantpl_id4694")), 'Timed Out')
		tryon_pic.click()
		tryon_item1 = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid577")), 'Timed Out')
		tryon_item1.click()
		glasses = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-glasses")), 'Timed Out')
		glasses.click()
		tryon_item2 = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid42")), 'Timed Out')
		tryon_item2.click()

		'''tryon_item1_img = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp577")), 'Timed Out')
		item1_attr = tryon_item1_img.get_attribute("style")
		attr_dic = self.parse_item_attributes(item1_attr)
		attr_dic2 = self.parse_item_attributes(item1_attr)
		result = self.compare_item_attributes(attr_dic, attr_dic2)'''

		return True

	def parse_item_attributes(self, attr):
		array = attr.split(';')
		attr_dic = {}
		for attribute in array:
			if attribute.startswith(' width'):
				attr_dic['width'] = float(attribute[8:-2])
			elif attribute.startswith(' height'):
				attr_dic['height'] = float(attribute[9:-2])
			elif attribute.startswith(' top'):
				attr_dic['top'] = float(attribute[6:-2])
			elif attribute.startswith(' left'):
				attr_dic['left'] = float(attribute[7:-2])
		return attr_dic

	def compare_item_attributes(self, attr1, attr2):
		flag = True
		for key in attr1:
			a = attr1[key]
			b = attr2[key]
			if(abs(a - b) > 2):
				flag = False
				break
		return flag

	def save_review_without_items(self):
		savereview = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Save For Review')]")), 'Timed Out')
		savereview.click()
		try:
			WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.require_tryon_item_xpath)), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def save_review_without_signin(self):
		tryon_pic = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shichuantpl_id4375")), 'Timed Out')
		tryon_pic.click()
		tryon_item = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid579")), 'Timed Out')
		tryon_item.click()
		savereview = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Save For Review')]")), 'Timed Out')
		savereview.click()
		try:
			WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#tryon_results>.try-results")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def view_all_results_without_signin(self):
		self.save_review_without_signin()
		tryon_item = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid580")), 'Timed Out')
		tryon_item.click()
		savereview = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Save For Review')]")), 'Timed Out')
		savereview.click()
		self.webdriver.find_element_by_xpath("//a[contains(text(), 'View All')]").click()
		num = len(self.webdriver.find_elements_by_css_selector(".try-results.col-xs-3"))
		return num == 2

	def view_result_and_items(self):
		self.save_review_without_signin()
		self.webdriver.find_elements_by_class_name("fitting-results")[1].click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Black Cardigan')]")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def goto_item_from_view_result(self):
		self.view_result_and_items()
		self.webdriver.find_element_by_xpath("//a[contains(text(), 'View Item')]").click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "product-description")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def save_tryon_without_signin(self):
		self.view_result_and_items()
		self.webdriver.find_element_by_css_selector(".bottom-btn>a:nth-child(1)").click()
		try:
			WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.login_xpath)), 'Timed Out')
			return True
		except TimeoutException:
			return False
		
	def share_tryon_without_signin(self):
		self.view_result_and_items()
		self.webdriver.find_element_by_css_selector(".bottom-btn>a:nth-child(2)").click()
		try:
			WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.login_xpath)), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def use_up_arrow(self):
		self.choose_tryon_items()
		tryon_item_img = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp42")), 'Timed Out')
		item_attr = tryon_item_img.get_attribute("style")
		before = self.parse_item_attributes(item_attr)
		up = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@act='wy_up']")))
		for x in range(0, 3):
			up.click()
		item_attr = tryon_item_img.get_attribute("style")
		after = self.parse_item_attributes(item_attr)
		diff = before['top']-after['top']
		return (diff < 11 and diff > 9)

	def use_grow_icon(self):
		self.choose_tryon_items()
		tryon_item_img = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp42")), 'Timed Out')
		item_attr = tryon_item_img.get_attribute("style")
		before = self.parse_item_attributes(item_attr)
		up = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@act='plus']")))
		for x in range(0, 3):
			up.click()
		item_attr = tryon_item_img.get_attribute("style")
		after = self.parse_item_attributes(item_attr)
		return (after['width'] > before['width'])

	def use_right_rotate_icon(self):
		self.choose_tryon_items()
		rotate_right = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@act='right']")))
		for x in range(0, 3):
			rotate_right.click()
		tryon_item_img = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp42")), 'Timed Out')
		item_attr = tryon_item_img.get_attribute("style")
		degree = int(item_attr.replace('deg);', 'rotate(').split('rotate(')[1])
		return degree == 10

	def clear_tryon_items(self):
		self.choose_tryon_items()
		clear = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "Clear")))
		clear.click()
		WebDriverWait(self.webdriver, 10).until(EC.invisibility_of_element_located((By.ID, "cur_item_577")), 'Timed Out')
		WebDriverWait(self.webdriver, 10).until(EC.invisibility_of_element_located((By.ID, "cur_item_42")), 'Timed Out')
		WebDriverWait(self.webdriver, 10).until(EC.invisibility_of_element_located((By.ID, "tryimgtmp577")), 'Timed Out')
		try:
			WebDriverWait(self.webdriver, 10).until(EC.invisibility_of_element_located((By.ID, "tryimgtmp42")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def filter_gender_male(self):
		show = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "showButton")), 'Timed Out')
		show.click()
		male = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Male")), 'Timed Out')
		male.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "trypicid577")), 'Timed Out')
			return True
		except TimeoutException:
			return False	

	def filter_brand_soho(self):
		show = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "brandButton")), 'Timed Out')
		show.click()
		soho = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "SOHO IMAGE NY")), 'Timed Out')
		soho.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "trypicid577")), 'Timed Out')
			return True
		except TimeoutException:
			return False
		'''try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid288")), 'Timed Out')
			return True
		except TimeoutException:
			return False'''

	def search_for_items(self):
		search = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "textSearch")), 'Timed Out')
		search.send_keys("blue")
		search_btns = self.webdriver.find_elements_by_css_selector(".fa-search")
		search_btns[1].click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid60")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def show_category_necklace(self):
		necklace = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-necklaces")), 'Timed Out')
		necklace.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid499")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def drag_tryon_item(self):
		self.choose_tryon_items()
		glasses = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp42")), 'Timed Out')
		chain = ActionChains(self.webdriver)
		chain.move_to_element_with_offset(glasses, 3, 3)
		chain.click_and_hold()
		chain.move_by_offset(200, 200)
		chain.release()
		chain.perform()
		attr = glasses.get_attribute("style")
		after = self.parse_item_attributes(attr)
		return after['top'] >= 425 and after['top'] <= 435 and after['left'] >= 435 and after['left'] <= 445

	def drag_to_resize_tryon_item(self):
		self.choose_tryon_items()
		glasses = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp42")), 'Timed Out')
		attr_before = glasses.get_attribute("style")
		before = self.parse_item_attributes(attr_before)
		chain = ActionChains(self.webdriver)
		chain.move_to_element(glasses)
		chain.perform()
		drag_btn = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#tryimgtmp42>.coor")), 'Timed Out')
		chain.move_to_element(drag_btn)
		chain.click_and_hold()
		chain.move_by_offset(100, 100)
		chain.release()
		chain.perform()
		attr_after = glasses.get_attribute("style")
		after = self.parse_item_attributes(attr_after)

		return before['width'] < after['width']

	def choose_tryon_items_for_save_settings(self):
		tryon_pic = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shichuantpl_id4693")), 'Timed Out')
		tryon_pic.click()
		glasses = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-glasses")), 'Timed Out')
		glasses.click()
		tryon_item1 = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid254")), 'Timed Out')
		tryon_item1.click()	
		necklace = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-necklaces")), 'Timed Out')
		necklace.click()
		tryon_item2 = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid499")), 'Timed Out')
		tryon_item2.click()	

	def save_tryon_item_position(self):
		self.choose_tryon_items_for_save_settings()
		tryon_item_img = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp254")), 'Timed Out')
		down = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@act='wy_down']")))
		for x in range(0, 3):
			down.click()
		item_attr = tryon_item_img.get_attribute("style")
		before = self.parse_item_attributes(item_attr)
		save_config = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "saveConfig")), 'Timed Out')
		save_config.click()

		self.webdriver.refresh()
		self.choose_tryon_items_for_save_settings()
		tryon_item_img_after = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp254")), 'Timed Out')
		item_attr_after = tryon_item_img_after.get_attribute("style")
		after = self.parse_item_attributes(item_attr_after)

		diff = abs(before['top']-after['top'])
		return (diff < 2)
		
	def save_shirt_ratio_with_positioning_of_other_dragged_item(self):
		self.choose_tryon_items_for_save_settings()
		top = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-garments")), 'Timed Out')
		top.click()
		shirt = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid578")), 'Timed Out')
		shirt.click()	
		plus = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@act='plus']")))
		for x in range(0, 3):
			plus.click()
		shirt_attr = shirt.get_attribute("style")
		shirt_dic_before = self.parse_item_attributes(shirt_attr)

		glasses = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp254")), 'Timed Out')
		chain = ActionChains(self.webdriver)
		chain.move_to_element_with_offset(glasses, 3, 3)
		chain.click_and_hold()
		chain.move_by_offset(0, 20)
		chain.release()
		chain.perform()
		glasses_attr = glasses.get_attribute("style")
		glasses_dic_before = self.parse_item_attributes(glasses_attr)

		save_config = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "saveConfig")), 'Timed Out')
		save_config.click()

		self.webdriver.refresh()
		self.choose_tryon_items_for_save_settings()
		top = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-garments")), 'Timed Out')
		top.click()
		shirt = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid578")), 'Timed Out')
		shirt.click()

		shirt_after = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid578")), 'Timed Out')
		shirt_attr_after = shirt_after.get_attribute("style")
		shirt_dic_after = self.parse_item_attributes(shirt_attr_after)
		glasses_after = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp254")), 'Timed Out')
		glasses_attr_after = glasses_after.get_attribute("style")
		glasses_dic_after = self.parse_item_attributes(glasses_attr_after)
		shirt_result = self.compare_item_attributes(shirt_dic_before, shirt_dic_after)
		glasses_result = self.compare_item_attributes(glasses_dic_before, glasses_dic_after)

		return shirt_result and glasses_result

	def save_shirt_positioning_and_ratio(self):
		tryon_pic = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shichuantpl_id4693")), 'Timed Out')
		tryon_pic.click()
		tryon_item3 = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid578")), 'Timed Out')
		tryon_item3.click()	

		tryon_item_img = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp578")), 'Timed Out')
		plus = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@act='plus']")))
		for x in range(0, 3):
			plus.click()
		down = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@act='wy_down']")))
		for x in range(0, 3):
			down.click()
		item_attr = tryon_item_img.get_attribute("style")
		before = self.parse_item_attributes(item_attr)
		save_config = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "saveConfig")), 'Timed Out')
		save_config.click()

		self.webdriver.refresh()
		tryon_pic_after = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shichuantpl_id4693")), 'Timed Out')
		tryon_pic_after.click()
		tryon_item_after = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid578")), 'Timed Out')
		tryon_item_after.click()	
		tryon_item_img_after = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp578")), 'Timed Out')
		item_attr_after = tryon_item_img_after.get_attribute("style")
		after = self.parse_item_attributes(item_attr_after)
		result = self.compare_item_attributes(before, after)
		return result

	def show_dropdown(self):
		self.choose_tryon_items()
		tryon_item2_img = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp42")), 'Timed Out')
		tryon_item2_img.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "myDropdown42")), 'Timed Out')
			return True
		except TimeoutException:
			return False		

	def delete_tryon_item_from_dropdown(self):
		self.choose_tryon_items()
		tryon_item2_img = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp42")), 'Timed Out')
		tryon_item2_img.click()
		dropdown = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "myDropdown42")), 'Timed Out')
		dropdown.find_element_by_css_selector("a:nth-child(1)").click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.invisibility_of_element_located((By.ID, "tryimgtmp42")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def move_item_to_top_from_dropdown(self):
		self.choose_tryon_items()
		tryon_item1_img = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp577")), 'Timed Out')
		tryon_item1_img.click()
		dropdown = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "myDropdown577")), 'Timed Out')
		dropdown.find_element_by_css_selector("a:nth-child(2)").click()
		timeout = time.time()+5
		while True:
			if self.webdriver.find_element_by_css_selector("div.img_box>div:nth-last-child(1)").get_attribute("id") == "tryimgtmp577":
				return True
			elif time.time()>timeout:
				return False

	def move_item_to_bottom_from_dropdown(self):
		self.choose_tryon_items()
		tryon_item2_img = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "tryimgtmp42")), 'Timed Out')
		tryon_item2_img.click()
		dropdown = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "myDropdown42")), 'Timed Out')
		dropdown.find_element_by_css_selector("a:nth-child(3)").click()
		timeout = time.time()+5
		while True:
			if self.webdriver.find_element_by_css_selector("div.img_box > div:nth-child(2)").get_attribute("id") == "tryimgtmp42":
				return True
			elif time.time()>timeout:
				return False

	def save_settings_without_signin(self):
		save_config = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "saveConfig")), 'Timed Out')
		save_config.click()
		try:
			WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.login_xpath)), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def upload_photo_without_signin(self):
		upload = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Upload')]")), 'Timed Out')
		upload.click()
		try:
			WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.login_xpath)), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def take_snapshot_without_signin(self):
		snapshot = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "fa-camera")), 'Timed Out')
		snapshot.click()
		try:
			WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.login_xpath)), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def switch_to_hand(self):
		hand = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, '//label[@for="hand"]')), 'Timed Out')
		hand.click()
		try:
			WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//img[@src='/templates/default/images/TRY-ON/left1.PNG']")), 'Timed Out')
			return self.webdriver.current_url == self.base_url+'modules/index.php?pkg=tryon&contr=tryon&tryontype=hand'
		except TimeoutException:
			return False

	def switch_back_to_face_from_hand(self):
		self.switch_to_hand()
		face = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, '//label[@for="face"]')), 'Timed Out')
		face.click()
		try:
			WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//img[@src='/public/js/takephoto/images/outline.png']")), 'Timed Out')
			return self.webdriver.current_url == self.base_url+'modules/index.php?pkg=tryon&contr=tryon'
		except TimeoutException:
			return False

	def delete_tryon_item_from_current(self):
		self.choose_tryon_items()
		curr_item = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, 'cur_item_577')), 'Timed Out')
		ActionChains(self.webdriver).move_to_element(curr_item).perform()

		remove_btn = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#cur_item_577>a')), 'Timed Out')
		remove_btn.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.invisibility_of_element_located((By.ID, "tryimgtmp577")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def choose_tryon_item_without_photo(self):
		tryonitem = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, 'trypicimg577')), 'Timed Out')
		tryonitem.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, self.require_tryon_pic_xpath)), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def save_settings_without_tryon_items(self):
		self.choose_tryon_pic()
		save_config = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "saveConfig")), 'Timed Out')
		save_config.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, self.require_tryon_item_xpath)), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def quick_view(self):
		element = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid577")), 'Timed Out')
		hov = ActionChains(self.webdriver).move_to_element(element)
		hov.perform()
		quick_view = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Quick View')]")), 'Timed Out')
		quick_view.click()
		try:
			WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Brown Chiffon Pullover Tank')]")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def save_tryon(self):
		self.choose_tryon_items()
		self.webdriver.find_element_by_xpath("//button[contains(text(),'Save For Review')]").click()
		WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#tryon_results>.try-results")), 'Timed Out')
		self.webdriver.find_elements_by_class_name("fitting-results")[1].click()
		save = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bottom-btn>a:nth-child(1)")), 'Timed Out')
		save.click()
		WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "iframe")), 'Timed Out')
		self.webdriver.switch_to_frame(self.webdriver.find_element_by_tag_name("iframe"))
		album = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "i963")), 'Timed Out')
		album.click()
		done = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "DONE")), 'Timed Out')
		done.click()
		self.webdriver.switch_to_default_content()
		try:			
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'The operation completed successfully!')]")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def tutorial(self):
		tutorial = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, 'cd-tour-trigger')), 'Timed Out')
		tutorial.click()
		WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Step Number 1')]")), 'Timed Out')
		next = self.webdriver.find_elements_by_class_name("cd-next")
		next[0].click()
		WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Step Number 2')]")), 'Timed Out')
		next[1].click()
		WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Step Number 3')]")), 'Timed Out')
		next[2].click()
		WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Adjustment Tools')]")), 'Timed Out')
		next[3].click()
		WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Current Items')]")), 'Timed Out')
		self.webdriver.find_elements_by_class_name("cd-close")[4].click()
		try:			
			WebDriverWait(self.webdriver, 5).until(EC.invisibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Current Items')]")), 'Timed Out')
			return True
		except TimeoutException:
			return False

