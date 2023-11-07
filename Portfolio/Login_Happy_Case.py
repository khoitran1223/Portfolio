from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Login():
    def Login_Happy_Case(self):
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service, options=options)

        driver.get("https://www.vemaybay.vn/")
        driver.fullscreen_window()
        Login_Or_Signin = driver.find_element(By.XPATH,"//span[contains(text(),'Đăng nhập hoặc đăng ký')]")
        Login_Or_Signin.click()
        Login = driver.find_element(By.XPATH,"//a[@class='btn btn-block btn-vmb register-button btn-warning my-3']")
        Login.click()
        Email = driver.find_element(By.ID,"LoginEmail")
        Email.click()
        Email.send_keys("portfolio.automation.testing@gmail.com")
        Pass = driver.find_element(By.ID,"LoginPassword")
        Pass.click()
        Pass.send_keys("0829627549")
        CheckBox = driver.find_element(By.XPATH,"//label[contains(text(),'Ghi nhớ')]")
        CheckBox.click()
        LogInButton = driver.find_element(By.XPATH,"//button[contains(text(),'Đăng nhập')]")
        LogInButton.click()
        driver.close()

chaythudemo = Login()
chaythudemo.Login_Happy_Case()