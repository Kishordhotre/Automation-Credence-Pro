import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import utilities
from pageObjects.UserProfilePage import UserProfile_Class
from utilities import ExcelFileOperation
from utilities.readproperties import Readconfig
from utilities.Logger import Logging_Class


class Test_User_Profile_DDT:
    LoginUrl = Readconfig.getLoginUrl()
    RegistrationUrl = Readconfig.getRegistrationUrl()
    Username = Readconfig.getUsername()
    Password = Readconfig.getPassword()
    path = "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\testCases\\TestData\\Excel Worksheet.xlsx"
    log = Logging_Class.log_genarator()


    def test_UserLogin_ddt_006(self, setup):
        self.log.info("The Test_UserLogin_ddt_006 started ")
        self.driver = setup
        self.log.info("Opening Browser")
        self.ur = UserProfile_Class(self.driver)
        self.rows = ExcelFileOperation.rows_count(self.path, 'Sheet1')
        print(self.rows)
        Result_List = []
        for r in range(2, self.rows + 1):
            self.email = ExcelFileOperation.ReadData(self.path, 'Sheet1', r, 1)
            self.password = ExcelFileOperation.ReadData(self.path, 'Sheet1', r, 2)
            self.Exp_Result = ExcelFileOperation.ReadData(self.path, 'Sheet1', r, 3)
            self.driver.get(self.LoginUrl)
            self.ur.Enter_Email(self.email)
            print("Username-->" + self.email)
            self.ur.Enter_Password(self.password)
            print("Password-->" + self.password)
            self.ur.Click_Login_Or_RegisterButton()
            if self.ur.Validate_Login_Or_Registration() == "Login or Registration Pass":
                if self.Exp_Result == "Pass":
                    Result_List.append("Pass")
                    ExcelFileOperation.WriteData(self.path, 'Sheet1', r, 4, "Pass")
                    self.driver.save_screenshot(
                        "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_pass.png")
                    self.driver.find_element(By.XPATH, "//a[@role='button']").click()
                    self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

                elif self.Exp_Result == "Fail":
                    Result_List.append("Fail")
                    ExcelFileOperation.WriteData(self.path, 'Sheet1', r, 4, "Pass")
                    self.driver.save_screenshot(
                        "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_pass.png")
                    self.driver.find_element(By.XPATH, "//a[@role='button']").click()
                    self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()

            else:
                if self.Exp_Result == "Pass":
                    Result_List.append("Fail")
                    ExcelFileOperation.WriteData(self.path, 'Sheet1', r, 4, "Fail")
                    self.driver.save_screenshot(
                        "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_pass.png")

                elif self.Exp_Result == "Fail":
                    Result_List.append("Pass")
                    ExcelFileOperation.WriteData(self.path, 'Sheet1', r, 4, "Fail")
                    self.driver.save_screenshot(
                        "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_pass.png")

                self.driver.save_screenshot(
                    "C:\\Users\\Dell\\PycharmProjects\\Pytest_Frame\\Screenshots\\Login_fail.png")

        print(Result_List)
        if "Fail" in Result_List:
            assert True
        else:
            assert False
