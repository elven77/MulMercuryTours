import time
import string

import baseTest
from locators.locators import BookFlight
from pages import logoutPages
from pages.bookFlightPages import BookFlightPages
from pages.fillFlightInfo import FillFlightInfo
from pages.selectFlightPages import SelectFlight
from pages.signOnPages import SignOnPage
from pages.logoutPages import LogOutPage
from testData.passengersInfo import PassengersInfo


class TestSignOn(baseTest.BaseTest):
    def setUp(self):
        super(TestSignOn, self).setUp()

    def test_signon(self):
        print(time.strftime("Start: "+'%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        signOnPage=SignOnPage(self.driver)
        fillFlightInfo=FillFlightInfo(self.driver)
        selectFlight=SelectFlight(self.driver)
        bookFlight=BookFlightPages(self.driver)
        #SignOnbPage=SignOnPage(self.driver)

        # Enter Sign On
        signOnPage.enterSignOn()

        # Input Username & Pwd
        signOnPage.inputSignInfo("aaa","aaa")

        # Submit
        signOnPage.submit()

        # Find Flight & Confirm
        fillFlightInfo.choosePersonNum('2')
        fillFlightInfo.chooseDepartCity('Sydney')
        fillFlightInfo.chooseDepartDate('January','7')
        fillFlightInfo.chooseDestination('Paris')
        fillFlightInfo.chooseReturnDate('May','26')
        fillFlightInfo.chooseBusinessClass()
        fillFlightInfo.chooseAirline('Unified Airlines')
        fillFlightInfo.findFlight()

        # Save Flight
        selectFlight.departFlight()
        selectFlight.returnFlight("14:30")
        selectFlight.saveFlight()

        # Book a flight
        bookFlight.fillPersonalInfo(PassengersInfo.passenger_info,"12345678")
        bookFlight.purchase()

        # Logout
        logout=LogOutPage(self.driver)
        logout.logOut()