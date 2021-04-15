from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class AddAdressOR:

    def __init__(self,driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.managementXpath = "//*[@id='mainNav']/li[4]/a"
        self.addressBookXpath = "//*[@id='mainNav']/li[4]/ul/li[1]/a"
        self.addAddressBtnXpath = "//*[@id='add']"
        self.nametxtXpath = "//*[@id='name']"
        self.addresstxtXpath = "//*[@id='address1']"
        self.citytxtXpath = "//*[@id='city']"
        self.statdrpXpath = "//*[@id='state']"
        self.ziptxtXpath = "//*[@id='zip']"
        self.saveBtnXpath = "//*[@id='address-book-add']/div/div/div[10]/div[2]/button"
        self.addressTableXpath = "//*[@id='gridBody']/table/tbody"

    def addAddress(self,name,address1, city, state, zip):
        elementManagementMainNav = self.driver.find_element(By.XPATH,self.managementXpath)
        self.action.move_to_element(elementManagementMainNav).perform()
        time.sleep(2)
        elementAddressBookTab = self.driver.find_element(By.XPATH, self.addressBookXpath)
        elementAddressBookTab.click()
        time.sleep(2)
        elementAddAddressBtn = self.driver.find_element(By.XPATH, self.addAddressBtnXpath)
        elementAddAddressBtn.click()
        time.sleep(1)
        elementName = self.driver.find_element(By.XPATH, self.nametxtXpath)
        elementName.send_keys(name)
        elementAddress1 = self.driver.find_element(By.XPATH, self.addresstxtXpath)
        elementAddress1.send_keys(address1)
        elementCity = self.driver.find_element(By.XPATH, self.citytxtXpath)
        elementCity.send_keys(city)
        elementState = Select(self.driver.find_element(By.XPATH, self.statdrpXpath))
        elementState.select_by_value(state)
        elementZip = self.driver.find_element(By.XPATH, self.ziptxtXpath)
        elementZip.send_keys(zip)
        self.driver.execute_script("window.scrollTo(0, 300);")
        elementSaveBtn = self.driver.find_element(By.XPATH, self.saveBtnXpath)
        elementSaveBtn.click()
        time.sleep(3)


    def verifyAddress(self,name):
        self.driver.execute_script("window.scrollTo(0, 500);")
        elementTable = self.driver.find_element(By.XPATH, self.addressTableXpath)
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
