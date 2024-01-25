from selenium.webdriver.common.by import By


class VerifyOrderAmount_Class:
    Click_AppleMocBook_XPath = (By.XPATH, "//h3[normalize-space()='Apple Macbook Pro']")
    Click_AddToCart_XPath = (By.XPATH, "//input[@value='Add to Cart']")
    Click_ContinueSHopping_XPath = (By.XPATH, "//a[@class='btn btn-primary btn-lg']")
    Click_AppleIPad_XPath = (By.XPATH, "//h3[normalize-space()='Apple iPad Retina']")
    Click_HeadPhone_XPath = (By.XPATH, "//h3[normalize-space()='Headphones']")

    def __init__(self, driver):
        self.driver = driver

    def Click_AppleMocBook(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_AppleMocBook_XPath).click()

    def Click_AppleIPad(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_AppleIPad_XPath).click()

    def Click_HeadPhone(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_HeadPhone_XPath).click()

    def Click_AddToCart(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_AddToCart_XPath).click()

    def Click_ContinueShoppingButton(self):
        self.driver.find_element(*VerifyOrderAmount_Class.Click_ContinueSHopping_XPath).click()

    def Validate_Amount(self):

        l = len(self.driver.find_elements(By.CSS_SELECTOR, "tbody tr"))

        Price_List = []
        for r in range(1, l - 2):
            Var = self.driver.find_element(By.CSS_SELECTOR,
                                           "tbody tr:nth-child(" + str(r) + ") td:nth-child(4)").text
            Product_Price = (Var[1:])
            Price_List.append(float(Product_Price))

        var2 = sum(Price_List)
        Exp_SubTotal = round(var2, 2)
        Exp_Tax = round((Exp_SubTotal * 0.13), 2)
        Exp_Total = Exp_SubTotal + Exp_Tax
        Amount_List = []
        for r in range(l - 2, l + 1):
            Var = self.driver.find_element(By.CSS_SELECTOR, "tbody tr:nth-child(" + str(r) + ") td:nth-child(4)").text
            var2 = (Var[1:])
            Amounts = var2.replace(',', '')
            Amount_List.append(float(Amounts))

        Act_SubTotal = Amount_List[0]
        Act_Tax = Amount_List[1]
        Act_Total = Amount_List[2]
        print("Exp_SubTotal" + str(Exp_SubTotal))
        print("Act_SubTotal" + str(Act_SubTotal))
        print("Exp_Tax" + str(Exp_Tax))
        print("Act_Tax" + str(Act_Tax))
        print("Exp_Total" + str(Exp_Total))
        print("Act_Total" + str(Act_Total))
        if Exp_SubTotal == Act_SubTotal and Exp_Tax == Act_Tax and Exp_Total == Act_Total:
            print("Amount is Matched")
            return "Amount is Matched"
        else:
            print("Amount is Not Matched")
            return "Amount is Not Matched"
