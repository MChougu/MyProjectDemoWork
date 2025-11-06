from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()

wait = WebDriverWait(driver, 10)
username_input = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
username_input.send_keys("Admin")
# driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin")
Password= driver.find_element(By.XPATH, "//input[@placeholder='Password']")
Password.send_keys("admin123")
click_onLoginButton= driver.find_element(By.XPATH, "//button[@type='submit']")
click_onLoginButton.click()
time.sleep(2)
