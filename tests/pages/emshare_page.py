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
import random
import string


class EmSharePage(PageObject):
	base_url = WTF_CONFIG_READER.get("baseurl")

	def _validate_page(self, webdriver):
		if not self.base_url+'modules/index.php?pkg=emshare&contr=emshare' in webdriver.current_url:
			raise InvalidPageError("This page did not pass page validation.")

	def post_without_signin(self):
		share = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Share')]")), 'Timed Out')
		share.click()
		WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
		alert = self.webdriver.switch_to_alert()
		alert_text = alert.text
		alert.accept()
		return alert_text == 'Please sign in to share!'

	def goto_signup_from_emshare_without_signin(self):
		signup = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Sign Up/Sign In')]")), 'Timed Out')
		signup.click()
		timeout = time.time()+5
		while True:
			if self.webdriver.current_url == self.base_url+'modules/index.php?pkg=account&contr=account':
				return True
			elif time.time()>timeout:
				return False

	def goto_my_page_from_emshare_without_signin(self):
		my = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go to My Page')]")), 'Timed Out')
		my.click()
		timeout = time.time()+5
		while True:
			if self.webdriver.current_url == self.base_url+'modules/index.php?pkg=account&contr=account':
				return True
			elif time.time()>timeout:
				return False

	def comment_without_signin(self):
		WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "form-horizontal")), 'Timed Out')
		form = self.webdriver.find_elements_by_class_name("form-horizontal")[2]
		box = form.find_element_by_class_name("form-control")
		box.send_keys("")
		form.find_element_by_css_selector("div>button").click()
		WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
		alert = self.webdriver.switch_to_alert()
		alert_text = alert.text
		alert.accept()
		return alert_text == 'Please sign in to comment!'

	def post_text_sharing(self):
		randomstring = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
		box = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "textarea")), 'Timed Out')
		box.send_keys('test post '+randomstring)
		self.webdriver.find_element_by_xpath("//button[contains(text(),'Share')]").click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'test post "+randomstring+"')]")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def comment(self):
		randomstring = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
		WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "form-horizontal")), 'Timed Out')
		form = self.webdriver.find_elements_by_class_name("form-horizontal")[2]
		box = form.find_element_by_class_name("form-control")
		box.send_keys('test comment '+randomstring)
		form.find_element_by_css_selector("div>button").click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'test comment "+randomstring+"')]")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	'''def invite_friends(self):
		invite = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "invite")), 'Timed Out')
		invite.click()
		WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "InputName2")), 'Timed Out')
		names = self.webdriver.find_elements_by_id("InputName2")
		names[0].send_keys("Judy1")
		names[1].send_keys("Judy2")
		emails = self.webdriver.find_elements_by_id("InputEmail2")
		emails[0].send_keys("judy0821.yang@gmail.com")
		emails[1].send_keys("jyang@emreal-corp.com")
		self.webdriver.find_element_by_xpath("//button[contains(text(),'Send invitation')]").click()'''

	def signup_from_emshare(self):
		signup = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Sign Up/Sign In')]")), 'Timed Out')
		signup.click()
		timeout = time.time()+5
		while True:
			if self.base_url+'modules/index.php?pkg=emshare&contr=emshare' in self.webdriver.current_url:
				return True
			elif time.time()>timeout:
				return False

	def goto_my_page_from_emshare(self):
		my = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Go to My Page')]")), 'Timed Out')
		my.click()
		timeout = time.time()+5
		while True:
			if self.base_url+'modules/index.php?pkg=my&contr=my' in self.webdriver.current_url:
				return True
			elif time.time()>timeout:
				return False
		
	def preview_youtube_video_before_posting(self):
		video = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "fname")), 'Timed Out')
		video.send_keys("https://www.youtube.com/watch?v=fk4BbF7B29w")
		preview = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "lblValue")), 'Timed Out')
		url = preview.get_attribute("src")
		return url == "https://www.youtube.com/embed/fk4BbF7B29w"

	def preview_vimeo_video_before_posting(self):
		video = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "fname")), 'Timed Out')
		video.send_keys("https://vimeo.com/23259282")
		preview = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "lblValue")), 'Timed Out')
		url = preview.get_attribute("src")
		return url == "https://player.vimeo.com/video/23259282"

	def post_sharing_with_youtube_url(self):
		video = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "fname")), 'Timed Out')
		video.send_keys("https://www.youtube.com/watch?v=60ItHLz5WEA")
		box = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "textarea")), 'Timed Out')
		box.send_keys('test youtube video post')
		self.webdriver.find_element_by_xpath("//button[contains(text(),'Share')]").click()
		show = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "show_video")), 'Timed Out')
		url = show.get_attribute("url")
		return 'https://www.youtube.com/watch?v=60ItHLz5WEA' == url

	def post_sharing_with_vimeo_url(self):
		video = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "fname")), 'Timed Out')
		video.send_keys("https://vimeo.com/17203320")
		box = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "textarea")), 'Timed Out')
		box.send_keys('test vimeo video post')
		self.webdriver.find_element_by_xpath("//button[contains(text(),'Share')]").click()
		show = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "show_video")), 'Timed Out')
		url = show.get_attribute("url")
		return 'https://vimeo.com/17203320' == url

	def post_empty_sharing(self):
		share = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Share')]")), 'Timed Out')
		share.click()
		WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
		alert = self.webdriver.switch_to_alert()
		alert_text = alert.text
		alert.accept()
		return alert_text == 'Your sharing cannot be empty.'

	def empty_comment(self):
		WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "form-horizontal")), 'Timed Out')
		form = self.webdriver.find_elements_by_class_name("form-horizontal")[2]
		box = form.find_element_by_class_name("form-control")
		box.send_keys("")
		form.find_element_by_css_selector("div>button").click()
		WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
		alert = self.webdriver.switch_to_alert()
		alert_text = alert.text
		alert.accept()
		return alert_text == 'Your comment cannot be empty.'