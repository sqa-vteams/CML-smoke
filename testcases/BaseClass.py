from selenium import webdriver
from objectrepository.LoginPageOR import LoginPageOR
import time
class BaseClass:

    chrompath = "E:/TestPythonCodes/SmokeTestSuiteCML/venv/chromedriver79.exe"
    url = "https://test.certifiedmaillabels.com/"


    def initDriver(self):
        self.driver = webdriver.Chrome(self.chrompath)
        self.driver.get(self.url)
        self.driver.maximize_window()
        return self.driver




    def scrollTo(self,x):
        self.driver.execute_script("window.scrollTo(0, "+x+");")

    def login(self, driver):
        self.username = "faizan.raheem@nxb.com.pk"
        self.password = "login101"
        self.loginPage = LoginPageOR(driver)
        self.loginPage.navToLogin()
        time.sleep(2)
        self.loginPage.setUserName(self.username)
        time.sleep(2)
        self.loginPage.setPassword(self.password)
        time.sleep(2)
        self.loginPage.clickSignin()
        time.sleep(2)
        assert self.loginPage.getPageTitle()
        print("User logged in successfully")
        return self.driver
