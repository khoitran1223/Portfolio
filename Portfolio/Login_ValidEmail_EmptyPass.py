from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def Login_ValidMail_EmptyPassword():
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-notifications')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.vemaybay.vn/")
    Login_Or_Signin = driver.find_element(By.XPATH,"//span[contains(text(),'Đăng nhập hoặc đăng ký')]")
    Login_Or_Signin.click()
    Login = driver.find_element(By.XPATH,"//a[@class='btn btn-block btn-vmb register-button btn-warning my-3']")
    Login.click()
    Email = driver.find_element(By.ID,"LoginEmail")
    Email.click()
    Email.send_keys("portfolio.automation.testing@gmail.com")
    
    CheckBox = driver.find_element(By.XPATH,"//label[contains(text(),'Ghi nhớ')]")
    CheckBox.click()
    LogInButton = driver.find_element(By.XPATH,"//button[contains(text(),'Đăng nhập')]")
    LogInButton.click()

    timestamp = int(time.time()) 
    screenshot_filename = f"D:\\Automated Traveloka\\FailCases\\Invalid_Email_{timestamp}.png"
    
    capture = driver.find_element(By.XPATH, "//div[@class='row justify-content-center align-items-center']")
    capture.screenshot(screenshot_filename)
    Invalid_Notification = driver.find_element(By.XPATH,"//span[@class='field-validation-error message-error text-danger my-4 d-block']").text
    print(Invalid_Notification)
    driver.close()
