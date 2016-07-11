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
import string

class EmShare(PageObject):
    '''
    EmShare
    WTFramework PageObject representing a page like:
    https://qa.emfitting.com/SHARE.php
    '''


    ### Page Elements Section ###
    ### End Page Elements Section ###
    base_url = WTF_CONFIG_READER.get("baseurl")
    emShare_url = base_url+'SHARE.php'

    def _validate_page(self, webdriver):
        '''
        Validates we are on the correct page.
        '''

        if not self.base_url+'SHARE.php' in webdriver.current_url:
            raise InvalidPageError("This page did not pass EmShare page validation.")

    def become_member(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Become a Member")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Become a Member").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "username")), 'Timed Out')
            self.webdriver.find_element_by_id("username").send_keys("aaa@gmail.com")
            self.webdriver.find_element_by_id("password").send_keys("123456"+Keys.RETURN)
        except TimeoutException:
            return False
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.emShare_url in self.webdriver.current_url  

    def view_all_members(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "View All Members")), 'Timed Out')
            self.webdriver.find_element_by_link_text("View All Members").click()
        except TimeoutException:
            return False
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'emSHARE2.php' == self.webdriver.current_url

    def search_for_member(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "sosuo1")), 'Timed Out')
            self.webdriver.find_element_by_class_name("sosuo1").send_keys("abc@yahoo.com"+Keys.RETURN)
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'abc@yahoo.com')]")), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def add_friend_after_search(self):
        self.webdriver.find_element_by_css_selector("a[href*='addfriend.php?id=144']").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == "The user is your friend!"

    def show_invite_popup(self):
        self.webdriver.get(self.base_url+'emSHARE2.php')
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "butimg")), 'Timed Out')
            self.webdriver.find_element_by_class_name("butimg").click()
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//li[contains(text(), 'Invite Your Friends to emShare')]")), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def invite_friends(self):
        email_spaces = self.webdriver.find_elements_by_class_name("ed")
        email_spaces[0].send_keys("123@test.com")
        email_spaces[1].send_keys("jyang@emreal-corp.com")
        self.webdriver.find_element_by_xpath("//input[@value='Send']").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False
        if alert_text != "Message Sent OK!":
            return False
        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == "Message Sent OK!"

    def add_friend(self):
        self.webdriver.get(self.base_url+'emSHARE2.php')
        randomnum = random.randrange(0, 20)
        members = self.webdriver.find_elements_by_class_name("listltul")
        members[randomnum].find_element_by_css_selector("li:nth-child(2)>a").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == "Added successfully!" or alert_text == "The user is your friend!"

    def next_page_friends(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Next")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Next").click()
        except TimeoutException:
            return False

        return self.base_url+'emSHARE2.php?page=2' == self.webdriver.current_url

    def goto_me(self):
        self.webdriver.get(self.emShare_url)
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Go to My Page")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Go to My Page").click()
        except TimeoutException:
            return False
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'My.php' == self.webdriver.current_url

    def add_friend_from_new_members(self):
        self.webdriver.get(self.emShare_url)
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "liaddfriend")), 'Timed Out')
            members = self.webdriver.find_elements_by_class_name("liaddfriend")
        except TimeoutException:
            return False

        randomnum = random.randrange(0, 6)
        members[randomnum].find_element_by_css_selector("a").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == "Added successfully!" or alert_text == "The user is your friend!"

    def goto_detail_of_latest_sharing(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "lf2li")), 'Timed Out')
            self.webdriver.find_element_by_class_name("lf2li").click()
        except TimeoutException:
            return False        
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'Reply.php?sharid=' in self.webdriver.current_url

    def add_comment_to_latest_sharing(self):
        randomstring = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "textarea")), 'Timed Out')
            self.webdriver.find_element_by_id("textarea").send_keys("test comment "+randomstring)
            self.webdriver.find_element_by_class_name("sub").click()
        except TimeoutException:
            return False
        WTF_TIMEOUT_MANAGER.brief_pause()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'test comment "+randomstring+"')]")), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def goto_detail_page_from_reply_button(self):
        self.webdriver.get(self.emShare_url)
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Reply")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Reply").click()
        except TimeoutException:
            return False

        return self.base_url+'Reply.php?sharid=' in self.webdriver.current_url

    def next_page_share(self):
        self.webdriver.get(self.emShare_url)
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Next")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Next").click()
        except TimeoutException:
            return False

        return self.base_url+'SHARE.php?page=2' == self.webdriver.current_url  

    def goto_page(self):
        self.webdriver.get(self.emShare_url)
        self.webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        pages = self.webdriver.find_elements_by_class_name("num")
        numpages = len(pages)
        randomnum = random.randrange(0, numpages)
        page_url = pages[randomnum].get_attribute("href")
        pages[randomnum].click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.webdriver.current_url == page_url

             
    def emShare_test(self):
        f = open("debug_emShare.txt", "w")
        test1 = self.become_member()
        f.write("test1: "+str(test1))
        test2 = self.view_all_members()
        f.write("\ntest2: "+str(test2))
        test3 = self.search_for_member()
        f.write("\ntest3: "+str(test3))
        test4 = self.add_friend_after_search()
        f.write("\ntest4: "+str(test4))
        test5 = self.show_invite_popup()
        f.write("\ntest5: "+str(test5))
        test6 = self.invite_friends()
        f.write("\ntest6: "+str(test6))
        test7 = self.add_friend()
        f.write("\ntest7: "+str(test7))
        test8 = self.next_page_friends()
        f.write("\ntest8: "+str(test8))
        test9 = self.goto_me()
        f.write("\ntest9: "+str(test9))
        test10 = self.add_friend_from_new_members()
        f.write("\ntest10: "+str(test10))
        test12 = self.goto_detail_of_latest_sharing()
        f.write("\ntest12: "+str(test12))
        test13 = self.add_comment_to_latest_sharing()
        f.write("\ntest13: "+str(test13))
        test14 = self.goto_detail_page_from_reply_button()
        f.write("\ntest14: "+str(test14))
        test15 = self.next_page_share()
        f.write("\ntest15: "+str(test15))
        test16 = self.goto_page()
        f.write("\ntest16: "+str(test16))
        return test1 and test2 and test3 and test4 and test5 and test6 and test7 and test8 and test9 and test10 and test12 and test13 and test14 and test15 and test16
