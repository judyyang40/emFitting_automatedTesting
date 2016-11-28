from wtframework.wtf.web.page import PageObject, InvalidPageError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from wtframework.wtf.web.webdriver import WTF_CONFIG_READER
from wtframework.wtf.config import WTF_TIMEOUT_MANAGER
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class SignInPage(PageObject):
	base_url = WTF_CONFIG_READER.get("baseurl")
	invalid_xpath = "//p[contains(text(), 'Invalid email address or password')]"
	used_xpath = "//p[contains(text(), 'Email address already in use')]"
	reset_xpath = "//div[contains(text(), 'A secured link has been sent to your email. Please follow the link to reset your password.')]"

	def _validate_page(self, webdriver):
		if not self.base_url+'modules/index.php?pkg=account&contr=account' in webdriver.current_url:
			raise InvalidPageError("This page did not pass page validation.")

	def signin(self):
		email = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "form-email")), 'Timed Out')
		email.send_keys("test@emreal-corp.com")
		self.webdriver.find_element_by_id("form-password1").send_keys("123456"+Keys.RETURN)
		WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "index-tryon")), 'Timed Out')
		return self.base_url+'modules/index.php?pkg=main&contr=main' == self.webdriver.current_url

	def signin_with_incorrect_password(self):
		email = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "form-email")), 'Timed Out')
		email.send_keys("test@emreal-corp.com")
		self.webdriver.find_element_by_id("form-password1").send_keys("654321"+Keys.RETURN)
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, self.invalid_xpath)), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def signup(self):
		dname = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "form-display-name")), 'Timed Out')
		dname.send_keys("Test Person")
		self.webdriver.find_element_by_id("form-email2").send_keys("test_signup@emreal-corp.com")
		self.webdriver.find_element_by_id("form-password2").send_keys("123456")
		self.webdriver.find_element_by_id("agreement").click();
		self.webdriver.find_element_by_id("confirm-form-password").send_keys("123456"+Keys.RETURN)
		return self.base_url+'modules/index.php?pkg=main&contr=main' == self.webdriver.current_url

	def signup_with_bad_email(self):
		dname = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "form-display-name")), 'Timed Out')
		dname.send_keys("Test Person")
		self.webdriver.find_element_by_id("form-email2").send_keys("test")
		self.webdriver.find_element_by_id("form-password2").send_keys("123456")
		self.webdriver.find_element_by_id("confirm-form-password").send_keys("123456")
		return not self.webdriver.find_element_by_id("signup-btn").is_enabled()

	def signup_with_unmatching_passwords(self):
		dname = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "form-display-name")), 'Timed Out')
		dname.send_keys("Test Person")
		self.webdriver.find_element_by_id("form-email2").send_keys("test@emreal-corp.com")
		self.webdriver.find_element_by_id("form-password2").send_keys("123456")
		self.webdriver.find_element_by_id("confirm-form-password").send_keys("654321")
		WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "has-error")), 'Timed Out')
		return not self.webdriver.find_element_by_id("signup-btn").is_enabled()

	def signup_with_existing_email(self):
		dname = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "form-display-name")), 'Timed Out')
		dname.send_keys("Test Person")
		self.webdriver.find_element_by_id("form-email2").send_keys("test@emreal-corp.com")
		self.webdriver.find_element_by_id("form-password2").send_keys("123456")
		self.webdriver.find_element_by_id("agreement").click();
		self.webdriver.find_element_by_id("confirm-form-password").send_keys("123456"+Keys.RETURN)
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, self.used_xpath)), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def signup_with_short_password(self):
		dname = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "form-display-name")), 'Timed Out')
		dname.send_keys("Test Person")
		self.webdriver.find_element_by_id("form-email2").send_keys("test@emreal-corp.com")
		self.webdriver.find_element_by_id("form-password2").send_keys("12345")
		self.webdriver.find_element_by_id("confirm-form-password").send_keys("12345")
		return not self.webdriver.find_element_by_id("signup-btn").is_enabled()

	def forgot_password(self):
		forgot = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "forgot-pw")), 'Timed Out')
		forgot.click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "forgot-pw")), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def send_reset_password_email(self):
		self.forgot_password()
		email = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "forgot-pw-email")), 'Timed Out')
		email.send_keys("test@emreal-corp.com")
		self.webdriver.find_element_by_id("forgot-btn").click()
		try:
			WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, self.reset_xpath)), 'Timed Out')
			return True
		except TimeoutException:
			return False

	def send_reset_password_email_with_bad_email(self):
		self.forgot_password()
		email = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "forgot-pw-email")), 'Timed Out')
		email.send_keys("test")
		return not self.webdriver.find_element_by_id("forgot-btn").is_enabled()



