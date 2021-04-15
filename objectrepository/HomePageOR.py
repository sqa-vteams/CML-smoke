from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


class HomePageOR:
    def __init__(self, driver):
        self.driver = driver
        self.linksListXPATH = "/html/body/div/div[1]/div/div/div/div/div[2]/aside/ul/li[1]/a"
        self.logoCMLXPATH = "//*[@id='header']/div/div[2]/div/div[1]/div/div/a"
        self.mainNavXPATH = "//*[@id='topNav']/li[1]/a"
        self.getStartLink = "/html/body/div[1]/div[1]/div/div/div/div/div[2]/aside/h2[1]/a"
        self.blogLinksXPATH = "//h4/a"



    def clickLinks(self):
        elementLinkList = self.driver.find_elements(self, By.XPATH,self.linksListXPATH)
        for element in elementLinkList:
            element.click()

    def clickGetStarted(self):
        elementGetStartedLink = self.driver.find_element(By.XPATH,self.getStartLink)
        elementGetStartedLink.click()
        time.sleep(3)
        if self.driver.current_url in "https://test.certifiedmaillabels.com/register":
            return True
        else:
            return False

    def clickCMLLogo(self):
        elementLogo = self.driver.find_element(By.XPATH,self.logoCMLXPATH)
        elementLogo.click()

        if self.driver.current_url == "https://test.certifiedmaillabels.com/":
            return True
        else:
            return False

    def getBlogLinks(self):
        self.driver.execute_script("window.scrollTo(0,  1500);")
        time.sleep(3)
        blogLinks = self.driver.find_elements(By.XPATH,self.blogLinksXPATH)
        x = len(blogLinks)
        if x==3:
            return True
        else:
            return False




