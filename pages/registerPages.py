import basePages
from locators.locators import RegisterObj


class Register(basePages.BasePage):
    def beginRegister(self):
        elemRegEntry=self.driver.find_element(*RegisterObj.elemRegisterEntry)
        self.mouse_click(elemRegEntry)

    def fillRegInfo(self,username,pwd,confirmPwd):
        # Input user name
        elemUsername=self.driver.find_element(*RegisterObj.elemEmail)
        elemUsername.send_keys(username)

        # Input password
        elemPwd=self.driver.find_element(*RegisterObj.elemPwd)
        elemPwd.send_keys(pwd)

        # Confirm password
        elemConfirmPwd=self.driver.find_element(*RegisterObj.elemConfirmPwd)
        elemConfirmPwd.send_keys(confirmPwd)

    def confirmRegister(self):
        elemRegister=self.driver.find_element(*RegisterObj.elemRegister)
        self.mouse_click(elemRegister)