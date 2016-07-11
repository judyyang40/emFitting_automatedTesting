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
from selenium.webdriver.support.ui import Select

class ShopPage(PageObject):
    '''
    ShopPage
    WTFramework PageObject representing a page like:
    https://qa.emfitting.com/Shop.php
    '''


    ### Page Elements Section ###
    ### End Page Elements Section ###
    base_url = WTF_CONFIG_READER.get("baseurl")
    product_url = base_url+'goodsshow.php?cid=12&tid=39&id=573'
    cart_url = base_url+'shoppingcart.php'
    browser = WTF_CONFIG_READER.get("selenium.browser")

    def _validate_page(self, webdriver):
        '''
        Validates we are on the correct page.
        '''

        if not self.base_url+'Shop.php' in webdriver.current_url:
            raise InvalidPageError("This page did not pass ShopPage page validation.")

    def goto_category(self):
        self.webdriver.find_element_by_css_selector("a[href*='tid=39']").click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'goodslist.php?cid=12&tid=39' == self.webdriver.current_url

    def goto_tryon_from_product_details(self):
        self.webdriver.get(self.product_url)
        self.webdriver.find_element_by_class_name("tryonbutton").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "trypicimg")), 'Timed Out')
            tryonpicid = self.webdriver.find_element_by_class_name("trypicimg").get_attribute("id")
        except TimeoutException:
            return False

        return tryonpicid == "trypicimg573"

    def like_product(self):
        self.webdriver.get(self.product_url)
        self.webdriver.find_element_by_css_selector("div.likeblock>img").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False

        if alert_text != "like":
            return False

        self.webdriver.refresh()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "likes")), 'Timed Out')
            likes = self.webdriver.find_element_by_id("likes").get_attribute("value")
        except TimeoutException:
            return False

        return likes == "1"

    def dislike_product(self):
        self.webdriver.get(self.product_url)
        self.webdriver.find_element_by_css_selector("div.likeblock>img").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False

        if alert_text != "like cancel":
            return False

        self.webdriver.refresh()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "likes")), 'Timed Out')
            likes = self.webdriver.find_element_by_id("likes").get_attribute("value")
        except TimeoutException:
            return False

        return likes == "0"

    def add_to_wishlist(self):
        self.webdriver.get(self.product_url)
        self.webdriver.find_element_by_id("addwish").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False

        condition1 = alert_text == "Collect success!"
        condition2 = alert_text == "Pro, you have to collect the goods!"

        return condition1 or condition2

    def next_page_of_items(self):
        self.webdriver.get(self.product_url)
        self.webdriver.find_element_by_link_text("Next").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "left1ulpic")), 'Timed Out')
            img = self.webdriver.find_element_by_class_name("left1ulpic")
        except TimeoutException:
            return False
        img_url = img.find_element_by_css_selector("a > img").get_attribute("src")

        return "uploads/image/20160601/1464728805.jpg" in img_url 

    def show_size_helper(self):
        self.webdriver.get(self.product_url)
        main_window = self.webdriver.current_window_handle
        self.webdriver.find_element(By.XPATH, '//button[text()="Size Helper"]').click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        self.webdriver.switch_to_window(self.webdriver.window_handles[1])
        url = self.webdriver.current_url
        self.webdriver.close()
        self.webdriver.switch_to_window(main_window)
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'sizehelper.php' ==  url

    def show_3Dmodel(self):
        self.webdriver.get(self.product_url)
        main_window = self.webdriver.current_window_handle
        self.webdriver.find_element(By.XPATH, '//button[text()="Size Helper"]').click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        self.webdriver.switch_to_window(self.webdriver.window_handles[1])

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "Submit")), 'Timed Out')
            self.webdriver.find_element_by_id("Submit").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 20).until(EC.visibility_of_element_located((By.ID, "lcanvas")), 'Timed Out')
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.short_pause()
        model_src = self.webdriver.find_element_by_id("lcanvas").get_attribute("src")
        self.webdriver.close()
        self.webdriver.switch_to_window(main_window)
        WTF_TIMEOUT_MANAGER.brief_pause()

        return "3d-demo-folder2/wd17.png" in model_src

    def show_dress_recommendations(self):
        self.webdriver.get(self.product_url)
        main_window = self.webdriver.current_window_handle
        self.webdriver.find_element(By.XPATH, '//button[text()="Size Helper"]').click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        self.webdriver.switch_to_window(self.webdriver.window_handles[1])
        flag = False

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "Submit")), 'Timed Out')
            self.webdriver.find_element_by_id("Submit").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Modify']")), 'Timed Out')
            self.webdriver.find_element_by_xpath("//input[@value='Modify']").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), ' Dress Sizes Recommendations ')]")), 'Timed Out')
            flag = True
        except TimeoutException:
            return False

        self.webdriver.close()
        self.webdriver.switch_to_window(main_window)
        WTF_TIMEOUT_MANAGER.brief_pause()

        return flag

    def close_size_helper_popup(self):
        self.webdriver.get(self.product_url)
        main_window = self.webdriver.current_window_handle
        self.webdriver.find_element(By.XPATH, '//button[text()="Size Helper"]').click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        self.webdriver.switch_to_window(self.webdriver.window_handles[1])

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "Submit")), 'Timed Out')
            self.webdriver.find_element_by_id("Submit").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Modify']")), 'Timed Out')
            self.webdriver.find_element_by_xpath("//input[@value='Modify']").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@value='Done']")), 'Timed Out')
            self.webdriver.find_element_by_xpath("//input[@value='Done']").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert.accept()
        except TimeoutException:
            return False

        self.webdriver.switch_to_window(main_window)
        WTF_TIMEOUT_MANAGER.brief_pause()

        window_num = len(self.webdriver.window_handles)

        return window_num == 1

    def add_to_cart(self):
        self.webdriver.get(self.product_url)
        self.webdriver.find_element_by_id("jia").click()
        self.webdriver.find_element_by_id("addcart").click()
        return True

    def check_shopping_cart(self):
        self.webdriver.get(self.product_url)
        self.webdriver.find_element_by_css_selector("li.accountlink>a").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "title")), 'Timed Out')
            titles = self.webdriver.find_elements_by_class_name("title")
        except TimeoutException:
            return False

        for t in titles:
            if t.text == "White Lotus Poncho":
                return True

        return False

    def remove_item_from_cart(self):
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, "Remove")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Remove").click()
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Your shopping cart is empty')]")), 'Timed Out')
            return True
        except TimeoutException:
            return False


    def change_quantity_in_cart(self):
        self.webdriver.get(self.base_url+'goodsshow.php?cid=12&tid=29&id=554')
        self.webdriver.find_element_by_id("addcart").click()
        self.webdriver.find_element_by_css_selector("li.accountlink>a").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "jia")), 'Timed Out')
            self.webdriver.find_element_by_id("jia").click()
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()
        quantity = self.webdriver.find_element_by_id("num0").get_attribute("value")
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), '$776')]")), 'Timed Out')
            if quantity == "2":
                return True
            else:
                return False
        except TimeoutException:
            return False

    def remove_all_from_cart(self):
        self.webdriver.get(self.base_url+'goodsshow.php?cid=12&tid=31&id=493')
        self.webdriver.find_element_by_id("addcart").click()
        self.webdriver.find_element_by_css_selector("li.accountlink>a").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "stu")), 'Timed Out')
            self.webdriver.find_element_by_name("stu").click()
        except TimeoutException:
            return False
        removes = self.webdriver.find_elements_by_link_text("Remove")
        removes[2].click()

        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Your shopping cart is empty')]")), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def goto_checkout(self):
        self.add_to_cart()
        self.webdriver.find_element_by_css_selector("li.accountlink>a").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "next")), 'Timed Out')
            self.webdriver.find_element_by_class_name("next").click()
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'checkoutoptions.php' in self.webdriver.current_url

    def checkout_as_guest(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "guestemail")), 'Timed Out')
            self.webdriver.find_element_by_id("guestemail").send_keys("aaa@gmail.com")
        except TimeoutException:
            return False
        self.webdriver.find_element_by_xpath("//input[@value='Checkout as Guest']").click()

        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'guestorder.php' in self.webdriver.current_url

    def back_on_guestcheckout(self):
        self.webdriver.find_element_by_link_text("Back").click()

        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'shoppingcart.php' in self.webdriver.current_url

    def place_order_without_shipping_option(self):
        self.webdriver.find_element_by_class_name("next").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "guestemail")), 'Timed Out')
            self.webdriver.find_element_by_id("guestemail").send_keys("aaa@gmail.com")
        except TimeoutException:
            return False
        self.webdriver.find_element_by_xpath("//input[@value='Checkout as Guest']").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Place order")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Place order").click()
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == "Please select shipping method!"

    def place_order_without_payment_option(self):
        shipping = self.webdriver.find_element_by_id("postmode")
        shipping_select = Select(shipping)
        shipping_select.select_by_visible_text('Standard')
        self.webdriver.find_element_by_link_text("Place order").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == "Please select payment method!"

    def place_order_using_paypal(self):
        payment = self.webdriver.find_element_by_id("paymode")
        payment_select = Select(payment)
        payment_select.select_by_visible_text('PayPal')

        self.webdriver.find_element_by_id("username").send_keys("Adam")
        self.webdriver.find_element_by_id("line").send_keys("1525 McCarthy Blvd.")
        self.webdriver.find_element_by_id("city").send_keys("Milpitas")
        self.webdriver.find_element_by_id("Zip").send_keys("95035")
        self.webdriver.find_element_by_id("phone").send_keys("1234567890")

        self.webdriver.find_element_by_link_text("Place order").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'Shipping fee')]")), 'Timed Out')
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'Estimated tax to be collected')]")), 'Timed Out')
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Order total')]")), 'Timed Out')
        except TimeoutException:
            return False

        return self.base_url+'orderenter.php' in self.webdriver.current_url

    def place_order_after_review(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "submitBtn")), 'Timed Out')
            self.webdriver.find_element_by_id("submitBtn").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Total')]")), 'Timed Out')
        except TimeoutException:
            return False

        return 'https://www.sandbox.paypal.com' in self.webdriver.current_url

    def login_to_paypal(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "loadLogin")), 'Timed Out')
            self.webdriver.find_element_by_id("loadLogin").click()
        except TimeoutException:
            return False     
        
        try:
            WebDriverWait(self.webdriver, 20).until(EC.visibility_of_element_located((By.ID, "login_email")), 'Timed Out')
            self.webdriver.find_element_by_id("login_email").send_keys("testperson@emreal-corp.com")
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.ID, "login_password")), 'Timed Out')
            self.webdriver.find_element_by_id("login_password").send_keys("emrealcorp")
        except TimeoutException:
            return False   
        self.webdriver.find_element_by_id("submitLogin").click()

        try:
            WebDriverWait(self.webdriver, 30).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Review your information')]")), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def process_payment(self):
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.ID, "continue")), 'Timed Out')
            self.webdriver.find_element_by_id("continue").click()
        except TimeoutException:
            return False  

        if self.browser == "FIREFOX":
            try:
                WebDriverWait(self.webdriver, 30).until(EC.alert_is_present(), 'Timed out')
                alert = self.webdriver.switch_to.alert
                alert.accept()
            except TimeoutException:
                return False

        try:
            WebDriverWait(self.webdriver, 30).until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Order is placed successfully.')]")), 'Timed Out')
        except TimeoutException:
            return False 

        #return self.base_url+'b.php' in self.webdriver.current_url
        return 'b.php' in self.webdriver.current_url

    def place_order_with_credit_card(self):
        self.goto_checkout()
        self.checkout_as_guest()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "username")), 'Timed Out')
            self.webdriver.find_element_by_id("username").send_keys("Adam")
        except TimeoutException:
            return False 
        self.webdriver.find_element_by_id("line").send_keys("1525 McCarthy Blvd.")
        self.webdriver.find_element_by_id("city").send_keys("Milpitas")
        self.webdriver.find_element_by_id("Zip").send_keys("95035")
        self.webdriver.find_element_by_id("phone").send_keys("1234567890")

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "username")), 'Timed Out')
            shipping = self.webdriver.find_element_by_id("postmode")
        except TimeoutException:
            return False 
        shipping_select = Select(shipping)
        shipping_select.select_by_visible_text('Standard')

        payment = self.webdriver.find_element_by_id("paymode")
        payment_select = Select(payment)
        payment_select.select_by_visible_text('Credit Card')

        self.webdriver.find_element_by_link_text("Place order").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'Shipping fee')]")), 'Timed Out')
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'Estimated tax to be collected')]")), 'Timed Out')
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Order total')]")), 'Timed Out')
        except TimeoutException:
            return False

        return self.base_url+'orderenter.php' in self.webdriver.current_url

    def place_order_without_card_number(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "submitBtn")), 'Timed Out')
            self.webdriver.find_element_by_id("submitBtn").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == "The credit card number appears to be invalid."

    def place_order_without_CVC(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "card-number")), 'Timed Out')
            self.webdriver.find_element_by_class_name("card-number").send_keys("378282246310005")
        except TimeoutException:
            return False
        self.webdriver.find_element_by_id("submitBtn").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == "The CVC number appears to be invalid."

    def place_order_without_expiration_date(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "card-cvc")), 'Timed Out')
            self.webdriver.find_element_by_class_name("card-cvc").send_keys("1811")
        except TimeoutException:
            return False
        self.webdriver.find_element_by_id("submitBtn").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.alert_is_present(), 'Timed out')
            alert = self.webdriver.switch_to.alert
            alert_text = alert.text
            WTF_TIMEOUT_MANAGER.brief_pause()
            alert.accept()
        except TimeoutException:
            return False

        return alert_text == "The expiration date appears to be invalid."

    def process_credit_card(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "card-expiry-month")), 'Timed Out')
            self.webdriver.find_element_by_class_name("card-expiry-month").send_keys("11")
            self.webdriver.find_element_by_class_name("card-expiry-year").send_keys("2020")
        except TimeoutException:
            return False
        self.webdriver.find_element_by_id("submitBtn").click()

        try:
            WebDriverWait(self.webdriver, 30).until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Order is placed successfully.')]")), 'Timed Out')
        except TimeoutException:
            return False 

        #return self.base_url+'b.php' in self.webdriver.current_url
        return 'b.php' in self.webdriver.current_url

    def signin(self):
        self.webdriver.get(self.base_url+'signin.php')
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.NAME, "username")), 'Timed Out')
            self.webdriver.find_element_by_name("username").send_keys("aaa@gmail.com")
            self.webdriver.find_element_by_name("password").send_keys("123456"+Keys.RETURN)
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()
        return self.base_url+'SHARE.php' in self.webdriver.current_url

    def goto_checkout_logged_in(self):
        self.add_to_cart()
        self.webdriver.find_element_by_css_selector("li.accountlink>a").click()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "next")), 'Timed Out')
            self.webdriver.find_element_by_class_name("next").click()
        except TimeoutException:
            return False

        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'order.php' in self.webdriver.current_url

    def open_popup_to_add_new_shipping_address(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "add_add")), 'Timed Out')
            self.webdriver.find_element_by_class_name("add_add").click()
        except TimeoutException:
            return False

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "envon")), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def add_new_shipping_address(self):
        num_address = len(self.webdriver.find_elements_by_class_name("ad_on"))
        self.webdriver.find_element_by_id("username").send_keys("Adam")
        self.webdriver.find_element_by_id("line").send_keys("1525 McCarthy Blvd.")
        self.webdriver.find_element_by_id("city").send_keys("Milpitas")
        self.webdriver.find_element_by_id("zip").send_keys("95035")
        self.webdriver.find_element_by_id("phone").send_keys("1234567890")
        self.webdriver.find_element_by_link_text("Ship to this address").click()
        WTF_TIMEOUT_MANAGER.brief_pause()
        num_address_after = len(self.webdriver.find_elements_by_class_name("ad_on"))

        return num_address_after == (num_address+1)

    def place_order_using_paypal_logged_in(self):
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "postmode")), 'Timed Out')
            shipping = self.webdriver.find_element_by_id("postmode")
        except TimeoutException:
            return False 
        shipping_select = Select(shipping)
        shipping_select.select_by_visible_text('Standard')

        payment = self.webdriver.find_element_by_id("paymode")
        payment_select = Select(payment)
        payment_select.select_by_visible_text('PayPal')

        self.webdriver.find_element_by_link_text("Place order").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'Shipping fee')]")), 'Timed Out')
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'Estimated tax to be collected')]")), 'Timed Out')
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Order total')]")), 'Timed Out')
        except TimeoutException:
            return False

        return self.base_url+'orderenter.php' in self.webdriver.current_url

    def place_order_after_review_logged_in(self):
        return self.place_order_after_review()

    def login_to_paypal_logged_in(self):
        '''#take this part out if testing whole shop_age
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "loadLogin")), 'Timed Out')
            self.webdriver.find_element_by_id("loadLogin").click()
        except TimeoutException:
            return False     
        
        try:
            WebDriverWait(self.webdriver, 20).until(EC.visibility_of_element_located((By.ID, "login_email")), 'Timed Out')
            self.webdriver.find_element_by_id("login_email").send_keys("testperson@emreal-corp.com")
        except TimeoutException:
            return False
        #
        '''

        try:
            WebDriverWait(self.webdriver, 30).until(EC.visibility_of_element_located((By.ID, "login_password")), 'Timed Out')
            self.webdriver.find_element_by_id("login_password").send_keys("emrealcorp")
        except TimeoutException:
            return False   
        self.webdriver.find_element_by_id("submitLogin").click()

        try:
            WebDriverWait(self.webdriver, 30).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Review your information')]")), 'Timed Out')
            return True
        except TimeoutException:
            return False

    def process_payment_logged_in(self):
        return self.process_payment()

    def place_order_with_credit_card_logged_in(self):
        self.goto_checkout_logged_in()
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.ID, "postmode")), 'Timed Out')
            shipping = self.webdriver.find_element_by_id("postmode")
        except TimeoutException:
            return False 
        shipping_select = Select(shipping)
        shipping_select.select_by_visible_text('Standard')

        payment = self.webdriver.find_element_by_id("paymode")
        payment_select = Select(payment)
        payment_select.select_by_visible_text('Credit Card')

        self.webdriver.find_element_by_link_text("Place order").click()

        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'Shipping fee')]")), 'Timed Out')
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//td[contains(text(), 'Estimated tax to be collected')]")), 'Timed Out')
        except TimeoutException:
            return False
        try:
            WebDriverWait(self.webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(), 'Order total')]")), 'Timed Out')
        except TimeoutException:
            return False

        return self.base_url+'orderenter.php' in self.webdriver.current_url

    def place_order_without_card_number_logged_in(self):
        return self.place_order_without_card_number()

    def place_order_without_CVC_logged_in(self):
        return self.place_order_without_CVC()

    def place_order_without_expiration_date_logged_in(self):
        return self.place_order_without_expiration_date()

    def process_credit_card_logged_in(self):
        return self.process_credit_card()

    def goto_orderslist(self):
        self.webdriver.get(self.base_url+'My.php')
        hoverItem = WebDriverWait(self.webdriver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "signoutlinkaccount")))
        ActionChains(self.webdriver).move_to_element(hoverItem).perform()

        ordersBtn = WebDriverWait(self.webdriver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Orders")))
        ordersBtn.click()
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.webdriver.current_url == self.base_url+'myorder.php'

    def goto_order_details(self):
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, "Details")), 'Timed Out')
            self.webdriver.find_element_by_link_text("Details").click()
        except TimeoutException:
            return False 
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'ordershow.php?id=' in self.webdriver.current_url

    def goto_return_page(self):
        self.webdriver.get(self.base_url+'myorder.php')
        main_window = self.webdriver.current_window_handle
        try:
            WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((By.XPATH, '//input[@value=" Return & Refund "]')), 'Timed Out')
            self.webdriver.find_element(By.XPATH, '//input[@value=" Return & Refund "]').click()
        except TimeoutException:
            return False 

        self.webdriver.switch_to_window(self.webdriver.window_handles[1])
        url = self.webdriver.current_url
        self.webdriver.close()
        self.webdriver.switch_to_window(main_window)
        WTF_TIMEOUT_MANAGER.brief_pause()

        return self.base_url+'return.php' == url
        

    def shop_test(self):
        f = open("debug_shop.txt", "w")

        test2 = self.goto_category()
        f.write("test2: "+str(test2))
        test3 = self.goto_tryon_from_product_details()
        f.write("\ntest3: "+str(test3))
        test8 = self.next_page_of_items()
        f.write("\ntest8: "+str(test8))
        test13 = self.add_to_cart()
        f.write("\ntest13: "+str(test13))
        test14 = self.check_shopping_cart()
        f.write("\ntest14: "+str(test14))
        test16 = self.remove_item_from_cart()
        f.write("\ntest16: "+str(test16))
        test15 = self.change_quantity_in_cart()
        f.write("\ntest15: "+str(test15))
        test17 = self.remove_all_from_cart()
        f.write("\ntest17: "+str(test17))
        test18 = self.goto_checkout()
        f.write("\ntest18: "+str(test18))
        test19 = self.checkout_as_guest()
        f.write("\ntest19: "+str(test19))
        test20 = self.back_on_guestcheckout()
        f.write("\ntest20: "+str(test20))
        test21 = self.place_order_without_shipping_option()
        f.write("\ntest21: "+str(test21))
        test22 = self.place_order_without_payment_option()
        f.write("\ntest22: "+str(test22))
        test23 = self.place_order_using_paypal()
        f.write("\ntest23: "+str(test23))
        test24 = self.place_order_after_review()
        f.write("\ntest24: "+str(test24))
        test25 = self.login_to_paypal()
        f.write("\ntest25: "+str(test25))
        test26 = self.process_payment()
        f.write("\ntest26: "+str(test26))
        test28 = self.place_order_with_credit_card()
        f.write("\ntest28: "+str(test28))
        test29 = self.place_order_without_card_number()
        f.write("\ntest29: "+str(test29))
        test30 = self.place_order_without_CVC()
        f.write("\ntest30: "+str(test30))
        test31 = self.place_order_without_expiration_date()
        f.write("\ntest31: "+str(test31))
        test32 = self.process_credit_card()
        f.write("\ntest32: "+str(test32))

        #signin
        signin = self.signin()
        f.write("\nsignin: "+str(signin))
        test5 = self.like_product()
        f.write("\ntest5: "+str(test5))
        test6 = self.dislike_product()
        f.write("\ntest6: "+str(test6))
        test7 = self.add_to_wishlist()
        f.write("\ntest7: "+str(test7))
        test9 = self.show_size_helper()
        f.write("\ntest9: "+str(test9))
        test10 = self.show_3Dmodel()
        f.write("\ntest10: "+str(test10))
        test11 = self.show_dress_recommendations()
        f.write("\ntest11: "+str(test11))
        test12 = self.close_size_helper_popup()
        f.write("\ntest12: "+str(test12))

        test34 = self.goto_checkout_logged_in()
        f.write("\ntest34: "+str(test34))
        test35 = self.open_popup_to_add_new_shipping_address()
        f.write("\ntest35: "+str(test35))
        test36 = self.add_new_shipping_address()
        f.write("\ntest36: "+str(test36))

        test37 = self.place_order_using_paypal_logged_in()
        f.write("\ntest37: "+str(test37))
        test38 = self.place_order_after_review_logged_in()
        f.write("\ntest38: "+str(test38))
        test39 = self.login_to_paypal_logged_in()
        f.write("\ntest39: "+str(test39))
        test40 = self.process_payment_logged_in()
        f.write("\ntest40: "+str(test40))
        test42 = self.place_order_with_credit_card_logged_in()
        f.write("\ntest42: "+str(test42))
        test43 = self.place_order_without_card_number_logged_in()
        f.write("\ntest43: "+str(test43))
        test44 = self.place_order_without_CVC_logged_in()
        f.write("\ntest44: "+str(test44))
        test45 = self.place_order_without_expiration_date_logged_in()
        f.write("\ntest45: "+str(test45))
        test46 = self.process_credit_card_logged_in()
        f.write("\ntest46: "+str(test46))

        signin = self.signin()
        f.write("\nsignin: "+str(signin))
        test48 = self.goto_orderslist()
        f.write("\ntest48: "+str(test48))
        test49 = self.goto_order_details()
        f.write("\ntest49: "+str(test49))
        test50 = self.goto_return_page()
        f.write("\ntest50: "+str(test50))

        return test2 and test3 and test8 and test13 and test14 and test16 and test17 and test18 and test19 and test20 and test21 and test22 and test23 and test24 and test25 and test26 and test28 and test29 and test30 and test31 and test32 and test5 and test6 and test7 and test9 and test10 and test11 and test12 and test34 and test35 and test36 and test37 and test38 and test39 and test40 and test42 and test43 and test44 and test45 and test46 and test48 and test49 and test50
