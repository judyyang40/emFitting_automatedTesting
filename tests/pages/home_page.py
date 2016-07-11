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

class HomePage(PageObject):
    '''
    Home
    WTFramework PageObject representing a page like:
    https://qa.emfitting.com/index-1.php
    '''


    ### Page Elements Section ###
    ### End Page Elements Section ###
    base_url = WTF_CONFIG_READER.get("baseurl")
    home_url = base_url+'index-1.php'

    def _validate_page(self, webdriver):
        '''
        Validates we are on the correct page.
        '''

        if not self.base_url+'index-1.php' in webdriver.current_url:
            raise InvalidPageError("This page did not pass Home page validation.")

    
             
    def home_test(self):
        f = open("debug_home.txt", "w")
        test1 = self.goto_landing_page()
        f.write("test1: "+str(test1))
        test2 = self.goto_virtual_fitting()
        f.write("\ntest2: "+str(test2))
        test3 = self.goto_shop()
        f.write("\ntest3: "+str(test3))
        test4 = self.goto_emshare()
        f.write("\ntest4: "+str(test4))
        test5 = self.goto_fashion()
        f.write("\ntest5: "+str(test5))
        test6 = self.goto_pros()
        f.write("\ntest6: "+str(test6))
        test7 = self.goto_shopping_cart()
        f.write("\ntest7: "+str(test7))
        test8 = self.goto_me()
        f.write("\ntest8: "+str(test8))
        test9 = self.search_for_bracelet()
        f.write("\ntest9: "+str(test9))
        test10 = self.click_on_side_banner()
        f.write("\ntest10: "+str(test10))
        test11 = self.click_on_hot_item()
        f.write("\ntest11: "+str(test11))
        test12 = self.goto_category()
        f.write("\ntest12: "+str(test12))
        test13 = self.goto_brand()
        f.write("\ntest13: "+str(test13))
        test14 = self.goto_latest_share()
        f.write("\ntest14: "+str(test14))
        test15 = self.click_on_ad()
        f.write("\ntest15: "+str(test15))
        test16 = self.goto_wishlist()
        f.write("\ntest16: "+str(test16))
        test17 = self.find_experts_near_you()
        f.write("\ntest17: "+str(test17))
        test18 = self.goto_company_from_site_map()
        f.write("\ntest18: "+str(test18))

        return test1 and test2 and test3 and test4 and test5 and test6 and test7 and test8 and test9 and test10 and test11 and test12 and test13 and test14 and test15 and test16 and test17 and test18
