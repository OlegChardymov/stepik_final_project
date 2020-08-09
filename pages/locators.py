from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGOUT_LINK = (By.CSS_SELECTOR, "#logout_link")
    BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini .btn-group .btn:first-child")
    # should be first on page ^
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    MAIN_LINK = "http://selenium1py.pythonanywhere.com/"


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REG_PASS = (By.CSS_SELECTOR, "[name='registration-password1']")
    REG_CONF_PASS = (By.CSS_SELECTOR, "[name='registration-password2']")
    REG_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_NAME = (By.CSS_SELECTOR, "#messages .alert:first-child .alertinner strong")
    # should be first on page ^
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner p strong")


class BasketPageLocators():
    BASKET_SUMMARY = (By.CSS_SELECTOR, "form.basket_summary")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    # if no element for "your basket is empty" text then basket is not empty, presumably ^
