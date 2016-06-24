'''
Created on Fri Jun 10 2016 15:54:10 GMT-0700 (PDT)

@author:Judy Yang
'''
from wtframework.wtf.web.page import PageObject, InvalidPageError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from wtframework.wtf.web.webdriver import WTF_CONFIG_READER
from wtframework.wtf.config import WTF_TIMEOUT_MANAGER
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class SignInPage(PageObject):
    '''
    SignInPage
    WTFramework PageObject representing a page like:
    http://ec2-52-9-175-55.us-west-1.compute.amazonaws.com/signin.php
    '''


    ### Page Elements Section ###
    username = lambda self:self.webdriver.find_element_by_id("username")
    password = lambda self:self.webdriver.find_element_by_id("password")
    signinBtn = lambda self:self.webdriver.find_element_by_css_selector("input[class='sub'][value='Sign In']")

    email = lambda self:self.webdriver.find_element_by_name("email")
    userpass = lambda self:self.webdriver.find_element_by_name("userpass")
    userpass1 = lambda self:self.webdriver.find_element_by_name("userpass1")
    signupBtn = lambda self:self.webdriver.find_element_by_css_selector("input[class='sub'][value='Sign Up']")

    forgot = lambda self:self.webdriver.find_element_by_link_text("Forgot Password?")
    ### End Page Elements Section ###

    base_url = WTF_CONFIG_READER.get("baseurl")
    signin_url = base_url+'signin.php'
    forget_url = base_url+'signin1.php'
    signup_message = "You have successfully registered your emReal account. We sent an email to confirm your email address.\nPlease login your email account to complete it."
    blank_password_message = "Please enter the password"
    incorrect_password_message = "Incorrect username or password!"
    existing_email_message = "The email address you entered is already in use."
    bad_email_message = "The mailbox is not in the correct format!"

    def _validate_page(self, webdriver):
        '''
        Validates we are on the correct page.
        '''

        if not 'http://ec2-52-9-175-55.us-west-1.compute.amazonaws.com/signin.php' in webdriver.current_url:
            raise InvalidPageError("This page did not pass SignInPage page validation.")

    '''def goto_signin(self):
        self.webdriver.get(self.base_url+'index-1.php')'''

            
    def signin(self, username, password):
        self.webdriver.get(self.signin_url)
        self.username().send_keys(username)
        self.password().send_keys(password)
        self.signinBtn().click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        return self.base_url+'SHARE.php' in self.webdriver.current_url

    def signin_with_blank_password(self,username):
        self.webdriver.get(self.signin_url)
        self.username().send_keys(username)
        self.signinBtn().click()

        try:
            WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == self.blank_password_message

    def signin_with_incorrect_password(self, username, password):
        self.webdriver.get(self.signin_url)
        self.username().send_keys(username)
        self.password().send_keys(password)
        self.signinBtn().click()

        try:
            WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == self.incorrect_password_message

    def signup(self, email, password):
        self.webdriver.get(self.signin_url)
        self.email().send_keys(email)
        self.userpass().send_keys(password)
        self.userpass1().send_keys(password)
        self.signupBtn().click()

        try:
            WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()
        condition1 = alert_text == self.signup_message
        condition2 = self.base_url+'My.php' in self.webdriver.current_url
        
        return condition1 and condition2

    def signup_with_unmatching_passwords(self, email, password, password1):
        self.webdriver.get(self.signin_url)
        self.email().send_keys(email)
        self.userpass().send_keys(password)
        self.userpass1().send_keys(password1)

        error_message = "Password input don't match"

        error = len(self.webdriver.find_elements_by_xpath("//span[contains(text(), \""+error_message+"\")]"))

        return error

    def signup_with_existing_username(self, email, password):
        self.webdriver.get(self.signin_url)
        self.email().send_keys(email)
        self.userpass().click()

        try:
            WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()
        return alert_text == self.existing_email_message

    def signup_with_short_password(self, email, password):
        self.webdriver.get(self.signin_url)
        self.email().send_keys(email)
        self.userpass().send_keys(password)
        self.userpass1().click()

        error = len(self.webdriver.find_elements_by_xpath("//span[contains(text(), 'Password need to be 6 digits at least.')]"))

        return error

    def goto_reset_password(self):
        self.webdriver.get(self.signin_url)
        self.forgot().click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        return self.webdriver.current_url == self.forget_url

    def reset_password(self, email):
        self.webdriver.get(self.forget_url)
        self.webdriver.find_element_by_id("email").send_keys(email)
        self.webdriver.find_element_by_css_selector("input[class='sub']").click()
        reset_message = len(self.webdriver.find_elements_by_xpath("//span[contains(text(), 'Email has been sent to you. Please follow it to reset your password')]"))
        return reset_message

    def reset_password_with_bad_email(self, email):
        self.webdriver.get(self.forget_url)
        self.webdriver.find_element_by_id("email").send_keys(email)
        self.webdriver.find_element_by_css_selector("input[class='sub']").click()

        try:
            WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == self.bad_email_message

    def reset_password_with_nonexistent_email(self, email):
        self.webdriver.get(self.forget_url)
        self.webdriver.find_element_by_id("email").send_keys(email)
        self.webdriver.find_element_by_css_selector("input[class='sub']").click()
        reset_message = len(self.webdriver.find_elements_by_xpath("//span[contains(text(), 'Email has been sent to you. Please follow it to reset your password')]"))
        return reset_message

    def signout(self):
        self.signin("aaa@gmail.com", "123456")

        hoverItem = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "signoutlinkaccount")))
        ActionChains(self.webdriver).move_to_element(hoverItem).perform()

        signoutBtn = WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign Out")))
        signoutBtn.click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.webdriver.current_url == self.base_url+'index-1.php'

    def signin_test(self):
        #test1 = self.goto_signin()
        test2 = self.signin("aaa@gmail.com", "123456")
        test3 = self.signin_with_blank_password("aaa@gmail.com")
        test4 = self.signin_with_incorrect_password("aaa@gmail.com", "654321")
        test5 = self.signup("c@gmail.com", "123456")
        test6 = self.signup_with_unmatching_passwords("bc@gmail.com", "123456", "654321")
        test7 = self.signup_with_existing_username("aaa@gmail.com", "123456")
        test8 = self.signup_with_short_password("bcd@gmail.com", "1234")
        test9 = self.goto_reset_password()
        test10 = self.reset_password("c@gmail.com")
        test11 = self.reset_password_with_bad_email("test123")
        test12 = self.reset_password_with_nonexistent_email("xyz@gmail.com")
        '''test13 = self.goto_reset_password_from_email()
        test14 = self.reset_password_with_unmatching_passwords()
        test15 = self.reset_password_with_matching_passwords()'''
        test16 = self.signout()
        f = open("debug_signin.txt", "w")
        f.write("signin"+str(test2)+str(test3)+str(test4)+str(test5)+str(test6)+str(test7)+str(test8)+str(test9)+str(test10)+str(test11)+str(test12)+str(test16))
        return test2 and test3 and test4 and test5 and test6 and test7 and test8 and test9 and test10 and test11 and test12 and test16        