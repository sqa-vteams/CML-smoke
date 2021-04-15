from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class AddMailingProfileOR:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.managementXpath = "//*[@id='mainNav']/li[4]/a"
        self.mailingProfileXpath = "//*[@id='mainNav']/li[4]/ul/li[4]/a"
        self.addMailingBtnXpath = "//*[@id='add']"
        self.profileNameTxtXpath = "//*[@id='profile_name']"
        self.address1TxtXpath = "//*[@id='address1']"
        self.cityTxtXpath = "//*[@id='city']"
        self.stateDrpXpath = "//*[@id='state']"
        self.zipTxtXpath = "//*[@id='zip']"
        self.phoneTxtXpath = "//*[@id='phone']"
        self.checkScanXpath = "//*[@id='use_scan_address']"
        self.scanNameXpath = "//*[@id='scan_name']"
        self.scanAddressXpath = "//*[@id='scan_address']"
        self.scanCityXpath = "//*[@id='scan_city']"
        self.scanStatDrpXpath = "//*[@id='scan_state']"
        self.scanZipTxtXpath = "//*[@id='scan_zip']"
        self.addMailBtnXpath = "//*[@id='mailing-profile-add']/div/div/div[20]/div[2]/button"
        self.tableXpath = "//*[@id='gridBody']/table/tbody"

    def addMailingProfile(self,name,address1, city, state, zip, phone):
        elementManagementMainNav = self.driver.find_element(By.XPATH, self.managementXpath)
        self.action.move_to_element(elementManagementMainNav).perform()
        time.sleep(2)
        elementMailngProfileOpt = self.driver.find_element(By.XPATH, self.mailingProfileXpath)
        elementMailngProfileOpt.click()
        time.sleep(2)
        elementAddMailingBtn = self.driver.find_element(By.XPATH, self.addMailingBtnXpath)
        elementAddMailingBtn.click()
        time.sleep(2)
        elementProfileName = self.driver.find_element(By.XPATH, self.profileNameTxtXpath)
        elementProfileName.send_keys(name)
        elementProfileAddress1 = self.driver.find_element(By.XPATH, self.address1TxtXpath)
        elementProfileAddress1.send_keys(address1)
        elementProfileCity = self.driver.find_element(By.XPATH, self.cityTxtXpath)
        elementProfileCity.send_keys(city)
        elementProfileState = Select(self.driver.find_element(By.XPATH,self.stateDrpXpath))
        elementProfileState.select_by_value(state)
        elementProfileZip = self.driver.find_element(By.XPATH, self.zipTxtXpath)
        elementProfileZip.send_keys(zip)
        self.driver.execute_script("window.scrollTo(0, 300);")
        elementProfilePhone = self.driver.find_element(By.XPATH, self.phoneTxtXpath)
        elementProfilePhone.send_keys(phone)
        self.driver.execute_script("window.scrollTo(0, 1000);")
        elementProfileAddBtn = self.driver.find_element(By.XPATH, self.addMailBtnXpath)
        elementProfileAddBtn.click()
        time.sleep(2)

    def verifyMailingProfile(self,name):
        self.driver.execute_script("window.scrollTo(0, 500);")
        elementTable = self.driver.find_element(By.XPATH, self.tableXpath)
        rows = elementTable.find_elements(By.TAG_NAME, "tr")
        print("Total Number of rows are:" + str(len(rows)))
        coloumns = elementTable.find_elements(By.XPATH, "//tr[1]/td")
        print("Total Number of coloumns are:" + str(len(coloumns)))
        found = False
        for i in range(1, len(rows)):
            for j in range(1, len(coloumns)):

                if name in elementTable.find_element(By.XPATH, "//tr[" + str(i) + "]/td[" + str(j) + "]").text:
                    found = True
                    break

                else:
                    found = False

            if found == True:
                break

        return found
