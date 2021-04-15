from selenium import webdriver
from objectrepository.LoginPageOR import LoginPageOR
import unittest
import time
from testcases.BaseClass import BaseClass

class TestCaseLogin(unittest.TestCase,BaseClass):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(self.chrompath)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.loginPage = LoginPageOR(self.driver)


    def testcaseLoginUser(self):
        self.username = "faizan.raheem@nxb.com.pk"
        self.password = "login101"

        self.loginPage.navToLogin()
        time.sleep(2)
        self.loginPage.setUserName(self.username)
        time.sleep(2)
        self.loginPage.setPassword(self.password)
        time.sleep(2)
        self.loginPage.clickSignin()
        assert self.loginPage.getPageTitle()
      #  assert loginPage.

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Execution is completed successfully")




