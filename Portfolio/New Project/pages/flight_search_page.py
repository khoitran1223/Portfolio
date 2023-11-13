from selenium.webdriver.common.by import By

class FlightSearchPage():
    def __init__(self, driver):
        self.driver = driver

    def Find_stops(self,stop):
        ChuyenBay = ["Chuyến bay thẳng","1 điểm dừng","2 điểm dừng"]
        for tempt in ChuyenBay:
            if tempt == stop:
                continue
            self.driver.find_element(By.XPATH,f"//span[contains(text(), '{tempt}')]").click()