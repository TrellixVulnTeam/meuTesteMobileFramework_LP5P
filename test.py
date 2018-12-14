import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import os
from appium.webdriver.common.mobileby import MobileBy


class Teste_Laudo(unittest.TestCase):
    dc = {}
    def setUp(self):
        self.dc['platformVersion'] = '7.0'
        self.dc['deviceName'] = 'Android Emulator'
        #self.dc['appPackage'] = 'br.org.sidi.technicalreport'
        #self.dc['appActivity'] = '.features.profile.view.LoginActivity'
        self.dc['platformName'] = 'Android'
        self.dc['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'apks\CTAppium-1-1 (1).apk'))
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.dc)

    def test_untitled(self):
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='Formulário']").click()

        #preencher nome
        self.element = self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'nome').send_keys('fernando cruz')

        #pega valor do combo
        self.comboText = self.driver.find_element(By.XPATH, "//android.widget.TextView[@resource-id='android:id/text1']").text
        print("Valor:", "\n" + self.comboText)


        #verifica valor
        #assert(self.element, "Fernando Cruz")
       
    def tearDown(self):
        self.driver.quit()
        
    if __name__ == '__main__':
        unittest.main()
