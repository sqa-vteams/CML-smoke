from objectrepository.AddMailingProfileOR import AddMailingProfileOR
import unittest
from testcases.BaseClass import BaseClass
from faker import Faker

class TestCaseAddMailingProfile(unittest.TestCase, BaseClass):
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
        self.phone = self.x.random_int(1111111111, 9999999999)
        self.driver = self.login(self, self.driver)
        self.mailingProfile = AddMailingProfileOR(self.driver)

    def testcaseAddmailingProifle(self):
        print("Test Case Execution Started")
        print("Name of the user is:"+str(self.name))
        self.mailingProfile.addMailingProfile(self.name, self.address1, self.city, self.stateshort, self.zip, self.phone)
        #assert self.mailingProfile.verifyMailingProfile(self.name)



    @classmethod
    def tearDown(self):
        self.driver.quit()