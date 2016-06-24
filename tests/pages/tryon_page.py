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
import random

class TryOnPage(PageObject):
    '''
    TryOnPage
    WTFramework PageObject representing a page like:
    http://ec2-52-9-175-55.us-west-1.compute.amazonaws.com/tryon.php?tryontype=face
    '''


    ### Page Elements Section ###
    ### End Page Elements Section ###
    base_url = WTF_CONFIG_READER.get("baseurl")
    tryon_url = base_url+'tryon.php?tryontype=face'
    item1css = ".img_box>#tryimgtmp505"
    item2css = ".img_box>#tryimgtmp373"
    item3css = ".img_box>#tryimgtmp108"

    def _validate_page(self, webdriver):
        '''
        Validates we are on the correct page.
        '''

        if not 'http://ec2-52-9-175-55.us-west-1.compute.amazonaws.com/tryon.php?tryontype=face' in webdriver.current_url:
            raise InvalidPageError("This page did not pass TryOnPage page validation.")

    def choose_tryon_items(self):
        self.choose_randomtryonpic()
        num = self.choose_randomtryonpic()+1
        self.webdriver.find_element_by_css_selector('#listtext_url>li:nth-child('+str(num)+')>a').click()
        #tryonpic = self.webdriver.find_element_by_css_selector('#listtext_url>li:nth-child('+str(num)+')>a')
        #self.webdriver.execute_script("arguments[0].click();", tryonpic)

        self.webdriver.find_element_by_class_name("trypicid505").click()
        self.webdriver.find_element_by_class_name("trypicid373").click()
        self.webdriver.find_element_by_class_name("trypicid108").click()
        
    def assert_choose_tryon_items(self):
        self.choose_tryon_items()
        item1 = len(self.webdriver.find_elements_by_css_selector(self.item1css))
        item2 = len(self.webdriver.find_elements_by_css_selector(self.item2css))
        item3 = len(self.webdriver.find_elements_by_css_selector(self.item3css))
        return item1 and item2 and item3

    def undo(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryon_items()
        self.webdriver.find_element_by_id("Undo").click()
        item1 = len(self.webdriver.find_elements_by_css_selector(self.item1css))
        item2 = len(self.webdriver.find_elements_by_css_selector(self.item2css))
        item3 = len(self.webdriver.find_elements_by_css_selector(self.item3css))
        return item1 and item2 and not item3

    def clear(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryon_items()
        self.webdriver.find_element_by_id("Clear").click()
        item1 = len(self.webdriver.find_elements_by_css_selector(self.item1css))
        item2 = len(self.webdriver.find_elements_by_css_selector(self.item2css))
        item3 = len(self.webdriver.find_elements_by_css_selector(self.item3css))
        return not item1 and not item2 and not item3

    def save_settings(self):
        self.webdriver.get(self.tryon_url)
        self.choose_randomtryonpic()
        num = self.choose_randomtryonpic()+1
        self.webdriver.find_element_by_css_selector('#listtext_url>li:nth-child('+str(num)+')>a').click()

        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_class_name("trypicid505").click()
        self.webdriver.find_element_by_class_name("trypicid373").click()
        self.webdriver.find_element_by_class_name("trypicid108").click()

        down = self.webdriver.find_element_by_xpath("//a[@act='wy_down']/img")
        down.click()
        down.click()
        down.click()
        style_attribute_before = self.webdriver.find_element_by_css_selector(self.item3css).get_attribute("style")

        self.webdriver.find_element_by_id("saveConfig").click()
        self.webdriver.refresh()
        
        #choose same tryonpic and items
        self.webdriver.implicitly_wait(3)
        arrow = self.webdriver.find_element_by_xpath(".//*[@id='photolistwrap']/a[4]")
        shichuantpl = self.webdriver.find_elements_by_class_name("shichuantpl")
        while 1:
            #self.webdriver.implicitly_wait(3)
            #if shichuantpl[num-1].is_displayed():
            tryonpicID = "shichuantpl_id"+str(shichuantpl[num-1].get_attribute("id"))
            if self.isClickable(tryonpicID):
                shichuantpl[num-1].click()
                break
            else:
                arrow.click()

        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_class_name("trypicid505").click()
        self.webdriver.find_element_by_class_name("trypicid373").click()
        self.webdriver.find_element_by_class_name("trypicid108").click()

        style_attribute_after = self.webdriver.find_element_by_css_selector(self.item3css).get_attribute("style")

        #parse style attribute before save
        before = style_attribute_before.split('; ')
        before_dic = {}
        for attribute in before:
            if attribute.startswith('width'):
                before_dic['width'] = float(attribute[7:-2])
            elif attribute.startswith('height'):
                before_dic['height'] = float(attribute[8:-2])
            elif attribute.startswith('top'):
                before_dic['top'] = float(attribute[5:-2])
            elif attribute.startswith('left'):
                before_dic['left'] = float(attribute[6:-2])

        #parse style attribute after save
        after = style_attribute_after.split('; ')
        after_dic = {}
        for attribute in after:
            if attribute.startswith('width'):
                after_dic['width'] = float(attribute[7:-2])
            elif attribute.startswith('height'):
                after_dic['height'] = float(attribute[8:-2])
            elif attribute.startswith('top'):
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

    def save(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryon_items()
        self.webdriver.find_element_by_id("savebtn").click()

        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.TAG_NAME, "iframe")), 'Timed Out')
            self.webdriver.switch_to_frame(self.webdriver.find_element_by_tag_name("iframe"))
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_id("DONE").click()

        return True

    def share_twitter(self):
        self.webdriver.get(self.tryon_url)
        #currentwindows = self.webdriver.window_handles # set of windows already open
        sharebuttonCSS = ".tryon-sharebutton"
        self.choose_tryon_items()
        self.webdriver.find_element_by_id("saveShareTryPhoto").click()

        browser = WTF_CONFIG_READER.get("selenium.browser")

        if browser == "FIREFOX":
            currentwindows = self.webdriver.window_handles # set of windows already open
            try:
                WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, sharebuttonCSS)), 'Timed Out')
                buttons = self.webdriver.find_elements_by_css_selector(sharebuttonCSS)
                buttons[1].click()
            except TimeoutException:
                return False

            newwindows = self.webdriver.window_handles # 1 extra window shows up here.
            newwindow = list(set(newwindows) - set(currentwindows))[0]
            self.webdriver.switch_to_window(newwindow)
            text = self.webdriver.find_element_by_id("status").get_attribute("value")

            self.webdriver.switch_to_window(currentwindows[0])
            WTF_TIMEOUT_MANAGER.brief_pause()

        elif browser == "CHROME":
            mainwindow = self.webdriver.current_window_handle
            try:
                WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, sharebuttonCSS)), 'Timed Out')
                buttons = self.webdriver.find_elements_by_css_selector(sharebuttonCSS)
                buttons[1].click()
            except TimeoutException:
                return False
            WTF_TIMEOUT_MANAGER.brief_pause()
            self.webdriver.switch_to_window(self.webdriver.window_handles[1])
            text = self.webdriver.find_element_by_id("status").get_attribute("value")
            self.webdriver.close()
            self.webdriver.switch_to_window(mainwindow)
            WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'/uploads/image/' in text

        '''try:
            WebDriverWait(self.webdriver, 10).until(
                lambda driver: self.webdriver.execute_script("return jQuery.active == 0")
            )
            WTF_TIMEOUT_MANAGER.short_pause()
            twitter = self.webdriver.find_element_by_css_selector(".tryon-sharebutton")
            self.webdriver.execute_script("arguments[0].click();", twitter)
            WTF_TIMEOUT_MANAGER.long_pause()
        finally:
            self.webdriver.quit()
        return True'''

    def goto_productpage(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryon_items()
        WTF_TIMEOUT_MANAGER.brief_pause()
        self.webdriver.find_element_by_css_selector("div.tck1.goodsinfo_108 > a > button.btn_buttom_box").click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        return self.base_url+'goodsshow.php' in self.webdriver.current_url

    def add_to_shopping_cart(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryon_items()
        self.webdriver.find_element_by_css_selector(".buttom.goodsinfo_108 > a.addcart").click()

        try:
            WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        self.webdriver.find_element_by_id("CartLink").click()

        title = self.webdriver.find_element_by_class_name("title").text

        condition1 = alert_text == "Join a shopping cart to succeed!"
        condition2 = title == "Brown Lady Hat"

        return condition1 and condition2

    def add_to_wish_list(self):
        self.webdriver.get(self.tryon_url)
        self.choose_tryon_items()
        WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".buttom.goodsinfo_108 > a.addwish")), 'Timed Out')
        self.webdriver.find_element_by_css_selector(".buttom.goodsinfo_108 > a.addwish").click()

        try:
            WebDriverWait(self.webdriver, 5).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        condition1 = alert_text == "Collect success!"
        condition2 = alert_text == "Pro, you have to collect the goods!"

        return condition1 or condition2

    '''def delete_tryonpic(self):
        self.webdriver.get(self.tryon_url)
        before = len(self.webdriver.find_elements_by_class_name("shichuantpl"))

        num = self.choose_randomtryonpic()+1
        deleteCSS = '#listtext_url>li:nth-child('+str(num)+')>span:nth-child(2)>a>img'
        element = self.webdriver.find_element_by_css_selector(deleteCSS)
        self.webdriver.execute_script("arguments[0].click();", element)
        WTF_TIMEOUT_MANAGER.brief_pause()

        self.webdriver.find_element_by_link_text("Confirm").click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        after = len(self.webdriver.find_elements_by_class_name("shichuantpl"))

        return (before-1) == after'''


    '''def upload_tryonpic(self):
        self.webdriver.find_element_by_link_text("Upload a Photo").click()
        self.webdriver.switch_to_frame(self.webdriver.find_element_by_tag_name("iframe"))
        self.webdriver.find_element_by_css_selector("div#uploadify.uploadify").click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        return True


    def take_snapshot(self):
        before = len(self.webdriver.find_elements_by_class_name("shichuantpl"))
        self.webdriver.find_element_by_link_text("Take a Snapshot").click()
        self.webdriver.switch_to_frame(self.webdriver.find_element_by_tag_name("iframe"))
        self.webdriver.find_element_by_id("btn_shoot").click()
        WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "btn_upload")))
        self.webdriver.find_element_by_id("btn_upload").click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        after = len(self.webdriver.find_elements_by_class_name("shichuantpl"))
        return (before+1) == after'''

    def choose_randomtryonpic(self):
        #returns random shichuantpl number
        shichuantpl = self.webdriver.find_elements_by_class_name("shichuantpl")
        num = len(shichuantpl)
        randomnum = random.randrange(0, num)
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, ".//*[@id='photolistwrap']/a[4]")), 'Timed Out')
            arrow = self.webdriver.find_element_by_xpath(".//*[@id='photolistwrap']/a[4]")
        except TimeoutException:
            return False

        while 1:
            #self.webdriver.implicitly_wait(3)
            #if shichuantpl[randomnum].is_displayed():
            tryonpicID = "shichuantpl_id"+str(shichuantpl[randomnum].get_attribute("id"))
            if self.isClickable(tryonpicID):
                #shichuantpl[randomnum].click()
                return randomnum
            else:
                arrow.click()
        return False

    def isClickable(self, tryonpicID):
        try:
            WebDriverWait(self.webdriver, 3).until(EC.element_to_be_clickable((By.CLASS_NAME, tryonpicID)), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def tryon_test(self):
        f = open("debug_tryon.txt", "w")
        test1 = self.assert_choose_tryon_items()
        f.write(str(test1))
        test2 = self.undo()
        f.write(str(test2))
        test3 = self.clear()
        f.write(str(test3))
        test4 = self.save_settings()
        f.write(str(test4))
        test5 = self.save()
        f.write(str(test5))
        test7 = self.goto_productpage()
        f.write(str(test7))
        test8 = self.add_to_shopping_cart()
        f.write(str(test8))
        test9 = self.add_to_wish_list()
        f.write(str(test9))
        test6 = self.share_twitter()
        f.write(str(test6))
        #test10 = self.delete_tryonpic()
        #test11 = self.upload_tryonpic()
        #test12 = self.take_snapshot()

        f.write("tryon"+str(test1)+str(test2)+str(test3)+str(test4)+str(test5)+str(test6)+str(test7)+str(test8)+str(test9))
        return test1 and test2 and test3 and test4 and test5 and test6 and test7 and test8 and test9
