'''
Created on Fri Jun 10 2016 17:08:35 GMT-0700 (PDT)

@author:Judy Yang
'''
from wtframework.wtf.web.page import PageObject, InvalidPageError
from wtframework.wtf.web.webdriver import WTF_CONFIG_READER
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from wtframework.wtf.config import WTF_TIMEOUT_MANAGER
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random

class TryOnPage(PageObject):
    '''
    TryOnPage
    WTFramework PageObject representing a page like:
    https://qa.emfitting.com/tryonindex.php
    '''


    ### Page Elements Section ###
    ### End Page Elements Section ###
    base_url = WTF_CONFIG_READER.get("baseurl")
    tryon_url = base_url+'tryon.php?tryontype=face'
    item1css = ".img_box>#tryimgtmp571"
    item2css = ".img_box>#tryimgtmp560"
    item3css = ".img_box>#tryimgtmp108"

    item1style = {}
    item1style['width'] = float(409.534)
    item1style['top'] = float(265.492)
    item1style['left'] = float(39.2012)
    item1style['height'] = float(518.886)
    item2style = {}
    item2style['width'] = float(108.179)
    item2style['top'] = float(255.241)
    item2style['left'] = float(188.9)
    item2style['height'] = float(89.0068)
    item3style = {}
    item3style['width'] = float(193.176)
    item3style['top'] = float(46.0972)
    item3style['left'] = float(147.38)
    item3style['height'] = float(111.761)

    require_signin_xpath = "//div[contains(text(), 'You need to sign in before using this function.')]"

    def _validate_page(self, webdriver):
        '''
        Validates we are on the correct page.
        '''

        if not self.base_url+'tryonindex.php' in webdriver.current_url:
            raise InvalidPageError("This page did not pass TryOnPage page validation.")

    def choose_tryonpic_and_items(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shichuantpl_id3581")), 'Timed Out')
            self.webdriver.find_element_by_class_name("shichuantpl_id3581").click()
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid571")), 'Timed Out')
            self.webdriver.find_element_by_class_name("trypicid571").click()
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid560")), 'Timed Out')
            self.webdriver.find_element_by_class_name("trypicid560").click()
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid108")), 'Timed Out')
            self.webdriver.find_element_by_class_name("trypicid108").click()
        except TimeoutException:
            return False

    def choose_tryonpic_and_items_logged_in(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shichuantpl_id3805")), 'Timed Out')
            self.webdriver.find_element_by_class_name("shichuantpl_id3805").click()
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid571")), 'Timed Out')
            self.webdriver.find_element_by_class_name("trypicid571").click()
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid560")), 'Timed Out')
            self.webdriver.find_element_by_class_name("trypicid560").click()
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid108")), 'Timed Out')
            self.webdriver.find_element_by_class_name("trypicid108").click()
        except TimeoutException:
            return False

    def goto_facetryon(self):
        self.webdriver.find_element_by_class_name("aRen").click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        return self.webdriver.current_url == self.tryon_url

    def choose_tryonpic(self):
        self.webdriver.get(self.tryon_url)
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "shichuantpl_id3581")), 'Timed Out')
            self.webdriver.find_element_by_class_name("shichuantpl_id3581").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.img_box > img.phone")), 'Timed Out')
            tryonpic = len(self.webdriver.find_elements_by_css_selector("div.img_box > img.phone"))
        except TimeoutException:
            return False

        return tryonpic   

    def choose_tryonitems(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items()
        WTF_TIMEOUT_MANAGER.brief_pause()

        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.item1css)), 'Timed Out')
            style1 = self.webdriver.find_element_by_css_selector(self.item1css).get_attribute("style")
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.item2css)), 'Timed Out')
            style2 = self.webdriver.find_element_by_css_selector(self.item2css).get_attribute("style")
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.item3css)), 'Timed Out')
            style3 = self.webdriver.find_element_by_css_selector(self.item3css).get_attribute("style")
        except TimeoutException:
            return False

        style1_array = style1.split('; ')
        style1_dic = {}
        for attribute in style1_array:
            if attribute.startswith('width'):
                style1_dic['width'] = float(attribute[7:-2])
            elif attribute.startswith('height'):
                style1_dic['height'] = float(attribute[8:-2])
            elif attribute.startswith('top'):
                style1_dic['top'] = float(attribute[5:-3])
            elif attribute.startswith('left'):
                style1_dic['left'] = float(attribute[6:-2])
        flag1 = 1
        for key in style1_dic:
            b = style1_dic[key]
            a = self.item1style[key]
            if(abs(a - b) > 2):
                flag1 = 0
                break
        style2_array = style2.split('; ')
        style2_dic = {}
        for attribute in style2_array:
            if attribute.startswith('width'):
                style2_dic['width'] = float(attribute[7:-2])
            elif attribute.startswith('height'):
                style2_dic['height'] = float(attribute[8:-2])
            elif attribute.startswith('top'):
                style2_dic['top'] = float(attribute[5:-3])
            elif attribute.startswith('left'):
                style2_dic['left'] = float(attribute[6:-2])
        flag2 = 1
        for key in style2_dic:
            b = style2_dic[key]
            a = self.item2style[key]
            if(abs(a - b) > 2):
                flag2 = 0
                break
        style3_array = style3.split('; ')
        style3_dic = {}
        for attribute in style3_array:
            if attribute.startswith('width'):
                style3_dic['width'] = float(attribute[7:-2])
            elif attribute.startswith('height'):
                style3_dic['height'] = float(attribute[8:-2])
            elif attribute.startswith('top'):
                style3_dic['top'] = float(attribute[5:-3])
            elif attribute.startswith('left'):
                style3_dic['left'] = float(attribute[6:-2])
        flag3 = 1
        for key in style3_dic:
            b = style3_dic[key]
            a = self.item3style[key]
            if(abs(a - b) > 2):
                flag3 = 0
                break
        #f = open("debug.txt", "w")
        #f.write(str(style1_dic)+"\n"+str(style2_dic)+"\n"+str(style3_dic))

        return flag1 and flag2 and flag3

    def drag_item_to_adjust_position(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items()
        WTF_TIMEOUT_MANAGER.brief_pause()
        hat = self.webdriver.find_element_by_css_selector(".img_box>#tryimgtmp108")
        chain = ActionChains(self.webdriver)
        chain.move_to_element_with_offset(hat, 20, 20)
        chain.click_and_hold()
        chain.move_by_offset(200, 200)
        chain.release()
        chain.perform()
        style3 = self.webdriver.find_element_by_css_selector(self.item3css).get_attribute("style")
        style3_array = style3.split('; ')
        style3_dic = {}
        for attribute in style3_array:
            if attribute.startswith('top'):
                style3_dic['top'] = float(attribute[5:-3])
            elif attribute.startswith('left'):
                style3_dic['left'] = float(attribute[6:-2])

        #f = open("debug_drag.txt", "w")
        #f.write(str(style3_dic['left'])+" "+str(style3_dic['top']))

        if (abs(style3_dic['left'] - 347) < 2) and (abs(style3_dic['top'] - 246) < 2):
            return True
        else:
            return False


    def upload_tryonpic_without_login(self):
        self.webdriver.get(self.tryon_url)
        self.webdriver.find_element_by_link_text("Upload a Photo").click()
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.require_signin_xpath)), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def take_snapshot_without_login(self):
        self.webdriver.get(self.tryon_url)
        self.webdriver.find_element_by_link_text("Take a Snapshot").click()
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.require_signin_xpath)), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def save_settings_without_login(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_link_text("Save Settings").click()
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.require_signin_xpath)), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def enlarge_photo_without_login(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_link_text("Enlarge").click()
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.require_signin_xpath)), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def save_tryon_without_login(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_id("savebtn").click()
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.require_signin_xpath)), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def share_tryon_without_login(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_id("saveShareTryPhoto").click()
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, self.require_signin_xpath)), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def login(self):
        self.webdriver.find_element_by_link_text("Sign in").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "username")), 'Timed Out')
        except TimeoutException:
            return False
        self.webdriver.find_element_by_id("username").send_keys("aaa@gmail.com")
        self.webdriver.find_element_by_id("password").send_keys("123456"+Keys.RETURN)
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'SHARE.php' in self.webdriver.current_url

    def undo(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_id("Undo").click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        item1 = len(self.webdriver.find_elements_by_css_selector(self.item1css))
        item2 = len(self.webdriver.find_elements_by_css_selector(self.item2css))
        item3 = len(self.webdriver.find_elements_by_css_selector(self.item3css))
        return item1 and item2 and not item3

    def clear(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_id("Clear").click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        item1 = len(self.webdriver.find_elements_by_css_selector(self.item1css))
        item2 = len(self.webdriver.find_elements_by_css_selector(self.item2css))
        item3 = len(self.webdriver.find_elements_by_css_selector(self.item3css))
        return not item1 and not item2 and not item3    

    def save_position_settings(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()
        down = self.webdriver.find_element_by_xpath("//a[@act='wy_down']/img")
        down.click()
        down.click()
        down.click()
        style_attribute_before = self.webdriver.find_element_by_css_selector(self.item3css).get_attribute("style")

        self.webdriver.find_element_by_id("saveConfig").click()
        self.webdriver.refresh()

        WTF_TIMEOUT_MANAGER.brief_pause()
        self.choose_tryonpic_and_items_logged_in()
        style_attribute_after = self.webdriver.find_element_by_css_selector(self.item3css).get_attribute("style")

        #parse style attribute before save
        before = style_attribute_before.split('; ')
        before_dic = {}
        for attribute in before:
            if attribute.startswith('top'):
                before_dic['top'] = float(attribute[5:-2])
            elif attribute.startswith('left'):
                before_dic['left'] = float(attribute[6:-2])

        #parse style attribute after save
        after = style_attribute_after.split('; ')
        after_dic = {}
        for attribute in after:
            if attribute.startswith('top'):
                after_dic['top'] = float(attribute[5:-3])
            elif attribute.startswith('left'):
                after_dic['left'] = float(attribute[6:-2])

        #compare attribute values before and after save
        flag = 1
        for key in before_dic:
            b = before_dic[key]
            a = after_dic[key]
            if(abs(a - b) > 2):
                flag = 0
                break
        return flag

    def save_ratio_settings(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()
        plus = self.webdriver.find_element_by_xpath("//a[@act='plus']/img")
        plus.click()
        plus.click()
        plus.click()
        style_attribute_before = self.webdriver.find_element_by_css_selector(self.item3css).get_attribute("style")

        self.webdriver.find_element_by_id("saveConfig").click()
        self.webdriver.refresh()

        WTF_TIMEOUT_MANAGER.brief_pause()
        self.choose_tryonpic_and_items_logged_in()
        style_attribute_after = self.webdriver.find_element_by_css_selector(self.item3css).get_attribute("style")

        #parse style attribute before save
        before = style_attribute_before.split('; ')
        before_dic = {}
        for attribute in before:
            if attribute.startswith('width'):
                before_dic['width'] = float(attribute[7:-2])
            elif attribute.startswith('height'):
                before_dic['height'] = float(attribute[8:-2])

        #parse style attribute after save
        after = style_attribute_after.split('; ')
        after_dic = {}
        for attribute in after:
            if attribute.startswith('width'):
                after_dic['width'] = float(attribute[7:-2])
            elif attribute.startswith('height'):
                after_dic['height'] = float(attribute[8:-2])

        f = open("debug.txt", "w")
        f.write(str(before_dic)+"\n")
        f.write(str(after_dic))

        #compare attribute values before and after save
        flag = 1
        for key in before_dic:
            b = before_dic[key]
            a = after_dic[key]
            if(abs(a - b) > 2):
                flag = 0
                break
        return flag

    def enlarge(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()

        self.webdriver.find_element_by_link_text("Enlarge").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#my_popup>img#big_view_pic")), 'Timed Out')
            big_pic = self.webdriver.find_element_by_css_selector("div#my_popup>img#big_view_pic")
        except TimeoutException:
            return False

        src = big_pic.get_attribute("src")

        return 'http://qa.emfitting.com//uploads/image/' in src

    def save_tryon(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()

        before_id = self.webdriver.find_element_by_class_name("showimg11").get_attribute("src")

        self.webdriver.find_element_by_id("savebtn").click()
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, "iframe")), 'Timed Out')
            self.webdriver.switch_to_frame(self.webdriver.find_element_by_tag_name("iframe"))
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.ID, "DONE")), 'Timed Out')
            self.webdriver.find_element_by_id("DONE").click()
        except TimeoutException:
            return False

        self.webdriver.switch_to_default_content()
        WTF_TIMEOUT_MANAGER.brief_pause()
        after_id = self.webdriver.find_element_by_class_name("showimg11").get_attribute("src")

        return before_id != after_id

    def share_tryon(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()

        main_window = self.webdriver.current_window_handle

        self.webdriver.find_element_by_id("saveShareTryPhoto").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tryon-sharebutton")), 'Timed Out')
            buttons = self.webdriver.find_elements_by_css_selector(".tryon-sharebutton")
            buttons[1].click()
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()

        self.webdriver.switch_to_window(self.webdriver.window_handles[1])
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "status")), 'Timed Out')
            text = self.webdriver.find_element_by_id("status").get_attribute("value")
        except TimeoutException:
            return False

        self.webdriver.close()
        self.webdriver.switch_to_window(main_window)
        WTF_TIMEOUT_MANAGER.brief_pause()

        return 'http://qa.emfitting.com//uploads/image/' in text 

    def dropdown_list(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_css_selector(self.item3css).click()
        try:
            WebDriverWait(self.webdriver, 3).until(EC.visibility_of_element_located((By.ID, "myDropdown108")), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def delete_tryonitem_from_dropdown_list(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_css_selector(self.item3css).click()

        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.ID, "myDropdown108")), 'Timed Out')
            self.webdriver.find_element_by_css_selector("div#myDropdown108>a:nth-child(2)").click()
        except TimeoutException:
            return False

        item1 = len(self.webdriver.find_elements_by_css_selector(self.item1css))
        item2 = len(self.webdriver.find_elements_by_css_selector(self.item2css))
        item3 = len(self.webdriver.find_elements_by_css_selector(self.item3css))
        return item1 and item2 and not item3

    def move_tryonitem_to_top_layer_from_dropdown_list(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_css_selector(self.item2css).click()

        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.ID, "myDropdown560")), 'Timed Out')
            self.webdriver.find_element_by_css_selector("div#myDropdown560>a:nth-child(3)").click()
        except TimeoutException:
            return False
        
        WTF_TIMEOUT_MANAGER.brief_pause()
        tryonpicid = self.webdriver.find_element_by_css_selector("div.img_box > div:nth-last-child(1)").get_attribute("id")

        return tryonpicid == "tryimgtmp560"

    def move_tryonitem_to_back_from_dropdown_list(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_css_selector(self.item3css).click()

        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.ID, "myDropdown108")), 'Timed Out')
            self.webdriver.find_element_by_css_selector("div#myDropdown108>a:nth-child(4)").click()
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()
        tryonpicid = self.webdriver.find_element_by_css_selector("div.img_box > div:nth-child(2)").get_attribute("id")

        return tryonpicid == "tryimgtmp108"

    def filter_tryonitems_by_gender(self):
        self.webdriver.get(self.tryon_url)
        self.webdriver.find_element_by_id("male").click()
        #male clothes visible, female clothes not visible
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid255")), 'Timed Out')
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicid571")), 'Timed Out')
        except TimeoutException:
            return True
        return False

    def add_to_cart(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_css_selector(".buttom.goodsinfo_108 > a.addcart").click()

        try:
            WebDriverWait(self.webdriver, 20).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False

        self.webdriver.find_element_by_css_selector("li.accountlink>a").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "title")), 'Timed Out')
            titles = self.webdriver.find_elements_by_class_name("title")
        except TimeoutException:
            return False

        condition2 = False
        for t in titles:
            if t.text == "Brown Lady Hat":
                condition2 = True
                break

        condition1 = alert_text == "Join a shopping cart to succeed!"

        return condition1 and condition2 

    def add_to_wishlist(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryonpic_and_items_logged_in()
        WTF_TIMEOUT_MANAGER.brief_pause() 
        self.webdriver.find_element_by_css_selector(".buttom.goodsinfo_108 > a.addwish").click()

        try:
            WebDriverWait(self.webdriver, 20).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False

        condition1 = alert_text == "Collect success!"
        condition2 = alert_text == "Pro, you have to collect the goods!"

        return condition1 or condition2

    def delete_tryon_result(self):
        self.webdriver.get(self.tryon_url)
        self.webdriver.find_element_by_css_selector("ul#Results_box>li>a:nth-child(3)").click()
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Are you sure you want to delete the photos?')]")), 'Timed Out')
        except TimeoutException:
            return False
        self.webdriver.find_element_by_link_text("Confirm").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'The operation completed successfully!')]")), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def share_tryon_result(self):
        self.webdriver.get(self.tryon_url)
        main_window = self.webdriver.current_window_handle
        self.webdriver.find_element_by_css_selector("ul#Results_box>li>a:nth-child(4)").click()
        #facebook
        self.webdriver.find_element_by_css_selector("ul#Results_box>li>div.share_box>a:nth-child(1)").click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        self.webdriver.switch_to_window(self.webdriver.window_handles[1])
        url = self.webdriver.current_url
        self.webdriver.close()
        self.webdriver.switch_to_window(main_window)
        WTF_TIMEOUT_MANAGER.brief_pause()

        return 'https://www.facebook.com/login.php' in url

    def goto_brand_list(self):
        self.webdriver.get(self.tryon_url)
        self.webdriver.find_element_by_css_selector("ul.brand>li>a:nth-child(1)").click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.webdriver.current_url == self.base_url+'goodslist.php?bid=11'

    def tryon_test(self):
        f = open("debug_tryon.txt", "w")
        test1 = self.goto_facetryon()
        f.write("test1: "+str(test1))
        test2 = self.choose_tryonpic()
        f.write("\ntest2: "+str(test2))
        test3 = self.choose_tryonitems()
        f.write("\ntest3: "+str(test3))
        test4 = self.drag_item_to_adjust_position()
        f.write("\ntest4: "+str(test4))
        test5 = self.upload_tryonpic_without_login()
        f.write("\ntest5: "+str(test5))
        test6 = self.take_snapshot_without_login()
        f.write("\ntest6: "+str(test6))
        test7 = self.save_settings_without_login()
        f.write("\ntest7: "+str(test7))
        test8 = self.enlarge_photo_without_login()
        f.write("\ntest8: "+str(test8))
        test9 = self.save_tryon_without_login()
        f.write("\ntest9: "+str(test9))
        test10 = self.share_tryon_without_login()
        f.write("\ntest10: "+str(test10))
        test11 = self.login()
        f.write("\ntest11: "+str(test11))
        test16 = self.undo()
        f.write("\ntest16: "+str(test16))
        test17 = self.clear()
        f.write("\ntest17: "+str(test17))
        test18 = self.save_position_settings()
        f.write("\ntest18: "+str(test18))
        #test19 = self.save_ratio_settings()
        #f.write("\ntest19: "+str(test19))
        test20 = self.enlarge()
        f.write("\ntest20: "+str(test20))
        test21 = self.save_tryon()
        f.write("\ntest21: "+str(test21))
        test22 = self.share_tryon()
        f.write("\ntest22: "+str(test22))
        test23 = self.dropdown_list()
        f.write("\ntest23: "+str(test23))
        test24 = self.delete_tryonitem_from_dropdown_list()
        f.write("\ntest24: "+str(test24))
        test25 = self.move_tryonitem_to_top_layer_from_dropdown_list()
        f.write("\ntest25: "+str(test25))
        test26 = self.move_tryonitem_to_back_from_dropdown_list()
        f.write("\ntest26: "+str(test26))
        test27 = self.filter_tryonitems_by_gender()
        f.write("\ntest27: "+str(test27))
        test28 = self.add_to_cart()
        f.write("\ntest28: "+str(test28))
        test29 = self.add_to_wishlist()
        f.write("\ntest29: "+str(test29))
        test30 = self.delete_tryon_result()
        f.write("\ntest30: "+str(test30))
        test31 = self.share_tryon_result()
        f.write("\ntest31: "+str(test31))
        test32 = self.goto_brand_list()
        f.write("\ntest32: "+str(test32))

        return test1 and test2 and test3 and test4 and test5 and test6 and test7 and test8 and test9 and test10 and test11 and test16 and test17 and test18 and test20 and test21 and test22 and test23 and test24 and test25 and test26 and test27 and test28 and test29 and test30 and test31 and test32

        '''test5 = self.upload_tryonpic_without_login()
        f.write("\ntest5: "+str(test5))
        test11 = self.login()
        f.write("\ntest11: "+str(test11))
        test25 = self.move_tryonitem_to_top_layer_from_dropdown_list()
        f.write("\ntest25: "+str(test25))

        return test5 and test11 and test25'''
