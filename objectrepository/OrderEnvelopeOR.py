from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

import random


class OrderEnvelopeOR:
    def __init__(self, driver = webdriver.Chrome):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.managementXpath = "//*[@id='mainNav']/li[4]/a"
        self.orderOptionXpath = "//*[@id='mainNav']/li[4]/ul/li[5]/a"
        self.addToCartBtnXpath = "//*[@id='update']"
        self.addToCartProductXpath = "//*[@id='add-cart']"
        self.checkOutbtnXpath = "/html/body/div[1]/div[1]/div/div/div/div/div/div/div/div[3]/div/div/a[2]"
        self.checkoutProductXpath = "//*[@id='checkout']/div[3]/div/div/button"
        self.confirmBtnXpath = "/html/body/div[5]/div/div[3]/button[1]"
        self.priceBeforePurchaseXpath = "//*[@id='checkout']/div[1]/div/div/div/div[2]/div/div[2]/div/div/table/tbody/tr[3]/td/b/span"
        self.priceAfterPurchaseXpath = "//*[@id='gridBody']/table/tbody/tr[1]/td[8]"
        self.priceBeforePurchase = ""
        self.priceAfterPurchase  = ""

    def navToEnvelopeStore(self):
        elementManagementTab = self.driver.find_element(By.XPATH, self.managementXpath)
        time.sleep(1)
        self.action.move_to_element(elementManagementTab).perform()
        time.sleep(2)
        elementOrderOption = self.driver.find_element(By.XPATH, self.orderOptionXpath)
        elementOrderOption.click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 300);")
        elementAddToCartList = self.driver.find_elements(By.XPATH,self.addToCartBtnXpath)
        #listSize = len(elementAddToCartList)
        #elementAddToCartList[random.randrange(0,listSize)].click()
        elementAddToCartList[0].click()
        time.sleep(2)
        elementAddToCardProduct = self.driver.find_element(By.XPATH, self.addToCartProductXpath)
        elementAddToCardProduct.click()
        time.sleep(4)

        self.driver.execute_script("window.scrollTo(0, 2000);")

        time.sleep(2)
        #self.action.move_to_element(self.driver.find_element(By.XPATH, self.checkOutbtnXpath)).perform()
        #time.sleep(1)
        elementCheckoutBtn = self.driver.find_element(By.XPATH, self.checkOutbtnXpath)

        elementCheckoutBtn.click()

        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2 )
        elementPriceBeforePurchase = self.driver.find_element(By.XPATH, self.priceBeforePurchaseXpath)
        self.priceBeforePurchase = elementPriceBeforePurchase.text
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1500);")

        elementCheckoutProduct = self.driver.find_element(By.XPATH, self.checkoutProductXpath)
        elementCheckoutProduct.click()

        time.sleep(2)

        elementConfirmCheckoutBtn = self.driver.find_element(By.XPATH, self.confirmBtnXpath)
        elementConfirmCheckoutBtn.click()
        time.sleep(3)

        self.driver.execute_script("window.scrollTo(0, 400);")

        elementPriceAfterPurchase = self.driver.find_element(By.XPATH, self.priceAfterPurchaseXpath)
        self.priceAfterPurchase = elementPriceAfterPurchase.text


    def validateRate(self):
        if self.priceBeforePurchase in self.priceAfterPurchase:
            return  True
        else:
            return False

