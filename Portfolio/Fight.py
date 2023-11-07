from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime

class Demo():
    def Flight(self):
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-notifications')
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service=service, options=options)
        wait = WebDriverWait(driver,20)
        driver.get("https://www.vemaybay.vn/")
        #Chon noi di
        driver.find_element(By.XPATH,"//input[@location='departure']").click()
        DepartureFrom = driver.find_element(By.XPATH,"//input[@class='ftl-location-mobile']")
        DepartureFrom.send_keys("Ho ")
        HCM = wait.until(EC.element_to_be_clickable((By.XPATH,"//b[normalize-space()='SGN']")))
        HCM.click()
        #chon noi den
        DepartureTo = driver.find_element(By.XPATH,"//input[@location='arrived']")
        DepartureTo.click()
        DepartureTo.send_keys("PUS")
        PUS = wait.until(EC.element_to_be_clickable((By.XPATH,"//b[normalize-space()='PUS']")))
        PUS.click()

        #So ve
        for x in range(3):
            x = driver.find_element(By.XPATH,"//ul[@type='adt']//i[@class='fa fa-plus-square-o ftl-active']")
            x.click()
        
        #ngay
        driver.find_element(By.XPATH,"//input[@id='ftl-date-departure']").click()
        #Valid_day = driver.find_element(By.XPATH,"//td[@class='day']//label[@class='cld'][normalize-space()]").text
        present = datetime.datetime.today()
        #cai nay la hard code chon ngay 10
        day = 11
        SelectedDate = datetime.datetime(datetime.datetime.now().year,datetime.datetime.now().month,day)
        if present < SelectedDate:
            XPATH = f"(//label[@class='cld'][normalize-space()='{day}'])"
            driver.find_element(By.XPATH,XPATH).click()
        else:
            print("Xin chon lai ngay")

        #Tim chuyen bay
        driver.find_element(By.XPATH,"//button[contains(text(),'TÌM KIẾM CHUYẾN BAY')]").click()
        all_flight = driver.find_elements(By.XPATH,"(//div[@class='ftl-flight-segment'])")
        print(len(all_flight))
        for stop1 in all_flight:
            if stop1.text == "Bay thẳng":
                print(stop1.text)

ChayDemo = Demo()
ChayDemo.Flight()

