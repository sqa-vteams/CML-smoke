import unittest
from faker import Faker
from testcases.BaseClass import BaseClass
from objectrepository.SingleLabelPurchaseOR import SingleLabelPurchase

class TestCaseSingleLabelPurchase(unittest.TestCase, BaseClass):

    @classmethod
    def setUp(self):
        self.driver = self.initDriver(self)
        self.driver = self.login(self, self.driver)
        self.purchaseLabel = SingleLabelPurchase(self.driver)
        self.x = Faker('en_US')
        self.name = self.x.name()+ " - Script"
        self.address = self.x.address()
        self.add1 = self.address.split('\n')
        self.address1 = self.add1[0]
        self.citystate = self.add1[1].split(',')
        self.city = self.citystate[0]
        self.state = self.citystate[1].strip()
        self.state = self.state.split()
        self.stateshort = self.state[0]
        self.zip = self.state[1]
        self.ref = "This label is created by automation script"

    def testcaseSingleLabelPurchase(self):
        print("Test Case Execution Started")
        self.purchaseLabel.navToSingleLabel(self.name, self.address1, self.city, self.stateshort,self.zip, self.ref)
        assert self.purchaseLabel.verifyLabel()

    @classmethod
    def tearDown(self):
        self.driver.quit()
        print("Test Case Execution is completed....!")
