import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.UserProfilePage import UserProfile_Class
from utilities.readproperties import Readconfig
from utilities.Logger import Logging_Class


class Test_User_Profile:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    log = Logging_Class.log_genarator()

    def test_UserRegistration_001(self, setup):
        self.log.info("test_UserRegistration_001 is started")
        self.driver = setup
        self.log.info(" Opening Browser")
        self.ur = UserProfile_Class(self.driver)
        self.driver.get(self.RegistrationUrl)
        self.log.info("Going to Url-->" + self.RegistrationUrl)
        self.ur.Enter_Name("Rohit")
        self.log.info("Entering the name")

        email = Generate_Email()
        self.ur.Enter_Email(email)
        self.log.info("Entering the Email-->" + email)

        self.ur.Enter_Password("Test123")
        self.log.info("Entering the password")

        self.ur.Enter_ConfirmPassword("Test123")
        self.log.info("Entering the confirm password")
        self.ur.Click_Login_Or_RegisterButton()
        self.log.info("Clicking on Register Button")

        if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
            self.log.info("test_UserRegistration_001 is pass")
            self.driver.save_screenshot(
                "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_Pass.png")
            assert True
        else:
            self.log.info("test_UserRegistration_001 is fail")
            self.driver.save_screenshot(
                "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_Pass.png")

            assert False
        self.log.info("test_UserRegistration_001 is completed")

    def test_UserLogin_002(self, setup):
        self.driver = setup

        self.driver.get(self.LoginUrl)
        self.ur = UserProfile_Class(self.driver)

        self.ur.Enter_Email(self.Username)

        self.ur.Enter_Password(self.Password)

        self.ur.Click_Login_Or_RegisterButton()

        if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
            self.driver.save_screenshot(
                "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_Pass.png")

            # self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_Pass.png")

            assert False


def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase, k=4))
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
    return f"{username}@{domain}"
