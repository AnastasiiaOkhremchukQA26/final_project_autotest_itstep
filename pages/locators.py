from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    DETAILS = (By.XPATH, "//a[text()='Детали сотрудничества']")
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
    ALERT_SUCCESS = (By.XPATH, "//div[@id = 'alert-success']")



class MainPageLocators:
    MAIN_SLIDER = (By.XPATH, "//div[@class = 'screen_slider']")
    CAT_ZARYADKI = (By.XPATH, "//a[@href='category/zaryadki']")
    MAIN_SUBCAT = (By.XPATH, '//a[@href="category/Besprovodnye-BZU"]')

    REFUND = (By.XPATH, "(//div[@class='char_item d-flex flex-row align-items-center justify-content-start'])[1]")
    FREE_SHIPPING = (By.XPATH, "(//div[@class='char_item d-flex flex-row align-items-center justify-content-start'])[2]")
    PAYMENT_DELAY = (By.XPATH, "(//div[@class='char_item d-flex flex-row align-items-center justify-content-start'])[3]")
    TECHNICAL_SUPPORT = (By.XPATH, "(//div[@class='char_item d-flex flex-row align-items-center justify-content-start'])[4]")

    SHOW_ALL = (By.XPATH, "//a[@href='main/showNew' and contains(@class, 'view-all')]")
    LEFT = (By.XPATH, "//div[@class='arrivals_nav arrivals_prev']/i[@class='fas fa-chevron-left']")
    RIGHT = (By.XPATH, "//div[@class='arrivals_nav arrivals_next']/i[@class='fas fa-chevron-right']")
    PRODUCT_PANEL = (By.XPATH, "//div[@class='product_panel panel active']")
    XIAOMI_5A_PRIME = (By.XPATH, "(//div[@class='product_item is_new d-flex flex-column align-items-center justify-content-center text-center'])[6]")

    SHOW_HIT = (By.XPATH, "//a[@href='main/showHit' and contains(@class, 'view-all')]")
    HIT_LEFT = (By.XPATH, "//div[@class='best_prev best_nav']/i[@class='fas fa-chevron-left']")
    HIT_RIGHT = (By.XPATH, "//div[@class='best_next best_nav']/i[@class='fas fa-chevron-right']")
    HIT_PANEL = (By.XPATH, "(//div[@class='slick-list draggable'])[3]")
    HIT_MOUSE = (By.XPATH, "(//div[@class='bestsellers_item_container d-flex flex-row align-items-center justify-content-start'])[14]")

    TRENDS_LEFT = (By.XPATH, "//div[@class='trends_prev trends_nav slick-arrow']")
    TRENDS_RIGHT = (By.XPATH, "//div[@class='trends_next trends_nav slick-arrow']")
    TRENDS_AIRPODS_2 = (By.XPATH, "(//div[@class='trends_item d-flex flex-column align-items-center justify-content-center'])[11]")










