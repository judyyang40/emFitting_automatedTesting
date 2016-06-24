'''
Created on Thu Jun 16 2016 16:57:13 GMT-0700 (PDT)

@author:Judy
'''
from wtframework.wtf.web.page import PageObject, InvalidPageError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from wtframework.wtf.web.webdriver import WTF_CONFIG_READER
from wtframework.wtf.config import WTF_TIMEOUT_MANAGER
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ShopPage(PageObject):
    '''
    ShopPage
    WTFramework PageObject representing a page like:
    http://ec2-52-9-175-55.us-west-1.compute.amazonaws.com/Shop.php
    '''


    ### Page Elements Section ###
    ### End Page Elements Section ###
    base_url = WTF_CONFIG_READER.get("baseurl")

    def _validate_page(self, webdriver):
        '''
        Validates we are on the correct page.
        '''

        if not 'http://ec2-52-9-175-55.us-west-1.compute.amazonaws.com/Shop.php' in webdriver.current_url:
            raise InvalidPageError("This page did not pass ShopPage page validation.")

    def goto_productpage(self):

        self.webdriver.find_element_by_css_selector("a[href*='tid=39']").click()

        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='tid=39&page=2']")), 'Timed Out')
            self.webdriver.find_element_by_css_selector("a[href*='tid=39&page=2']").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href*='tid=39&id=477']")), 'Timed Out')
            shirt = self.webdriver.find_element_by_css_selector("a[href*='tid=39&id=477']")
            shirt.find_element_by_css_selector("*").click()
        except TimeoutException:
            return False
        
        WTF_TIMEOUT_MANAGER.brief_pause()
        title = self.webdriver.find_element_by_css_selector("div.fr > div.tck1 > strong:nth-child(1)").text

        return title == "Black Classic-fit Suit"


    def add_to_wish_list(self):
        self.webdriver.find_element_by_id("addwish").click()
        try:
            WebDriverWait(self.webdriver, 3).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to_alert()
            alert_text = alert.text
            alert.accept()
        except TimeoutException:
            return False

        condition1 = alert_text == "Collect success!"
        condition2 = alert_text == "Pro, you have to collect the goods!"

        return condition1 or condition2

    def share_facebook(self):
        self.goto_productpage()
        browser = WTF_CONFIG_READER.get("selenium.browser")

        if browser == "FIREFOX":
            currentwindows = self.webdriver.window_handles # set of windows already open
            self.webdriver.find_element_by_css_selector("ul.list1ul > li > a:nth-child(1)").click()
            WTF_TIMEOUT_MANAGER.brief_pause()
            newwindows = self.webdriver.window_handles # 1 extra window shows up here.
            newwindow = list(set(newwindows) - set(currentwindows))[0]
            self.webdriver.switch_to_window(newwindow)
            title = self.webdriver.title
            self.webdriver.switch_to_window(currentwindows[0])

        elif browser == 'CHROME':
            mainwindow = self.webdriver.current_window_handle
            self.webdriver.find_element_by_css_selector("ul.list1ul > li > a:nth-child(1)").click()
            WTF_TIMEOUT_MANAGER.brief_pause()
            self.webdriver.switch_to_window(self.webdriver.window_handles[1])

            title = self.webdriver.title
            self.webdriver.close()
            self.webdriver.switch_to_window(mainwindow)
            WTF_TIMEOUT_MANAGER.brief_pause()

        return "Facebook" in title

    def zoomin(self):
        self.webdriver.get(self.base_url+'Shop.php')
        self.goto_productpage()
        pic = self.webdriver.find_element_by_id("zoompic")
        hover = ActionChains(self.webdriver).move_to_element(pic)
        hover.perform()
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "cloudzoom-blank")), 'Timed Out')
            condition = True
        except TimeoutException:
            return False

        slideshow = self.webdriver.find_element_by_class_name("cycle-slideshow")
        unhover = ActionChains(self.webdriver).move_to_element(slideshow)
        unhover.perform()

        return condition

    def add_two_to_shopping_cart(self):
        self.webdriver.get(self.base_url+'Shop.php')
        self.goto_productpage()
        self.webdriver.find_element_by_id("jia").click()
        self.webdriver.find_element_by_id("addcart").click()
        self.webdriver.find_element_by_class_name("toCartlink").click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        title = self.webdriver.find_element_by_class_name("title").text
        price = self.webdriver.find_element_by_css_selector(".buy>ul>li:nth-child(5)>p").text
        WTF_TIMEOUT_MANAGER.brief_pause()
        return title == "Black Classic-fit Suit" and price == "3332"

    def shop_test(self):
        test1 = self.goto_productpage()
        test2 = self.add_to_wish_list()
        test3 = self.share_facebook()
        test5 = self.add_two_to_shopping_cart()
        test4 = self.zoomin()
        return test1 and test2 and test3 and test4 and test5
