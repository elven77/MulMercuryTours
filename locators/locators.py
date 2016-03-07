from selenium.webdriver.common.by import By


class baseLocators():
    pass


class SignOn(baseLocators):
    elemSignOn=(By.XPATH,"//td[@class='mouseOut']")
    elemUserName=(By.XPATH,"//input[@name='userName']")
    elemPwd=(By.XPATH,"//input[@name='password']")
    elemSubmit=(By.XPATH,"//input[@name='login']")

class FlightInfo(baseLocators):
    # Choose person number
    elemPersonNum=(By.XPATH,"//select[@name='passCount']")

    # Choose departing city
    elemDepart=(By.XPATH,"//select[@name='fromPort']")

    # Choose departing date
    elemDepartMonth=(By.XPATH,"//select[@name='fromMonth']")
    elemDepartDay=(By.XPATH,"//select[@name='fromDay']")

    # Choose Desination
    elemDestination=(By.XPATH,"//select[@name='toPort']")

    # Choose arrive date
    elemReturnMonth=(By.XPATH,"//select[@name='toMonth']")
    elemReturnDay=(By.XPATH,"//select[@name='toDay']")

    # Choose class
    elemBusinessClass=(By.XPATH,"//input[@value='Business']")

    # Choose airline
    elemAirline=(By.XPATH,"//select[@name='airline']")

    # Confirm
    elemFindFlight=(By.XPATH,"//input[@name='findFlights']")


class ChooseFlight(baseLocators):
    elemDepartFlight=(By.XPATH,"//input[@value='Unified Airlines$363$281$11:24']")
    #elemReturnFlight=(By.XPATH,"//input[@value='Blue Skies Airlines$631$273$14:30']")
    elemReturnFlight=(By.XPATH,"//input[@value={0}]")
    #elemReturnFlight=(By.XPATH,"//input[contains(@value,'14:30')]")
    elemSaveFlight=(By.XPATH,"//input[@name='reserveFlights']")

class BookFlight(baseLocators):
    elemTicketlessTravel=(By.XPATH,"//input[@name='ticketLess']")
    #elemFirstName=(By.XPATH,"//input[@name='passFirst0']")
    #elemLastName=(By.XPATH,"//input[@name='passLast0']")
    elemNumber=(By.XPATH,"//input[@name='creditnumber']")
    elemBuyFlight=(By.XPATH,"//input[@name='buyFlights']")

class Logout(baseLocators):
    elemLogout=(By.XPATH,"//a[@href='mercurysignoff.php']")

class BuyObj(baseLocators):
    elemCartBuy = (By.XPATH, "//div[@class='btn bt-primary size-s buy normal']")
    elemSize = (By.XPATH, "//div[@data-value='4']")

class RegisterObj(baseLocators):
    elemRegisterEntry=(By.PARTIAL_LINK_TEXT,"REGISTER")
    #elemRegisterEntry=(By.XPATH,"//a[@href='mercuryregister.php?osCsid=46d4e1b5537ca0e9622a5cdc7082a1d3']")
    elemEmail=(By.XPATH,"//input[@name='email']")
    elemPwd=(By.XPATH,"//input[@name='password']")
    elemConfirmPwd=(By.XPATH,"//input[@name='confirmPassword']")
    elemRegister=(By.XPATH,"//input[@name='register']")

class HomeLogin(baseLocators):
    elemUsername=(By.XPATH,"//input[@name='userName']")
    elemPwd=(By.XPATH,"//input[@name='password']")
    elemSignIn=(By.XPATH,"//input[@name='login']")

class Profile(baseLocators):
    elemFirstName=(By.XPATH,"//input[@name='firstName']")
    elemLastName=(By.XPATH,"//input[@name='lastName']")
    elemPhone=(By.XPATH,"//input[@name='phone']")
    elemEmail=(By.XPATH,"//input[@name='email']")
    elemaddr=(By.XPATH,"//input[@name='address1']")
    elemCity=(By.XPATH,"//input[@name='city']")
    elemState=(By.XPATH,"//input[@name='state']")
    elemPostCode=(By.XPATH,"//input[@name='postalCode']")
    elemCountry=(By.XPATH,"//select[@name='country']")
    elemSubmit=(By.XPATH,"//img[@src='images/profile_submit.gif']")

class AfterLogin(baseLocators):
    elemProfile=(By.LINK_TEXT,"PROFILE")
    #elemProfile=(By.XPATH,"//td[@class='mouseOut']")