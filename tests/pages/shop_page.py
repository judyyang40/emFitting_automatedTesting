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

class ShopPage(PageObject):
	base_url = WTF_CONFIG_READER.get("baseurl")

	def _validate_page(self, webdriver):
		if not self.base_url+'modules/index.php?pkg=shop&contr=shop' in webdriver.current_url:
			raise InvalidPageError("This page did not pass page validation.")

	def filter_brand_macy(self):
		brand = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "brandButton")), 'Timed Out')
		brand.click()
		macy = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Macys.com')]")), 'Timed Out')
		macy.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h6[contains(text(), 'Michael Kors MICHAEL Asymmetrical-Zip Walker Coat')]")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def filter_brand_macy_and_gender_male(self):
		self.filter_brand_macy()
		