import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
HeadLess_Option =webdriver.ChromeOptions()
HeadLess_Option.add_argument("headLess")
class Test_Pytest:
    def test_OrangeHRM_006(self):
        driver= webdriver.Chrome(options= HeadLess_Option)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(4)
        ##enter username
        # driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        #Enter pswd
        # driver.find_element(By.NAME,"").send_keys("admin123")
        driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(3)
        #click on login
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        # LOgout
        ## Click to dropdown
        driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
        time.sleep(2)
        #Click on Logout
        driver.find_element(By.XPATH,"//a[normalize-space()='Logout']")
        time.sleep(2)
        ##### You can explore TestCaseStudio--- selectorhubs--- just add in your browser.

    def test_Amazon_GetRandom_Items_007(self):
        driver = webdriver.Chrome(options= HeadLess_Option)
        driver.get("https://www.amazon.in/")
        driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("women kurties")
        driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
        l = len(driver.find_elements(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div'))
        print(l)
        RandomNum = random.randint(1, l + 1)
        driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[' + str(
            RandomNum) + "]").click()
        time.sleep(4)
        print("Page Title is", driver.title)
        print("selected Item No is: ", RandomNum)
