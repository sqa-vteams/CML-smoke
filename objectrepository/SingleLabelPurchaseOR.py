from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import random

class SingleLabelPurchase:
        def __init__(self,driver = webdriver.Chrome):
            self.driver = driver
            self.action = ActionChains(self.driver)
            self.navToAddressLetterXpath = "//*[@id='mainNav']/li[2]/a"
            self.singleLabelOption = "//*[@id='mainNav']/li[2]/ul/li[1]/a"
            self.selectProfile = "//*[@id='mailing_profile_id']"
            self.nextBtnStep1 = "//*[@id='step-1']/div/div/div[7]/div/div/button"
            self.companyNameStep2 = "//*[@id='to_company']"
            self.toNameStep2 = "//*[@id='to_name']"
            self.toAddres1Step2 = "//*[@id='to_address1']"
            self.toCity = "//*[@id='to_city']"
            self.toState = "//*[@id='to_state']"
            self.toZip = "//*[@id='to_zip']"
            self.turnOffCass = "//*[@id='turn_off_address_verification']"
            self.printLabelRef = "//*[@id='print_label_reference']"
            self.addToAddressCheck = "//*[@id='add_to_addressbook']"
            self.labelRefTxt = "//*[@id='customs_no']"
            self.nextBtnStep2 = "//*[@id='step-2']/div/div/div[11]/div/div/button[2]"
            self.mailClassStep3 = "//*[@id='mail_service_id']"
            self.containerStep3 = "//*[@id='mail_container_id']"
            self.weightStep3 = "//*[@id='mail_page_id']"
            self.purchaseBtn = "//*[@id='purchase']"
            self.confirmPurchase = "/html/body/div[5]/div/div[3]/button[1]"
            self.picNumbTxt = "/html/body/div[1]/div[1]/div/div/div/div/h4"

        def navToSingleLabel(self, name, add1, city, state, zip, refText):
            elementAddressLetter = self.driver.find_element(By.XPATH, self.navToAddressLetterXpath)
            self.action.move_to_element(elementAddressLetter).perform()
            elementSingleLabel = self.driver.find_element(By.XPATH, self.singleLabelOption)
            elementSingleLabel.click()
            time.sleep(2)
            elementSelectProfile =Select( self.driver.find_element(By.XPATH, self.selectProfile))
            elementSelectProfile.select_by_visible_text("Mailing Profile - ZIp 4")
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, 300);")
            elementStep1Next = self.driver.find_element(By.XPATH, self.nextBtnStep1)
            elementStep1Next.click()
            time.sleep(1)
            elementToName = self.driver.find_element(By.XPATH, self.toNameStep2)
            elementToName.send_keys(name)
            elementToAddress = self.driver.find_element(By.XPATH, self.toAddres1Step2)
            elementToAddress.send_keys(add1)
            self.driver.execute_script("window.scrollTo(0, 600);")
            elementCity = self.driver.find_element(By.XPATH, self.toCity)
            elementCity.send_keys(city)
            elementState = Select( self.driver.find_element(By.XPATH, self.toState))
            elementState.select_by_value(state)
            elementZip = self.driver.find_element(By.XPATH, self.toZip)
            elementZip.send_keys(zip)
            elementCheckAddAddress = self.driver.find_element(By.XPATH, self.addToAddressCheck)
            elementCheckAddAddress.click()
            elementCheckCass = self.driver.find_element(By.XPATH, self.turnOffCass)
            #elementCheckCass.click()
            elementCheckPrintRef = self.driver.find_element(By.XPATH, self.printLabelRef)
            #elementCheckPrintRef.click()
            elementLabelRef = self.driver.find_element(By.XPATH, self.labelRefTxt)
            elementLabelRef.send_keys(refText)
            elementNextToStep3 = self.driver.find_element(By.XPATH, self.nextBtnStep2)
            elementNextToStep3.click()
            time.sleep(2)
            elementMailClass = Select(self.driver.find_element(By.XPATH, self.mailClassStep3))
            elementMailClass.select_by_index(random.randrange(0, len(elementMailClass.options)-1))
            time.sleep(1)
            elementContainer = Select(self.driver.find_element(By.XPATH, self.containerStep3))
            elementContainer.select_by_index(random.randrange(0, len(elementContainer.options)-1))
            self.driver.execute_script("window.scrollTo(0, 600);")
            elementPurchaseBtn = self.driver.find_element(By.XPATH, self.purchaseBtn)
            elementPurchaseBtn.click()
            time.sleep(1)
            elementConfirmPurchase = self.driver.find_element(By.XPATH, self.confirmPurchase)
            elementConfirmPurchase.click()
            time.sleep(10)



        def verifyLabel(self):
            elementPic = self.driver.find_element(By.XPATH, self.picNumbTxt)
            if elementPic.is_displayed():
                return True
            else:
                return False







