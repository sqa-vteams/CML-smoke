from selenium import webdriver
from selenium.webdriver.support.ui import Select
class RegisterationOR:
    def __init__(self , driver ):
        self.driver = driver
        self.fname_id = "first_name"
        self.lname_name = "last_name"
        self.company_id = "company"
        self.address1_id = "address1"
        self.address2_id = "address2"
        self.city_id = "city"
        self.state_name = "state"
        self.zip_id = "zip"
        self.zip4_id = "zip4"
        self.phone_id = "phone"
        self.email_id = "email"
        self.password_id = "password"
        self.cnfpassword_id = "password_confirmation"
        self.registerbtn_xpath = "//*[@id='register']/div[13]/div/button"
        self.registerLink_xpath = "//*[@id='topNav']/li[2]/a"
        self.checkAgree = "agree"

    def navToRegisterPage(self):
        element = self.driver.find_element_by_xpath(self.registerLink_xpath)
        element.click()
    def setname(self, fname, lname):
        element1 = self.driver.find_element_by_id(self.fname_id)
        element2 = self.driver.find_element_by_name(self.lname_name)
        element1.send_keys(fname)
        element2.send_keys(lname)

    def setaddress(self, add1, city, state, zip ):
        elementAddress1 = self.driver.find_element_by_id(self.address1_id)
       # elementAddress2 = self.driver.find_element_by_id(self.address2_id)
        elementCity = self.driver.find_element_by_id(self.city_id)
        elementstate = Select( self.driver.find_element_by_name(self.state_name))
        elementzip = self.driver.find_element_by_id(self.zip_id)
       # elementzip4 = self.driver.find_element_by_id(self.zip4_id)
        elementAddress1.send_keys(add1)
       # elementAddress2.send_keys(add2)
        elementCity.send_keys(city)
        elementstate.select_by_value(state)
        elementzip.send_keys(zip)
        #elementzip4.send_keys(zip4)



    def setemailpass(self, email, pass1):
        elementemail = self.driver.find_element_by_id(self.email_id)
        elementpassword = self.driver.find_element_by_id(self.password_id)
        elementconfpass = self.driver.find_element_by_name(self.cnfpassword_id)
        elementemail.clear()
        elementpassword.clear()
        elementemail.send_keys(email)
        elementpassword.send_keys(pass1)
        elementconfpass.send_keys(pass1)

    def checkAgreeBox(self):
        elementCheck = self.driver.find_element_by_id(self.checkAgree)
        elementCheck.click()

    def clickRegister(self):
        elementRegisterBtn = self.driver.find_element_by_xpath(self.registerbtn_xpath)
        elementRegisterBtn.click()

    def getTitle(self):
        title = self.driver.title

        if "Dashboard" in title:
            return True
        else:
            return False
