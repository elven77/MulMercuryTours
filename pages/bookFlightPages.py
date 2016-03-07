from selenium.webdriver.common.by import By
import selenium.webdriver
import basePages
from locators.locators import BookFlight
from testData.passengersInfo import PassengersInfo


class BookFlightPages(basePages.BasePage):
    def fillPersonalInfo(self,nameSet,number):
        """
        # First name
        elemFirstName=self.driver.find_element(*BookFlight.elemFirstName)
        elemFirstName.send_keys(firstname)

        # Last name
        elemLastName=self.driver.find_element(*BookFlight.elemLastName)
        elemLastName.send_keys(lastname)
        """

        for i,p in enumerate(nameSet):
            # Locators
            firstnamelocator="//input[@name='passFirst{0}']".format(i)
            lastnamelocator="//input[@name='passLast{0}']".format(i)
            self.driver.find_element(By.XPATH,firstnamelocator).send_keys(p['firstname'])
            self.driver.find_element(By.XPATH,lastnamelocator).send_keys(p['lastname'])

        # Credit card number
        elemNumber=self.driver.find_element(*BookFlight.elemNumber)
        elemNumber.send_keys(number)

    def purchase(self):
        elemBuyFlight=self.driver.find_element(*BookFlight.elemBuyFlight)
        self.mouse_click(elemBuyFlight)