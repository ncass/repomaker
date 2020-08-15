from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#https://github.com/

#setup webdriver
class r:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    
    #method to take github url and setup repo
    def go(self):
        self.driver.get(self.url)
        self.usrname = self.driver.find_element_by_id("login_field").send_keys("/")
        self.pwd = self.driver.find_element_by_id("password").send_keys("/")
        self.signin = self.driver.find_element_by_name("commit").click()



        
test = r("https://github.com/login")
test.go()