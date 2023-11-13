import time
from selenium.webdriver.common.by import By
from pages.landing_page import LandingPage
from pages.flight_search_page import FlightSearchPage
from ultilities.utilities import Ultis
import pytest
@pytest.mark.usefixtures("setup")
class Testflight():
    def test_Flight(self):
        lp = LandingPage(self.driver,self.wait)
        fsp = FlightSearchPage(self.driver)
        ut = Ultis()

        lp.DepartureFrom(DepartureLocation="SGN")
        lp.Location(Location="PPUS")
        lp.TicketQuantities(Tikets=4)
        lp.Date(DepartureDate="2023/11/23")
        lp.ClickSearch()
        fsp.Find_stops("2 điểm dừng")
        all_flight = lp.All_flights(By.XPATH, "(//div[@class='ftl-flight-segment'])")
        print(len(all_flight))
        ut.assertFlight(all_flight,"2 điểm dừng")

        time.sleep(10)
