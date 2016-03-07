import baseTest
from pages.afterLoginPages import AfterLoginPages
from pages.loginPages import Login
from pages.profilePages import EditProfilePages


class EditProfile(baseTest.BaseTest):
    def test_edit_profile(self):
        elemLogin=Login(self.driver)
        elemLogin.login("aaa","aaa")

        # Go to Profile
        elemAfterLogin=AfterLoginPages(self.driver)
        elemAfterLogin.goToProfile()

        # Edit profile
        elemEditProfile=EditProfilePages(self.driver)
        elemEditProfile.fillContactInfo("Elven","Zhao","77777777","elven77@163.com")
        elemEditProfile.fillMailingInfo("abc","guiyang","Guizhou","777777","AUSTRALIA")
        elemEditProfile.submit()