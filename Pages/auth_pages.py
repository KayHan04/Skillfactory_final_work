from selenium.webdriver.common.by import By
from Pages.Base_pages import BasePage
from selenium.webdriver.common.action_chains import ActionChains


# Класс локаторов
class Yasearchlocators:
    LOCATOR_ROSTELEKOM_SEARCH_USERNAME = (By.ID, "username")
    LOCATOR_ROSTELEKOM_SEARCH_PASS = (By.ID, "password")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_ENTER = (By.ID, "kc-login")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_EMAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_LS = (By.ID, "t-btn-tab-ls")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_REGISTER = (By.ID, "kc-register")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_FIRSTNAME = (
        By.XPATH,
        "/html[1]/body[1]/div[1]/main[1]/section[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_LASTNAME = (
        By.XPATH,
        "/html[1]/body[1]/div[1]/main[1]/section[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_REGION = (
        By.XPATH, "//*[@id='page-right']/div/div/div/form/div[2]/div/div/input")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_EMAIL_REGISTER = (By.ID, "address")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_CHECK_PASS = (By.ID, "password-confirm")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_FIND_BUTTTON_REGISTER = (By.XPATH, "//*[@id='page-right']/div/div/div/form/button")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_FIND_BUTTTON_LOGO_HEADER = (By.CSS_SELECTOR, "#app-header > div > div > svg")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_FORGOT_PASSWORD = (By.ID, "forgot_password")
    LOCATOR_ROSTELEKOM_SEARCH_BUTTON_EXIT = (By.ID, "logout-btn")
    LOCATOR_ROSTELEKOM_SEARCH_ERROR_TEXT_FIRST_NAME = (
    By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]")
    LOCATOR_ROSTELEKOM_SEARCH_VALUE_FISRT_NAME_AT_REGISTER = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[1]/div[1]/div/div[1]")
    LOCATOR_ROSTELEKOM_SEARCH_VALUE_LAST_NAME_AT_REGISTER = (By.XPATH, "//*[@id='page-right']/div/div/div/form/div[1]/div[2]/div/div[1]")
    LOCATOR_ROSTELEKOM_SEARCH_ERROR_TEXT_LAST_NAME = (
    By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[2]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]")
    LOCATOR_ROSTELEKOM_SEARCH_ERROR_TEXT_PASSWORD = (
    By.XPATH, "/html[1]/body[1]/div[1]/main[1]/section[2]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]")
    LOCATOR_ROSTELEKOM_SEARCH_ERROR_TEXT_EMAIL_OR_PHONE = (
    By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")
    LOCATOR_ROSTELEKOM_SEARCH_YANDEX_EMAIL_SOCIAL = (By.XPATH, "//a[@id='oidc_ya']")
    LOCATOR_ROSTELEKOM_SEARCH_VK_SOCIAL = (By.XPATH, "//a[@id='oidc_vk']")
    LOCATOR_ROSTELEKOM_SEARCH_SCHOOL_SOCIAL = (By.XPATH, "//a[@id='oidc_ok']")
    LOCATOR_ROSTELEKOM_SEARCH_MAIL_SOCIAL = (By.XPATH, "//a[@id='oidc_mail']")

    LOCATOR_ROSTELEKOM_SEARCH_USERNAME_MAIN_LK = (By.XPATH, "//body/div[@id='app']/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]")

class SearchHelper(BasePage):


    # Поле ввода номера телефона/почты/логина/лицевого счета
    def enter_username(self, username):
        search_filed = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_USERNAME)
        search_filed.click()
        search_filed.send_keys(username)
        return search_filed

    # Поле вводе пароля
    def enter_pass(self, password):
        search_filed = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_PASS)
        search_filed.click()
        search_filed.send_keys(password)
        return search_filed

    # Поле проверки пароля при регистрации
    def enter_check_pass(self, check_pass):
        search_check_pass = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_CHECK_PASS)
        search_check_pass.click()
        search_check_pass.send_keys(check_pass)
        return search_check_pass

    # Клик кнопки входа на странице входа в личного кабинета
    def click_on_search_button_enter(self):
        return self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_ENTER).click()

    # Выбор авторизации через почту
    def click_on_button_email(self):
        return self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_EMAIL).click()

    # Выбор авторизации через логин
    def click_on_button_login(self):
        return self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_LOGIN).click()

    # Выбор авторизации через лицевой счет
    def click_on_button_ls(self):
        return self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_LS).click()

    # Клик кнопки регистрации, при регистрации
    def click_on_button_register_first_str(self):
        return self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_REGISTER).click()

    # Ввода имени при регистрации
    def enter_first_name(self, firstname):
        search_firstname = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_FIRSTNAME)
        search_firstname.clear()
        search_firstname.click()
        search_firstname.send_keys(firstname)
        return search_firstname

    # Значение вводимое в поле "имя"
    def value_first_name(self):
        value = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_VALUE_FISRT_NAME_AT_REGISTER).text
        return value

    def value_last_name(self):
        value = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_VALUE_LAST_NAME_AT_REGISTER).text
        return value

    # Ввода фамилии при регистрации
    def enter_last_name(self, lastname):
        search_lastname = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_LASTNAME)
        search_lastname.clear()
        search_lastname.click()
        search_lastname.send_keys(lastname)
        return search_lastname

    # Ввода региона при регистрации
    def enter_region(self, region):
        search_region = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_REGION)
        search_region.clear()
        search_region.send_keys(region)
        return search_region

    # Ввода почты при регистрации
    def enter_email_for_register(self, email_register):
        search_email_register = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_EMAIL_REGISTER)
        search_email_register.click()
        search_email_register.clear()
        search_email_register.send_keys(email_register)
        return search_email_register

    # Клик кнопки "зарегистрироваться" при регистрации
    def click_register_button(self):
        search_button = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_FIND_BUTTTON_REGISTER)
        search_button.click()
        return search_button

    # Клик по логотипу ростелеком в хедере главной страницы
    def click_logo_header(self):
        search_button = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_FIND_BUTTTON_LOGO_HEADER)
        search_button.click()
        return search_button

    # URL страницы авторизации
    def main_url_enter(self):
        correct_base_url = self.base_url
        return correct_base_url

    # URL личного кабинета
    def main_url_lk(self):
        url_lk = self.url_lk
        return url_lk

    # Кнопка 'забыл пароль' на странице авторизации
    def button_forgot_password(self):
        forgot_pass = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_FORGOT_PASSWORD)
        forgot_pass.click()
        return forgot_pass

    # Кнопка 'выйти' из аккаунта в личном кабинете
    def button_exit(self):
        exit_btn = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_BUTTON_EXIT)
        exit_btn.click()
        return exit_btn

    # Текст ошибки при вводе в поле "имя"
    def error_first_name(self):
        error_text = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_ERROR_TEXT_FIRST_NAME).text
        return error_text

    #  Текст ошибки при вводе в поле "фамилия"
    def error_text_last_name(self):
        error_text = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_ERROR_TEXT_LAST_NAME).text
        return error_text

    # Текст ошибки при вводе в поле "пароль"
    def error_text_password(self):
        error_text = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_ERROR_TEXT_PASSWORD)
        return error_text

    # Текст ошибки при вводе поля "Email или телефон"
    def error_text_email_or_phone(self):
        error_text = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_ERROR_TEXT_EMAIL_OR_PHONE).text
        return error_text

    # Кнопка "Яндекс" на странице авторизации
    def yandex_email_social_med(self):
        sm = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_YANDEX_EMAIL_SOCIAL).click()
        return sm

    # Имя фамилия в личном кабинете
    def user_name_for_lk(self):
        um = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_USERNAME_MAIN_LK)
        return um

    # Клик по кнопке VK на странице авторизации, через соц сети
    def click_VK(self):
        vk = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_VK_SOCIAL).click()
        return vk

    # Клик по кнопку "Одноклассники" на странице авторизации, через соц сети
    def click_school(self):
        sc = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_SCHOOL_SOCIAL).click()
        return sc

    # Клик по кнопку "Майл.ру" на странице авторизации, через соц сети
    def click_mail_ru(self):
        mrc = self.find_element(Yasearchlocators.LOCATOR_ROSTELEKOM_SEARCH_MAIL_SOCIAL).click()
        return mrc

