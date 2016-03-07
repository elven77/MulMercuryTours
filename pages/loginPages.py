import basePages
from locators.locators import HomeLogin


class Login(basePages.BasePage):
    def login(self,username,password):
        # Input username
        elemUsername=self.driver.find_element(*HomeLogin.elemUsername)
        elemUsername.send_keys(username)

        # Input password
        elemPwd=self.driver.find_element(*HomeLogin.elemPwd)
        elemPwd.send_keys(password)

        # Confirm
        elemSignIn=self.driver.find_element(*HomeLogin.elemSignIn)
        self.mouse_click(elemSignIn)