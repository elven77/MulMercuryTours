from selenium.webdriver.common.by import By
import basePages
from locators.locators import ChooseFlight


class SelectFlight(basePages.BasePage):
    def departFlight(self):
        elemDepartFlight=self.driver.find_element(*ChooseFlight.elemDepartFlight)
        elemDepartFlight.click()

    def returnFlight(self,keyword):
        ReturnFlightLocator="//input[contains(@value,'{0}')]".format(keyword)
        elemReturnFlight=self.driver.find_element(By.XPATH,ReturnFlightLocator)
        elemReturnFlight.click()

    def saveFlight(self):
        elemSaveFlight=self.driver.find_element(*ChooseFlight.elemSaveFlight)
        self.mouse_click(elemSaveFlight)