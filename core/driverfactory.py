from selenium import webdriverSelenium
from appium import webdriverAppium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import os
from appium.webdriver.common.mobileby import MobileBy


class DriverFactory():

    @property
    driver = None

    @property
    dc = {}

    def getDriver(self):
        if(self.driver==None):
            createTestObjectDriver(self)
        else:
            return self.driver    


    def createDriver(self):        
        self.dc['platformVersion'] = '7.0'
        self.dc['deviceName'] = 'Android Emulator'
        #self.dc['appPackage'] = 'br.org.sidi.technicalreport'
        #self.dc['appActivity'] = '.features.profile.view.LoginActivity'
        self.dc['platformName'] = 'Android'
        self.dc['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), self.apkPath))
        
        try:
           self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)
        except EnvironmentError as error:
           print_exception("Error:", error)

        self.driver.implicitly_wait(10)

    
