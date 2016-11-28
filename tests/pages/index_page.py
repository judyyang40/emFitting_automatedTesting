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


class IndexPage(PageObject):
	base_url = WTF_CONFIG_READER.get("baseurl")

	def _validate_page(self, webdriver):
		if not self.base_url+'modules/index.php?pkg=main&contr=main' in webdriver.current_url:
			raise InvalidPageError("This page did not pass page validation.")

	def goto_signin_from_emshare(self):
		signin_emshare = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Sign in')]")), 'Timed Out')
		signin_emshare.click()
		return self.base_url+'modules/index.php?pkg=account&contr=account' == self.webdriver.current_url

	def goto_signin(self):
		signin = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign Up / Login")), 'Timed Out')
		signin.click()
		return self.base_url+'modules/index.php?pkg=account&contr=account' == self.webdriver.current_url
	
	def no_signin_link_after_signin(self):
		try:
			WebDriverWait(self.webdriver, 10).until(EC.invisibility_of_element_located((By.LINK_TEXT, "Sign Up / Login")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def click_home_logo(self):
		home = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-brand>img")), 'Timed Out')
		home.click()
		return self.base_url+'modules/index.php?pkg=main&contr=main' == self.webdriver.current_url

	def search_in_navigation_bar(self):
		search = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "keyword")), 'Timed Out')
		search.send_keys("blue"+Keys.RETURN);
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src='/uploads/image/20160908/1473379424.png']")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def goto_home(self):
		home = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")), 'Timed Out')
		home.click()
		return self.base_url+'modules/index.php?pkg=main&contr=main' == self.webdriver.current_url

	def goto_tryon(self):
		tryon = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Try-On")), 'Timed Out')
		tryon.click()
		return self.base_url+'modules/index.php?pkg=tryon&contr=tryon' == self.webdriver.current_url

	def goto_shop(self):
		shop = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Shop")), 'Timed Out')
		shop.click()
		return self.base_url+'modules/index.php?pkg=shop&contr=shop' == self.webdriver.current_url

	def goto_emshare(self):
		emshare = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "emShare")), 'Timed Out')
		emshare.click()
		return self.base_url+'modules/index.php?pkg=emshare&contr=emshare' == self.webdriver.current_url

	def goto_me(self):
		me = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#navbar>ul>li>a>img.avatar")), 'Timed Out')
		me.click()
		return self.base_url+'modules/index.php?pkg=my&contr=my' == self.webdriver.current_url

	def goto_shopping_cart(self):
		bag = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "fa-shopping-bag")), 'Timed Out')
		bag.click()
		return self.base_url+'modules/index.php?pkg=shop&contr=shop&event=shoppingcart' == self.webdriver.current_url

	def goto_face_tryon(self):
		face = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "index-tryon")), 'Timed Out')
		face.find_element_by_css_selector(".row>.col-md-6:nth-child(1)").click()
		return self.base_url+'modules/index.php?pkg=tryon&contr=tryon' == self.webdriver.current_url

	def goto_hand_tryon(self):
		hand = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "index-tryon")), 'Timed Out')
		hand.find_element_by_css_selector(".row>.col-md-6:nth-child(2)").click()
		return self.base_url+'modules/index.php?pkg=tryon&contr=tryon&tryontype=hand' == self.webdriver.current_url

	def goto_soho_shop(self):
		soho = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src='/uploads/image/20151015/1444859633.jpg']")), 'Timed Out')
		soho.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src='/uploads/image/20160616/1466116988.png']")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def goto_glasses_category(self):
		WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "category-link")), 'Timed Out')
		self.webdriver.execute_script("window.scrollTo(0, 500);")
		self.webdriver.find_elements_by_class_name("category-link")[3].click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src='/uploads/image/20160816/1471396304.png']")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def click_product_in_shop(self):
		shop_item = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "content")), 'Timed Out')
		shop_item.click()
		return self.base_url+'modules/index.php?pkg=shop&contr=shop&event=productdetails&id=' in self.webdriver.current_url

	def goto_amazon(self):
		soho = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src='/uploads/image/20160816/1471393508.jpg']")), 'Timed Out')
		soho.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[src='/uploads/image/20160815/1471299799.png']")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def profile_pic_in_emshare(self):
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "welcome-avatar")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def goto_me_from_emshare(self):
		my = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "emshare-mypage")), 'Timed Out')
		my.click()
		return self.base_url+'modules/index.php?pkg=my&contr=my' == self.webdriver.current_url

	def goto_emshare(self):
		emshare = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'emShare')]")), 'Timed Out')
		emshare.click()
		return self.base_url+'modules/index.php?pkg=emshare&contr=emshare' == self.webdriver.current_url

	def view_demo(self):
		demo = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "demo-link")), 'Timed Out')
		demo.click()
		return 'https://www.youtube.com' in self.webdriver.current_url