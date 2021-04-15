from objectrepository.HomePageOR import HomePageOR
from testcases.BaseClass import BaseClass
import unittest
import time



class TestCaseBlogList(unittest.TestCase, BaseClass):

    @classmethod
    def setUp(self):

        self.driver = self.initDriver(self)
        self.cmlHomePage1 = HomePageOR(self.driver)
        self.checkBlogCount = False

    def testBlogLinks(self):
       self.scrollTo('250')
       time.sleep(3)
       self.checkBlogCount =  self.cmlHomePage1.getBlogLinks()
       assert self.checkBlogCount

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()