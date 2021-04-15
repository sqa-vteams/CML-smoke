import unittest
from objectrepository.OrderEnvelopeOR import OrderEnvelopeOR
from testcases.BaseClass import BaseClass

class TestCaseOrderEnvelope(BaseClass,unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = self.initDriver(self)
        self.driver = self.login(self, self.driver)
        self.orderEnvelope = OrderEnvelopeOR(self.driver)
        print("Test Case Execution Started...!")

    def testcaseOrderProcess(self):
        self.orderEnvelope.navToEnvelopeStore()
        assert self.orderEnvelope.validateRate()


    def tearDown(self):
        self.driver.quit()
        print("Test Case Completed")