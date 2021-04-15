from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
class LoginPageOR:
    def __init__(self , driver):
        self.driver = driver
       # self.__init__(driver)
        self.loginLink = "//*[@id='topNav']/li[1]/a"
        self.username = "email"
        self.password = "password"
        self.signinBtn = "//*[@id='login']/div[3]/div[2]/button"


    def navToLogin(self):
        element = self.driver.find_element_by_xpath(self.loginLink)
        element.click()



    def setUserName(self,uname):
        element = self.driver.find_element_by_id(self.username)
        element.send_keys(uname)

    def setPassword(self,pass1):
        element = self.driver.find_element_by_id(self.password)
        element.send_keys(pass1)

    def clickSignin(self):
        element = self.driver.find_element_by_xpath(self.signinBtn)
        element.click()

    def getPageTitle(self):
        self.title =  self.driver.title
        if "Dashboard" in self.title:
            return True
        else:
            return False



