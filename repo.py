from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#https://github.com/

#setup webdriver
class r:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    
    def go(self):
        self.driver.get(self.url)



        
test = r("https://github.com/")
test.go()