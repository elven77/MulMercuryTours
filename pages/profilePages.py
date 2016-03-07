from Tix import Select
import basePages
from locators.locators import Profile
from selenium.webdriver.support.ui import Select


class EditProfilePages(basePages.BasePage):
    def fillName(self,firstname,lastname):
        elemFName=self.driver.find_element(*Profile.elemFirstName)
        elemFName.send_keys(firstname)

        elemLName=self.driver.find_element(*Profile.elemLastName)
        elemLName.send_keys(lastname)

    def fillPhone(self,phone):
        elemPhone=self.driver.find_element(*Profile.elemPhone)
        elemPhone.send_keys(phone)

    def fillEmail(self,email):
        elemEmail=self.driver.find_element(*Profile.elemEmail)
        elemEmail.send_keys(email)

    def fillAddress(self,address):
        elemAddr=self.driver.find_element(*Profile.elemaddr)
        elemAddr.send_keys(address)

    def fillCity(self,city):
        elemCity=self.driver.find_element(*Profile.elemCity)
        elemCity.send_keys(city)

    def fillState(self,state):
        elemState=self.driver.find_element(*Profile.elemState)
        elemState.send_keys(state)

    def fillPostcode(self,postcode):
        elemPostcode=self.driver.find_element(*Profile.elemPostCode)
        elemPostcode.send_keys(postcode)

    def fillCountry(self,country):
        elemCountry=Select(self.driver.find_element(*Profile.elemCountry))
        elemCountry.select_by_visible_text(country)

    def fillContactInfo(self,firstname,lastname,phone,email):
        self.fillName(firstname,lastname)
        self.fillPhone(phone)
        self.fillEmail(email)

    def fillMailingInfo(self,address,city,state,postcode,country):
        self.fillAddress(address)
        self.fillCity(city)
        self.fillState(state)
        self.fillPostcode(postcode)
        self.fillCountry(country)

    def submit(self):
        elemSubmit=self.driver.find_element(*Profile.elemSubmit)
        self.mouse_click(elemSubmit)