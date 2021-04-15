from objectrepository.RegistrationOR import RegisterationOR
from faker import Faker
import time
import unittest
from testcases.BaseClass import BaseClass
from datetime import datetime

class TestCaseRegistration(unittest.TestCase, BaseClass):

    @classmethod
    def setUp(self):
        self.driver = self.initDriver(self)
        self.x = Faker('en_US')
        self.address = self.x.address()
        self.add1 = self.address.split('\n')
        self.address1 = self.add1[0]
        self.citystate = self.add1[1].split(',')
        self.city = self.citystate[0]
        self.state = self.citystate[1].strip()
        self.state = self.state.split()
        self.stateshort = self.state[0]
        self.zip = self.state[1]

    def testregisterUser(self):

        self.registerationPage = RegisterationOR(self.driver)
        self.registerationPage.navToRegisterPage()
        time.sleep(2)
        self.registerationPage.setname("Test Parent", "User Smoke")
        time.sleep(2)
        self.registerationPage.setaddress(self.address1,self.city,self.stateshort,self.zip)
        self.driver.execute_script("window.scrollTo(0, 500);")
        self.registerationPage.setemailpass(self.x.email(),"login101")
        time.sleep(2)
        now = datetime.now()
       # dateTime = datetime.timestamp(now)
        self.driver.get_screenshot_as_png()
        self.driver.save_screenshot("E:\Faizan Data\screenshotsScripts/screenshot"+now.__str__()+".png")
        self.registerationPage.checkAgreeBox()
        time.sleep(2)
        self.registerationPage.clickRegister()





    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Execution is completed successfully")
