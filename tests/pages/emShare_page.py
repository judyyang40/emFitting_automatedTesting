'''
Created on Thu Jun 23 2016 15:39:19 GMT-0700 (PDT)

@author:Judy Yang
'''
from wtframework.wtf.web.page import PageObject, InvalidPageError
from wtframework.wtf.web.webdriver import WTF_CONFIG_READER
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from wtframework.wtf.config import WTF_TIMEOUT_MANAGER
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

class EmShare(PageObject):
    '''
    EmShare
    WTFramework PageObject representing a page like:
    http://ec2-52-9-175-55.us-west-1.compute.amazonaws.com/SHARE.php
    '''


    ### Page Elements Section ###
    ### End Page Elements Section ###
    base_url = WTF_CONFIG_READER.get("baseurl")
    emShare_url = base_url+'SHARE.php'

    def _validate_page(self, webdriver):
        '''
        Validates we are on the correct page.
        '''

        if not 'http://ec2-52-9-175-55.us-west-1.compute.amazonaws.com/SHARE.php' in webdriver.current_url:
            raise InvalidPageError("This page did not pass EmShare page validation.")

    def search_member_add_friend(self):
        self.webdriver.get(self.emShare_url)
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='emSHARE2.php']")), 'Timed Out')
            self.webdriver.find_element_by_xpath("//a[@href='emSHARE2.php']").click()
        except TimeoutException:
            return False
        #search for friend
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.sosuo1")), 'Timed Out')
            self.webdriver.find_element_by_css_selector("input.sosuo1").send_keys("abc@gmail.com" + Keys.RETURN)
        except TimeoutException:
            return False
        #add friend
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='addfriend.php?id=197']")), 'Timed Out')
            self.webdriver.find_element_by_css_selector("a[href*='addfriend.php']").click()
        except TimeoutException:
            return False
        #accept alert
        try:
            WebDriverWait(self.webdriver, 5).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == "Added successfully!" or alert_text == "The user is your friend!"

    '''def post_text_to_emShare(self):

    def view_sharing_and_comment(self):'''

    def navigate_to_specific_page(self):
        self.webdriver.get(self.emShare_url)
        self.webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        pages = self.webdriver.find_elements_by_class_name("num")
        numpages = len(pages)
        randomnum = random.randrange(0, numpages)
        f = open("emShare.txt", "w")
        f.write(str(numpages)+str(randomnum))
        page_url = pages[randomnum].get_attribute("href")
        pages[randomnum].click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        f.write(self.webdriver.current_url+'\n')
        f.write(self.emShare_url+page_url)

        return self.webdriver.current_url == self.emShare_url+page_url

    def emShare_test(self):
        #test1 = self.search_member_add_friend()
        test2 = self.navigate_to_specific_page()
        return test2

