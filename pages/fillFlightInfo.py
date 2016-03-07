from selenium.webdriver.support.select import Select
import basePages
from locators.locators import FlightInfo


class FillFlightInfo(basePages.BasePage):
    def choosePersonNum(self,personnum):
        elemSelectPersonNum=Select(self.driver.find_element(*FlightInfo.elemPersonNum))
        elemSelectPersonNum.select_by_visible_text(personnum)

    def chooseDepartCity(self,city):
        elemDepart=Select(self.driver.find_element(*FlightInfo.elemDepart))
        elemDepart.select_by_visible_text(city)

    def chooseDepartDate(self,month,day):
        elemDepartMonth=Select(self.driver.find_element(*FlightInfo.elemDepartMonth))
        elemDepartMonth.select_by_visible_text(month)

        elemDepartDay=Select(self.driver.find_element(*FlightInfo.elemDepartDay))
        elemDepartDay.select_by_visible_text(day)

    def chooseDestination(self,destination):
        elemDestination=Select(self.driver.find_element(*FlightInfo.elemDestination))
        elemDestination.select_by_visible_text(destination)

    def chooseReturnDate(self,month,day):
        elemReturnMonth=Select(self.driver.find_element(*FlightInfo.elemReturnMonth))
        elemReturnMonth.select_by_visible_text(month)

        elemReturnDay=Select(self.driver.find_element(*FlightInfo.elemReturnDay))
        elemReturnDay.select_by_visible_text(day)

    def chooseBusinessClass(self):
        elemBusinessClass=self.driver.find_element(*FlightInfo.elemBusinessClass)
        elemBusinessClass.click()

    def chooseAirline(self,airline):
        elemAirline=Select(self.driver.find_element(*FlightInfo.elemAirline))
        elemAirline.select_by_visible_text(airline)

    def findFlight(self):
        elemSaveInfo=self.driver.find_element(*FlightInfo.elemFindFlight)
        self.mouse_click(elemSaveInfo)