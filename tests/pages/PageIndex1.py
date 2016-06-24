"""
Created on Jun 27, 2013

@author: davidlai
"""
#from selenium.common.exceptions import WebDriverException
#from selenium.webdriver.common import utils
#import os
#import selenium
#import subprocess


'''
import time
import wtframework.wtf.web.page
from tests.flows.search_flows import perform_search
from tests.pages.search_page import ISearchPage
from tests.pages.www_google_com import GoogleSearchPage
from tests.pages.www_yahoo_com import YahooSearchPage
from tests.testdata.settings import get_search_provider
from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.utils.test_utils import do_and_ignore
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER, WTF_CONFIG_READER, WTF_TIMEOUT_MANAGER
'''
from wtframework.wtf.web.page import PageObject, InvalidPageError
from wtframework.wtf.web.webdriver import WTF_CONFIG_READER
# from selenium import webdriver

class PageIndex1(PageObject):
    '''
    PageIndex
    WTFramework PageObject representing a page like:
    http://ec2-52-9-175-55.us-west-1.compute.amazonaws.com/index-1.php
    '''

    ### Page Elements Section ###
    virtualfitting = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(2)>ul:nth-child(2)>li>a>span")
    shop = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(2)>ul:nth-child(2)>li:nth-child(2)>a>span")
    emshare = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(2)>ul:nth-child(2)>li:nth-child(3)>a>span")
    fashion = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(2)>ul:nth-child(2)>li:nth-child(4)>a>span")
    pros = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(2)>ul:nth-child(2)>li:nth-child(5)>a>span")
    cart = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(2)>ul:nth-child(5)>li>a>div")
    me = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(2)>ul:nth-child(5)>li:nth-child(2)>a>img")
    signin = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(2)>ul:nth-child(5)>ul>li>a>img")
    home = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(2)>ul:nth-child(2)>li:nth-child(6)>a>img")
    keyword = lambda self:self.webdriver.find_element_by_name("keyword")
    Amazon = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(4)>div>a>img")
    eBay = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(4)>div>a:nth-child(2)>img")
    Soho = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(6)>ul>li>a>img")
    Sophies = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div>div>div:nth-child(6)>ul>li:nth-child(2)>a>img")
    company_a = lambda self:self.webdriver.find_element_by_css_selector("html>body>div>div:nth-child(2)>div>ul>li:nth-child(2)>a")
    ### End Page Elements Section ###

    # expected answers
    base_url = WTF_CONFIG_READER.get("baseurl")
    virtualfitting_url = base_url+"tryonindex.php"
    shop_url = base_url+"Shop.php"
    emshare_url = base_url+"SHARE.php"
    fashion_url = base_url+"Fashion%20News.php"
    pros_url = base_url+"PROS.php"
    signin_url = base_url+"signin.php"
    home_url = base_url+"index.php"
    Amazon_url = "http://amzn.to/1slc81o"
    eBay_url = "http://www.ebay.com/rpp/fashion-main?rmvSB=true"
    Soho_url = base_url+"goodslist.php?bid=11"
    Sophies_url = base_url+"goodslist.php?bid=12"
    cart_url = base_url+"shoppingcart.php?a=buynow"
    
   
    def _validate_page(self, webdriver):
        '''
        Validates page.
        '''
        if not 'http://ec2-52-9-175-55.us-west-1.compute.amazonaws.com/index-1.php' in webdriver.current_url:
            raise InvalidPageError("This is not index-1.")
    '''
    webdriver = None
    def __init__(self, webdriver):
        self._validate_page(webdriver)   
        self.webdriver = webdriver
    '''
    def validate_links(self):
        '''
        Validates links on the page.
        '''
        #if  not (self.virtualfitting_url in self.virtualfitting.click()):
        #    raise InvalidPageError("Index1 page did not pass validation.")
        self.virtualfitting().click()
        if not (self.virtualfitting_url in self.webdriver.current_url):
            raise InvalidPageError("Virtual Tryon link is broken.")
        else:
            self.shop().click()
            if not (self.shop_url in self.webdriver.current_url):
                raise InvalidPageError("Shop link is broken.")
            else:
                self.emshare().click()
                if not (self.emshare_url in self.webdriver.current_url):
                    raise InvalidPageError("emshare link is broken.")
                else:
                    self.pros().click()
                    if not (self.pros_url in self.webdriver.current_url):
                        raise InvalidPageError("emshare link is broken.")
                    else:
                        self.fashion().click()
                        if not (self.fashion_url in self.webdriver.current_url):
                            raise InvalidPageError("emshare link is broken.")
                        else:
                            self.cart().click()
                            if not (self.cart_url in self.webdriver.current_url):
                                raise InvalidPageError("emshare link is broken.")
                            else:
                                return True
                            '''
                                self.Soho().click()
                                if not (self.Soho_url in self.webdriver.current_url):
                                    raise InvalidPageError("emshare link is broken.")
                                else:
                                    self.Sophies().click()
                                    if not (self.Sophies_url in self.webdriver.current_url):
                                        raise InvalidPageError("emshare link is broken.")
                                    else:
                                        self.Amazon().click()
                                        if not (self.Amazon_url in self.webdriver.current_url):
                                            raise InvalidPageError("emshare link is broken.")
                                        else:
                            self.home().click()
                            if not (self.home_url in self.webdriver.current_url):
                                raise InvalidPageError("emshare link is broken.")
                            else:
                                    '''