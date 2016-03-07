import basePages
from locators.locators import AfterLogin


class AfterLoginPages(basePages.BasePage):
    def goToProfile(self):
        elemProfile=self.driver.find_element(*AfterLogin.elemProfile)
        self.mouse_click(elemProfile)