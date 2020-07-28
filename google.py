import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class google:
    def start_google(self,driver):
        driver.get("http://www.google.co.in")
    def search_google(self,driver,query):
        self.element = driver.find_element_by_name("q")
        self.element.clear()
        self.element.send_keys(query)
        time.sleep(1)
        self.element.send_keys(Keys.RETURN)
        time.sleep(1)
        #self.element = driver.find_element_by_class_name('LC20lb').click()

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome("C:/Program Files (x86)/Google/chromedriver.exe")
driver.maximize_window()
google().start_google(driver)
s = "hi"
google().search_google(driver,s)