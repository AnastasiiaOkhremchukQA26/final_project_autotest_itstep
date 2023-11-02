from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    FEEDBACK = (By.XPATH, "//a[text()='Обратная связь']")
    DELIVERY = (By.XPATH, "//a[text()='Доставка']")
    WARRANTY = (By.XPATH, "//a[text()='Гарантия']")
    PHONE = (By.XPATH, "//*[text()='+38 098 911 95 22']")
    CURRENCY = (By.XPATH, "//select[@id='currency']")
    CURRENCY_UAH = (By.XPATH, "//select[@id='currency']/option[text()='UAH']")
    CURRENCY_USD = (By.XPATH, "//select[@id='currency']/option[text()='USD']")
    CURRENCY_EUR = (By.XPATH, "//select[@id='currency']/option[text()='EUR']")
    LOGO_DESK = (By.XPATH, "//div[@class='logo logo-desk']/a/img")
    LOGO_MOB = (By.XPATH, "//div[@class='logo logo-mob']/a/img")
    SEARCH = (By.XPATH, "//*[@id='typeahead']")
    SUBMIT = (By.XPATH, "//div[@class='header_search']//button")
    WISH = (By.XPATH, "//div[contains(@class, 'wishlist')]/div[@class='wishlist_icon']/a/img")
    CART = (By.XPATH, "//div[@class='cart']//div[@class='cart_icon']/a/img")
    HITS = (By.XPATH, "//a[span='Хиты']")
    DISCOUNTS = (By.XPATH, "//a[span='Скидки']")
    NEW_ITEMS = (By.XPATH, "//a[span='Новинки']")
    SAMSUNG_CAT = (By.XPATH, "//div[text() = 'Samsung']")
    SAMSUNG_J701 = (By.XPATH, "//a[text() = 'Samsung J701']")
    SUBSCRIBE = (By.XPATH, "//button[text()='Подписаться!']")
    INPUT_SUBSCRIBE = (By.XPATH, "//input[@name='submail']")
    LOGO_FOOTER = (By.XPATH, "//img[@src='images/logo-footer.png']")




