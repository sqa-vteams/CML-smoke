import unittest
from objectrepository.HomePageOR import HomePageOR
from testcases.BaseClass import BaseClass
import time
class TestCaseCmlLogo(unittest.TestCase,BaseClass):
    @classmethod
    def setUp(self):
        self.initDriver(self)
        self.cmlHomePage = HomePageOR(self.driver)
        self.checkCmlLog = False

    def testCmlLogo(self):
        self.checkCmlLog = self.cmlHomePage.clickCMLLogo()
        time.sleep(3)
        assert self.checkCmlLog

    @classmethod
    def tearDown(self):
       self.driver.close()
       self.driver.quit()

