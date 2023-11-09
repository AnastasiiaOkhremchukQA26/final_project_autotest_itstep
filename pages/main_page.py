from ..pages import base_page, locators
import inspect

class MainPage(base_page.BasePage):
    def is_button_login(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_feedback(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
            "Button feedback is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_delivery(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.DELIVERY), \
            "Button delivery is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_warranty(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.WARRANTY), \
            "Button warranty is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_phone(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "Button phone is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_currency(self):
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
            "Button currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_uah(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_UAH), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_usd(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_USD), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_eur(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY_EUR), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
