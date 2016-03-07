import basePages
from locators.locators import Logout


class LogOutPage(basePages.BasePage):
    def logOut(self):
        elemLogout=self.driver.find_element(*Logout.elemLogout)
        self.mouse_click(elemLogout)