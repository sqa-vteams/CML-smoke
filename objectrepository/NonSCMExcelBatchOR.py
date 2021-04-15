from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import random

class NonSCMExcelBatchOR:
    def __init__(self,driver = webdriver.Chrome):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.mainNavAddressLetterXpath = "//*[@id='mainNav']/li[2]/a"
        self.excelbatchOptionXpath = "//*[@id='mainNav']/li[2]/ul/li[2]/a"
        self.batchNameXpath = "//*[@id='batch_name']"
        self.mailingProfileXpath = "//*[@id='mailing_profile_id']"
        self.mailClassXpath = "//*[@id='mailing_profile_id']"
        self.containerXpath = "//*[@id='mail_container_id']"
        self.envelopeWeightXpath = "//*[@id='mail_page_id']"
        self.dateAdvanceXpath = "//*[@id='date_advance']"
        self.cassXpath = "//*[@id='date_advance']"
        self.mergedPDFCheckXpath = "//*[@id='merge_pdf']"
        self.printCustomCheckXpath = "//*[@id='print_custom_field1']"
        self.inputFirmCheckXpath = "//*[@id='print_custom_field1']"
        self.uploadFileXpath = "//*[@id='file']"
        self.nextToStep2Xpath = "//*[@id='step-1']/div/div/div[23]/div/div/button"
        self.nextToStep3Xpath = "//*[@id='step-2']/div[2]/div/div/button"
        self.proceedBtnXpath = "//*[@id='save']"
        self.confirmProceedXpath = "/html/body/div[5]/div/div[3]/button[1]"
        self.refreshBtnXpath = "/html/body/div[1]/div[1]/div/div/div/a"
        self.queueXpath = "/html/body/div[1]/div[1]/div/div/div/div[1]"
        self.batchNameGridXpath = "//*[@id='gridBody']/table/tbody/tr[1]/td[2]"

    def inputValues(self,name):
        elementNavToAddressList = self.driver.find_element(By.XPATH, self.mainNavAddressLetterXpath)
        self.action.move_to_element(elementNavToAddressList).perform()
        elementExcelBatch = self.driver.find_element(By.XPATH, self.excelbatchOptionXpath)
        elementExcelBatch.click()
        time.sleep(3)
        elementBatchName = self.driver.find_element(By.XPATH,self.batchNameXpath)
        elementBatchName.send_keys(name)
        elementMailingProfile = Select(self.driver.find_element(By.XPATH,self.mailingProfileXpath))
        elementMailingProfile.select_by_index(3)
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, 300);")

