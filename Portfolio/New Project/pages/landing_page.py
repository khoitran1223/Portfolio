import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

class LandingPage():
     def __init__(self,driver,wait):
        self.driver = driver
        self.wait = wait

     def DepartureFrom(self,DepartureLocation):
        self.driver.find_element(By.XPATH,"//input[@location='departure']").click()
        DepartureFrom = self.driver.find_element(By.XPATH,"//input[@class='ftl-location-mobile']")
        DepartureFrom.send_keys(DepartureLocation)
        HCM = self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='ftl-search-geocode ftl-modal ftl-open'])//div[1]")))
        HCM.click()
     def Location(self,Location):
        #chon noi den
        DepartureTo = self.driver.find_element(By.XPATH,"//input[@location='arrived']")
        DepartureTo.click()
        time.sleep(2)
        DepartureTo.send_keys(Location)
        PUS = self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//div[@class='ftl-search-geocode ftl-modal ftl-open'])//div[1]")))
        PUS.click()

     def TicketQuantities(self,Tikets):
        #So ve
        for x in range(Tikets):
            x = self.driver.find_element(By.XPATH,"//ul[@type='adt']//i[@class='fa fa-plus-square-o ftl-active']")
            x.click()

     def Date(self,DepartureDate):
        #ngay
        self.driver.find_element(By.XPATH,"//input[@id='ftl-date-departure']").click()
        #Valid_day = driver.find_element(By.XPATH,"//td[@class='day']//label[@class='cld'][normalize-space()]").text
        today = datetime.today()
        Day_of_today = today.day
        Departure_Date = datetime.strptime(DepartureDate, "%Y/%m/%d")
        Selected_Date = Departure_Date.day

        if Day_of_today <= Selected_Date:
            XPATH = f"(//label[@class='cld'][normalize-space()='{Selected_Date}'])"
            self.driver.find_element(By.XPATH,XPATH).click()
        else:
            print("Xin chon lai ngay")

     def ClickSearch(self):
         # Tim chuyen bay
         self.driver.find_element(By.XPATH, "//button[contains(text(),'TÌM KIẾM CHUYẾN BAY')]").click()

     def All_flights (self, type, locator ):
         list_of_all_flight = self.driver.find_elements(type, locator)
         return list_of_all_flight