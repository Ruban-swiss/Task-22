from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class GuviInsta:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(20)

    def quit(self):
        self.driver.quit()
        
    def getNumberOfPosts(self):
        xpath = '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[1]/button/span/span'
        return self.driver.find_element(by=By.XPATH, value=xpath).text
    
    def getNumberOfFollowers(self):
        xpath=' /html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span'
        return self.driver.find_element(by=By.XPATH, value=xpath).text
    
    
    def getNumberOfFollowing(self):
        xpath=' /html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span'
        return self.driver.find_element(by=By.XPATH, value=xpath).text
    
    
url = "https://www.instagram.com/guviofficial/"
obj = GuviInsta(url)
obj.boot()
print(obj.getNumberOfPosts())
print(obj.getNumberOfFollowers())
print(obj.getNumberOfFollowing())
obj.quit()
    
     