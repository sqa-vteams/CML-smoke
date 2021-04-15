from selenium import webdriver
from objectrepository.HomePageOR import HomePageOR
from testcases.BaseClass import BaseClass
import unittest
from selenium.webdriver.common.by import By

class TestCaseGetStarted(unittest.TestCase, BaseClass):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(self.chrompath)
        #self.url = "https://test.certifiedmaillabels.com/"
        self.driver = self.initDriver(self, self.driver)
        self.cmlHomePage1 = HomePageOR(self.driver)
        self.checkUrl = False

    def testGetStartedLink(self):
        elementGetStartedLink = self.cmlHomePage1.clickGetStarted()
        self.checkUrl = elementGetStartedLink
        assert self.checkUrl

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
