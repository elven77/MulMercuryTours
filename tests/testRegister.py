import baseTest
from pages.registerPages import Register


class Register(baseTest.BaseTest):
    def test_register(self):
        print "test register"
        register = Register(self.driver)
        register.beginRegister()
        register.fillRegInfo("aaa","aaa","aaa")
        register.confirmRegister()