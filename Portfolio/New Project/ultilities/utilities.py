class Ultis():
    def assertFlight(self,list,value):
        for stop1 in list:
            assert stop1.text == value
