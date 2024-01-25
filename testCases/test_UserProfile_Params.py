import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.UserProfilePage import UserProfile_Class
from utilities.readproperties import Readconfig


class Test_User_Profile_Params:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()

    def test_UserLogin_Params_005(self, setup, getDataForLogin):
        self.driver = setup
        self.driver.get(self.LoginUrl)
        self.ur = UserProfile_Class(self.driver)
        self.ur.Enter_Email(getDataForLogin[0])
        print("Username-->" + getDataForLogin[0])
        self.ur.Enter_Password(getDataForLogin[1])
        print("Password-->" + getDataForLogin[1])
        self.ur.Click_Login_Or_RegisterButton()
        if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot(
                    "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_Pass.png")

                assert True
            elif getDataForLogin[2] == "Fail":
                self.driver.save_screenshot(
                    "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_Pass.png")
                assert False

        else:
            if getDataForLogin[2] == "Pass":
                self.driver.save_screenshot(
                    "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_Pass.png")

                assert False
            elif getDataForLogin[2] == "Fail":
                self.driver.save_screenshot(
                    "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_Pass.png")
                assert True

            self.driver.save_screenshot(
                "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_Fail.png")
