import baseTest
from pages.registerPages import Register


class TestRegister(baseTest.BaseTest):
    def test_register(self):
        register=Register(self.driver)
        register.beginRegister()
        register.fillRegInfo("aaa","aaa","aaa")
        register.confirmRegister()