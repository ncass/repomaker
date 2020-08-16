from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys

#setup webdriver
class r:
    def __init__(self, rname, description):
        self.url = "https://github.com/login"
        self.rname = rname
        self.description = description
        self.driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    
    #method to take github url and setup repo
    def go(self):
        self.driver.get(self.url)
        self.usrname = self.driver.find_element_by_id("login_field").send_keys("ncass")
        self.pwd = self.driver.find_element_by_id("password").send_keys("nickroks45")
        self.signin = self.driver.find_element_by_name("commit").click()
        self.create = self.driver.find_element_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a").click()
        self.repo = self.driver.find_element_by_id("repository_name").send_keys(self.rname)
        self.desc = self.driver.find_element_by_id("repository_description").send_keys(self.description)
        self.submit = self.driver.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").click()
    
    def quit(self):
        self.driver.close()

if __name__ == "__main__":
    nr = r(str(sys.argv[1]), str(sys.argv[2]))
    nr.go()
    nr.quit()

    #method to create a local folder to connect to this repo
    os.chdir("/Users/nicholascassara/Desktop")
    os.system("mkdir "+ nr.rname)
    os.chdir("/Users/nicholascassara/Desktop/"+nr.rname)
    os.system("git init")
    os.system("git remote add origin https://github.com/ncass/"+nr.rname+".git")
    