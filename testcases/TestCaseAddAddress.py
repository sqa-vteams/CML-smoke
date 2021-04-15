from objectrepository.AddAddressOR import AddAdressOR
import unittest
from testcases.BaseClass import BaseClass
from faker import Faker


class TestCaseAddAddress(unittest.TestCase, BaseClass):
    @classmethod
    def setUp(self):
        self.driver = self.initDriver(self)
        self.x = Faker('en_US')
        self.name = self.x.name()
        self.address = self.x.address()
        self.add1 = self.address.split('\n')
        self.address1 = self.add1[0]
        self.citystate = self.add1[1].split(',')
        self.city = self.citystate[0]
        self.state = self.citystate[1].strip()
        self.state = self.state.split()
        self.stateshort = self.state[0]
        self.zip = self.state[1]
        self.driver = self.login(self, self.driver)
        self.addAddress = AddAdressOR(self.driver)

    def testcaseAddAddress(self):
        print("Test Case Execution Started")
        print("Name of the user is:"+str(self.name))
        self.addAddress.addAddress(self.name, self.address1, self.city, self.stateshort, self.zip)
        #self.addAddress.verifyAddress(self.name)


    @classmethod
    def tearDown(self):
        self.driver.quit()