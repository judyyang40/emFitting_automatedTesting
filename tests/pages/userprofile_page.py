'''
Created on Fri Jun 24 2016 16:41:55 GMT-0700 (PDT)

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
from selenium.webdriver.support.ui import Select
import random
import string

class UserProfile(PageObject):
    '''
    UserProfile
    WTFramework PageObject representing a page like:
    https://qa.emfitting.com/My.php
    '''


    ### Page Elements Section ###
    ### End Page Elements Section ###
    base_url = WTF_CONFIG_READER.get("baseurl")
    profile_url = base_url+'My.php'

    def _validate_page(self, webdriver):
        '''
        Validates we are on the correct page.
        '''

        if not self.base_url+'My.php' in webdriver.current_url:
            raise InvalidPageError("This page did not pass UserProfile page validation.")

    def goto_me(self):
        self.webdriver.get(self.base_url+'index-1.php')
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "t1img")), 'Timed Out')
            self.webdriver.find_element_by_class_name("t1img").click()
        except TimeoutException:
            return False
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.profile_url in self.webdriver.current_url

    def goto_edit_profile(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Edit Profile")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Edit Profile").click()
        except TimeoutException:
            return False
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'editshare.php' in self.webdriver.current_url

    def reset_password(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "pass")), 'Timed Out')
        except TimeoutException:
            return False
        self.webdriver.find_element_by_id("pass").send_keys("123456")
        self.webdriver.find_element_by_id("pass1").send_keys("654321")
        self.webdriver.find_element_by_id("pass2").send_keys("654321")
        self.webdriver.find_element_by_xpath("//input[@value='Done']").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False

        if alert_text != "Successful modification!":
            return False

        self.webdriver.get(self.base_url+'signin.php')
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "username")), 'Timed Out')
            self.webdriver.find_element_by_name("username").send_keys("aaa@gmail.com")
            self.webdriver.find_element_by_name("password").send_keys("654321"+Keys.RETURN)
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()
        if self.base_url+'SHARE.php' not in self.webdriver.current_url:
            return False

        self.webdriver.get(self.base_url+'editshare.php?id=194')
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "pass")), 'Timed Out')
        except TimeoutException:
            return False
        self.webdriver.find_element_by_id("pass").send_keys("654321")
        self.webdriver.find_element_by_id("pass1").send_keys("123456")
        self.webdriver.find_element_by_id("pass2").send_keys("123456")
        self.webdriver.find_element_by_xpath("//input[@value='Done']").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False   

        return alert_text == "Successful modification!"   

    def modify_horoscope(self):
        self.webdriver.get(self.base_url+'editshare.php?id=194')
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "s2")), 'Timed Out')
            horoscope = self.webdriver.find_element_by_name("s2")
        except TimeoutException:
            return False

        randomnum = random.randrange(1, 13)
        #horoscope_text = horoscope.find_element_by_css_selector('option:nth-child('+str(randomnum+1)+')').get_attribute("value")
        horoscope_select = Select(horoscope)
        horoscope_select.select_by_index(randomnum)
        horoscope_text = horoscope_select.first_selected_option.text
        self.webdriver.find_element_by_xpath("//input[@value='Done']").click()

        try:
            WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        if alert_text != "Successful modification!":
            return False

        self.webdriver.get(self.base_url+'editshare.php?id=194')
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "s2")), 'Timed Out')
            horoscope2 = self.webdriver.find_element_by_name("s2")
        except TimeoutException:
            return False

        horoscope_select2 = Select(horoscope2)
        horoscope_text2 = horoscope_select2.first_selected_option.text
        return horoscope_text == horoscope_text2

    def modify_display_name(self):
        randomnum = random.randrange(0, 100)
        display_name_text = "display name "+str(randomnum)
        display_name = self.webdriver.find_element_by_name("nicheng")
        display_name.clear()
        WTF_TIMEOUT_MANAGER.brief_pause()
        display_name.send_keys(display_name_text)
        self.webdriver.find_element_by_xpath("//input[@value='Done']").click()

        try:
            WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        if alert_text != "Successful modification!":
            return False

        self.webdriver.get(self.base_url+'editshare.php?id=194')
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "nicheng")), 'Timed Out')
            display_name_text2 = self.webdriver.find_element_by_name("nicheng").get_attribute("value")
        except TimeoutException:
            return False
        return display_name_text == display_name_text2

    def modify_gender(self):
        gender = self.webdriver.find_element_by_name("s1")
        gender_select = Select(gender)
        before_text = gender_select.first_selected_option.text
        if before_text == "male":
            expected = "female"
            gender_select.select_by_index(2)
        else:
            expected = "male"
            gender_select.select_by_index(1)
        self.webdriver.find_element_by_xpath("//input[@value='Done']").click()
        try:
            WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        if alert_text != "Successful modification!":
            return False

        self.webdriver.get(self.base_url+'editshare.php?id=194')
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "s1")), 'Timed Out')
            gender2 = self.webdriver.find_element_by_name("s1")
        except TimeoutException:
            return False

        gender_select2 = Select(gender2)
        gender_text = gender_select2.first_selected_option.text
        return gender_text == expected

    def modify_birthday(self):
        pass

    def add_album(self):
        self.webdriver.get(self.profile_url)
        self.webdriver.find_element_by_link_text("Edit Profile").click()

        before = (len(self.webdriver.find_elements_by_css_selector("#gundiv2 > ul >li")))/2

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "But1")), 'Timed Out')
            self.webdriver.find_element_by_id("But1").click()
        except TimeoutException:
            return False

        randomstring = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "newalbum")), 'Timed Out')
            self.webdriver.find_element_by_name("newalbum").send_keys("Album"+randomstring)
            self.webdriver.find_element_by_name("albumdecs").send_keys("New Album description")
        except TimeoutException:
            return False

        self.webdriver.find_element_by_css_selector("div#tck > form > div > input.sub").click()

        try:
            WebDriverWait(self.webdriver, 5).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()
        after = (len(self.webdriver.find_elements_by_css_selector("#gundiv2 > ul >li")))/2

        return alert_text == "Successful!" and before+1 == after

    def delete_album(self):
        pass

    def add_video_collection(self):
        self.webdriver.get(self.profile_url)
        self.webdriver.find_element_by_link_text("Edit Profile").click()

        before = (len(self.webdriver.find_elements_by_css_selector("#gundivn3 > ul >li")))/2
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "But2")), 'Timed Out')
            self.webdriver.find_element_by_id("But2").click()
        except TimeoutException:
            return False

        randomstring = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "videoname")), 'Timed Out')
            self.webdriver.find_element_by_id("videoname").send_keys("Video"+randomstring)
        except TimeoutException:
            return False

        self.webdriver.find_element_by_css_selector("div#tck2 > form > div > input.sub").click()

        try:
            WebDriverWait(self.webdriver, 5).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()
        after = (len(self.webdriver.find_elements_by_css_selector("#gundivn3 > ul >li")))/2

        return alert_text == "Successful!" and before+1 == after

    def delete_video_collection(self):
        before = (len(self.webdriver.find_elements_by_css_selector("#gundivn3 > ul >li")))/2
        self.webdriver.find_element_by_css_selector("#gundivn3>ul>li:nth-child(1)>a:nth-child(2)").click()
        try:
            WebDriverWait(self.webdriver, 5).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()
        after = (len(self.webdriver.find_elements_by_css_selector("#gundivn3 > ul >li")))/2

        return alert_text == "Successful!" and before == after+1

    def add_friends_from_me(self):
        self.webdriver.get(self.base_url+'My.php?id=194')
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Add Friends")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Add Friends").click()
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()
        return self.base_url+'emSHARE2.php' == self.webdriver.current_url

    def show_invite_friends_popup(self):
        self.webdriver.get(self.base_url+'My.php?id=194')
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Invite New Members")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Invite New Members").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Invite New Members")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Invite New Members").click()
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
        self.webdriver.find_element_by_id("email_con").send_keys("invite friends email content")
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

    def goto_product_detail_in_wishlist(self):
        self.webdriver.get(self.base_url+'My.php?id=194')
        self.webdriver.find_element_by_css_selector("div#gundiv.container2 > ul > li > a").click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        return self.base_url+'goodsshow.php' in self.webdriver.current_url 

    def click_photo_in_collection(self):
        #self.webdriver.get(self.base_url+'My.php?id=194')
        pass

    def goto_album_detail(self):
        pass

    def goto_runway_detail(self):
        self.webdriver.get(self.base_url+'My.php?id=194')
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#gundiv4>ul>li>a")), 'Timed Out')
            self.webdriver.find_element_by_css_selector("#gundiv4>ul>li>a").click()
        except TimeoutException:
            return False
        WTF_TIMEOUT_MANAGER.brief_pause()
        return self.base_url+'video.php' in self.webdriver.current_url

    def next_page_me(self):
        self.webdriver.get(self.base_url+'My.php?id=194')
        self.webdriver.find_element_by_class_name("last").click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        return self.base_url+'My.php?id=194&page=2' == self.webdriver.current_url

    def previous_page_me(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "home")), 'Timed Out')
            self.webdriver.find_element_by_class_name("home").click()
        except TimeoutException:
            return False
        return self.base_url+'My.php?id=194&page=1' == self.webdriver.current_url

    def userprofile_test(self):
        f = open("debug_me.txt", "w")
        test1 = self.goto_me()
        f.write("test1: "+str(test1))
        test2 = self.goto_edit_profile()
        f.write("\ntest2: "+str(test2))
        test7 = self.reset_password()
        f.write("\ntest7: "+str(test7))
        test8 = self.modify_horoscope()
        f.write("\ntest8: "+str(test8))
        test9 = self.modify_display_name()
        f.write("\ntest9: "+str(test9))
        test10 = self.modify_gender()
        f.write("\ntest10: "+str(test10))
        '''test11 = self.modify_birthday()
        f.write("\ntest11: "+str(test11))
        test12 = self.modify_location()
        f.write("\ntest12: "+str(test12))'''
        '''test13 = self.modify_pro_expertise()
        f.write("\ntest13: "+str(test13))
        test14 = self.modify_pro_highest_education()
        f.write("\ntest14: "+str(test14))
        test15 = self.modify_pro_profession()
        f.write("\ntest15: "+str(test15))
        test16 = self.modify_pro_email()
        f.write("\ntest16: "+str(test16))
        test17 = self.modify_pro_location()
        f.write("\ntest17: "+str(test17))
        test18 = self.modify_pro_phone_address()
        f.write("\ntest18: "+str(test18))'''
        test21 = self.add_album()
        f.write("\ntest21: "+str(test21))
        #test22 = self.delete_album()
        #f.write("\ntest22: "+str(test22))
        test25 = self.add_video_collection()
        f.write("\ntest25: "+str(test25))
        test26 = self.delete_video_collection()
        f.write("\ntest26: "+str(test26))

        test29 = self.add_friends_from_me()
        f.write("\ntest29: "+str(test29))
        test30 = self.show_invite_friends_popup()
        f.write("\ntest30: "+str(test30))
        test31 = self.invite_friends()
        f.write("\ntest31: "+str(test31))
        test32 = self.goto_product_detail_in_wishlist()
        f.write("\ntest32: "+str(test32))
        #test33 = self.click_photo_in_collection()
        #f.write("\ntest33: "+str(test33))
        #test34 = self.goto_album_detail()
        #f.write("\ntest34: "+str(test34))
        #test35 = self.click_photo_in_album()
        #f.write("\ntest35: "+str(test35))
        test37 = self.goto_runway_detail()
        f.write("\ntest37: "+str(test37))
        #test38 = self.click_photo_in_runway()
        #f.write("\ntest38: "+str(test38))
        test40 = self.next_page_me()
        f.write("\ntest40: "+str(test40))
        test41 = self.previous_page_me()
        f.write("\ntest41: "+str(test41))
        return test1 and test2 and test7 and test8 and test9 and test10 and test21 and test25 and test26 and test29 and test30 and test31 and test32 and test37 and test40 and test41
