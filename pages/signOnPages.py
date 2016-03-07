import time
import basePages
from locators.locators import SignOn


class SignOnPage(basePages.BasePage):
    def enterSignOn(self):
        elemEnterSignon=self.driver.find_element(*SignOn.elemSignOn)
        self.mouse_click(elemEnterSignon)

    def inputSignInfo(self,username,pwd):
        elemUserName=self.driver.find_element(*SignOn.elemUserName)
        elemPwd=self.driver.find_element(*SignOn.elemPwd)
        elemUserName.send_keys(username)
        elemPwd.send_keys(pwd)

    def submit(self):
        elemSubmit=self.driver.find_element(*SignOn.elemSubmit)
        self.mouse_click(elemSubmit)
        #elemSubmit.click()