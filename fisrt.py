from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Firefox Driver ka path
service = Service("C:\\DRIVERS\\geckodriver-v0.35.0-win64\\geckodriver.exe")

# Firefox WebDriver ko initialize karein
driver = webdriver.Firefox(service=service)

# Open the website
driver.get("https://opensource-demo.orangehrmlive.com/")
    

driver.find_element_by_name("username").send_keys("Admin")
driver.find_element_by_name("password").send_keys("admin123")
driver.find_element_by_class("oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()

act_title=driver.title
exp_title="OrangeHRM"


if act_title==exp_title:
    print("Test Case Pass")
else:
    print("Test case Failed")
    