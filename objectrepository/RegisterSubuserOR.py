from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class RegisterSubuserOR:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.management = "//*[@id='mainNav']/li[4]/a"
        self.navToSub = "/html/body/div[1]/header/div/div[3]/div/div/div/div/div/div/nav/ul/li[4]/ul/li[3]/a"
        self.addSubBtn = "//*[@id='add']"
        self.fNameTB = "//*[@id='first_name']"
        self.lNameTB = "//*[@id='last_name']"
        self.add1TB = "//*[@id='address1']"
        self.cityTB = "//*[@id='city']"
        self.stateDD = "//*[@id='state']"
        self.zipTB = "//*[@id='zip']"
        self.phoneTB = "//*[@id='phone']"
        self.emailTB = "//*[@id='email']"
        self.passTB = "//*[@id='password']"
        self.passCnfrmTB = "//*[@id='password_confirmation']"
        self.moneyCheck = "//*[@id='manage_payments']"
        self.mailprofileCheck = "//*[@id='manage_mailing_profiles']"
        self.editUserCheck = "//*[@id='manage_users']"
        self.postageCheck = "//*[@id='manage_refunds']"
        self.disableCheck = "//*[@id='disabled']"
        self.submitBtn = "//*[@id='user-add']/div/div/div[19]/div[2]/button"
        self.table = "//*[@id='gridBody']/table/tbody"


    def navToUser(self):
        navManagement = self.driver.find_element(By.XPATH,self.management)
        time.sleep(1)

        self.action.move_to_element(navManagement).perform()
        time.sleep(3)
        subUserOption = self.driver.find_element(By.XPATH, self.navToSub)
        subUserOption.click()


    def clickAddUser(self):
        addUser = self.driver.find_element(By.XPATH,self.addSubBtn)
        time.sleep(1)
        addUser.click()



    def submitForm(self,firstName,lastName,address,city,state,zip,phone,email,password):
        elementFirstName = self.driver.find_element(By.XPATH,self.fNameTB)
        elementLastName = self.driver.find_element(By.XPATH,self.lNameTB)
        elementAddress1 = self.driver.find_element(By.XPATH,self.add1TB)
        elementCity = self.driver.find_element(By.XPATH,self.cityTB)
        elementState = self.driver.find_element(By.XPATH,self.stateDD)
        elementZip = self.driver.find_element(By.XPATH, self.zipTB)
        elementPhone = self.driver.find_element(By.XPATH,self.phoneTB)
        elementEmail = self.driver.find_element(By.XPATH,self.emailTB)
        elementPass = self.driver.find_element(By.XPATH,self.passTB)
        elementPassCnfrm = self.driver.find_element(By.XPATH, self.passCnfrmTB)

        elementFirstName.send_keys(firstName)
        elementLastName.send_keys(lastName)
        elementAddress1.send_keys(address)
        elementCity.send_keys(city)
        dropdownstate = Select (elementState)
        self.driver.execute_script("window.scrollTo(0, 300);")
        time.sleep(2)
        dropdownstate.select_by_value(state)
        elementZip.send_keys(zip)
        elementPhone.send_keys(phone)
        elementEmail.send_keys(email)
        elementPass.send_keys(password)
        elementPassCnfrm.send_keys(password)

        self.driver.execute_script("window.scrollTo(0, 700);")
        elementMoneyCheck = self.driver.find_element(By.XPATH, self.moneyCheck)
        elementMailCheck = self.driver.find_element(By.XPATH, self.mailprofileCheck)
        elementEditCheck = self.driver.find_element(By.XPATH, self.editUserCheck)
        elementPostageCheck = self.driver.find_element(By.XPATH, self.postageCheck)
        elementSubmit = self.driver.find_element(By.XPATH, self.submitBtn)
        time.sleep(2)
        elementMoneyCheck.click()
        elementMailCheck.click()
        elementEditCheck.click()
        elementPostageCheck.click()
        elementSubmit.click()

    def verifyUser(self, value):
        self.driver.execute_script("window.scrollTo(0, 500);")
        elementTable = self.driver.find_element(By.XPATH,self.table)
        rows = elementTable.find_elements(By.TAG_NAME,"tr")
        print("Total Number of rows are:"+str(len(rows)))
        coloumns = elementTable.find_elements(By.XPATH,"//tr[1]/td")
        print("Total Number of coloumns are:" + str(len(coloumns)))
        found = False
        for i in range(1,len(rows)):
            for j in range(1,len(coloumns)):

                if value in elementTable.find_element(By.XPATH,"//tr["+str(i)+"]/td["+str(j)+"]").text:
                    found = True
                    break

                else:
                    found = False

            if found==True:
                break



        return found

