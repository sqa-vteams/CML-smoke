from selenium import webdriver
from objectrepository.LoginPageOR import LoginPageOR
from objectrepository.RegisterSubuserOR import RegisterSubuserOR
import time
import unittest
from testcases.BaseClass import BaseClass
from faker import Faker
import logging
class TestCaseRegisterSubuser(unittest.TestCase,BaseClass):
    @classmethod
    def setUp(self):
        #self.url = "https://test.certifiedmaillabels.com/"

        self.driver = self.initDriver(self)
        #self.loginPage = LoginPageOR(self.driver)
        self.driver = self.login(self, self.driver)
        self.addSubUserPage = RegisterSubuserOR(self.driver)

        self.x = Faker('en_US')
        self.fname = self.x.first_name()
        self.lname = self.x.last_name()
        self.address = self.x.address()
        self.add1 = self.address.split('\n')
        self.address1 = self.add1[0]
        self.citystate = self.add1[1].split(',')
        self.city = self.citystate[0]
        self.state = self.citystate[1].strip()
        self.state = self.state.split()
        self.stateshort = self.state[0]
        self.zip = self.state[1]
        self.phone = self.x.random_int(1111111111, 9999999999)
        self.email = self.fname+"@gmail.com"
        self.password = "login101"

    def testRegisterSubuser(self):
        self.addSubUserPage.navToUser()
        time.sleep(3)
        self.addSubUserPage.clickAddUser()
        time.sleep(3)
        self.addSubUserPage.submitForm(self.fname, self.lname, self.address1, self.city, self.stateshort, self.zip, self.phone, self.email, self.password)
        time.sleep(5)
        print("User is registered successfully")
        foundCheck = self.addSubUserPage.verifyUser(self.fname)
        assert foundCheck
        if foundCheck==True:
            print("User found in subuser table")
        else:
            print("User doesn't found in subuser table")


    @classmethod
    def tearDown(self):
        self.driver.close()
        logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
        logging.info("This is information message....!")





