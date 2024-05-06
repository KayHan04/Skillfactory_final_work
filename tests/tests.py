from Pages.auth_pages import SearchHelper
import time
from Pages.Base_pages import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест входа в личный кабинет через почту
def test_enter_lk_with_valid_data(browser, email_data, password_data):
    enter_lk = SearchHelper(browser)
    enter_lk.go_to_site()
    enter_lk.click_on_button_email()
    enter_lk.enter_username(email_data[0])
    enter_lk.enter_pass(password_data[0])
    enter_lk.click_on_search_button_enter()
    enter_lk.button_exit()
    assert enter_lk.main_url_lk() == "https://b2c.passport.rt.ru/account_b2c/page?state=39865372-26c6-4de5-8a52-164876235fcb&client_id=account_b2c&theme=light#/"


# Тест входа в личный кабинет через неверные данные почты
def test_enter_lk_with_error_data(browser, email_data, password_data):
    enter_lk = SearchHelper(browser)
    enter_lk.go_to_site()
    enter_lk.click_on_button_email()
    enter_lk.enter_username(email_data[1])
    enter_lk.enter_pass(password_data[0])
    enter_lk.click_on_search_button_enter()
    assert enter_lk.main_url_enter() == 'https://b2c.passport.rt.ru/auth'


# !!!!!!!!!!!!!!!!!!!!!!!!!!!! Обновление страницы, через нажатие по логотипу 'Ростелеком' в хедере
def test_refresh_header(browser):
    refresh = SearchHelper(browser)
    refresh.go_to_site()
    refresh.click_logo_header()
    time.sleep(1)


# Вход в личный кабинет через номер телефона
def test_enter_with_valid_phone(browser, password_data, phone_number_data):
    enter_phone = SearchHelper(browser)
    enter_phone.go_to_site()
    enter_phone.enter_username(phone_number_data[0])
    enter_phone.enter_pass(password_data[0])
    enter_phone.click_on_search_button_enter()
    enter_phone.button_exit()
    assert enter_phone.main_url_lk() == "https://b2c.passport.rt.ru/account_b2c/page?state=39865372-26c6-4de5-8a52-164876235fcb&client_id=account_b2c&theme=light#/"


# Сценарий восстановления пароля
def test_forgot_password(browser):
    test = SearchHelper(browser)
    test.go_to_site()
    test.button_forgot_password()
    time.sleep(5)


# Сценарий регистрации пользователя
def test_register_acc(browser, email_data, password_data, first_name_data, last_name_data, region_data):
    register = SearchHelper(browser)
    register.go_to_site()
    register.click_on_button_register_first_str()
    register.enter_first_name(first_name_data[0])
    register.enter_last_name(last_name_data[0])
    register.enter_region(region_data[0])
    register.enter_email_for_register(email_data[0])
    register.enter_pass(password_data[0])
    register.enter_check_pass(password_data[0])
    register.click_register_button()
    assert register.main_url_lk() == "https://b2c.passport.rt.ru/account_b2c/page?state=39865372-26c6-4de5-8a52-164876235fcb&client_id=account_b2c&theme=light#/"


# Тест BQa-0008 таб аутентификации при вводе почты, таб автоматически меняется на "почта"
def test_auth_email(browser, email_data, password_data):
    tab_auth = SearchHelper(browser)
    tab_auth.go_to_site()
    tab_auth.enter_username(email_data[0])
    tab_auth.enter_pass(password_data[0])
    tab_auth.click_on_search_button_enter()
    tab_auth.button_exit()
    assert tab_auth.main_url_lk() == "https://b2c.passport.rt.ru/account_b2c/page?state=39865372-26c6-4de5-8a52-164876235fcb&client_id=account_b2c&theme=light#/"


# Тест BQa-0009 таб аутентификации, при вводе номера телефона, таб автоматически меняется на "почта"
def test_tab_auth_phone(browser, phone_number_data, password_data):
    tab_auth = SearchHelper(browser)
    tab_auth.go_to_site()
    tab_auth.click_on_button_email()
    tab_auth.enter_username(phone_number_data[0])
    tab_auth.enter_pass(password_data[0])
    tab_auth.click_on_search_button_enter()
    tab_auth.button_exit()
    assert tab_auth.main_url_lk() == "https://b2c.passport.rt.ru/account_b2c/page?state=39865372-26c6-4de5-8a52-164876235fcb&client_id=account_b2c&theme=light#/"


# Тест на принятие кириллицы поля "имя", с использованием англ. символов при регистрации
def test_register_name_english(browser, first_name_data):
    reg_name = SearchHelper(browser)
    reg_name.go_to_site()
    reg_name.click_on_button_register_first_str()
    reg_name.enter_first_name(first_name_data[4])
    reg_name.click_register_button()
    assert reg_name.error_first_name() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


#  Тест на принятие кириллицы поля "имя", с использованием цифр при регистрации
def test_register_name_numbers(browser, first_name_data):
    reg_name = SearchHelper(browser)
    reg_name.go_to_site()
    reg_name.click_on_button_register_first_str()
    reg_name.enter_first_name(first_name_data[5])
    reg_name.click_register_button()
    assert reg_name.error_first_name() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


#  Тест на принятие кириллицы поля "имя", с использованием 31 сивола (кирилица)
def test_register_name_numbers_1(browser, first_name_data):
    reg_name = SearchHelper(browser)
    reg_name.go_to_site()
    reg_name.click_on_button_register_first_str()
    reg_name.enter_first_name(first_name_data[7])
    reg_name.click_register_button()
    assert reg_name.error_first_name() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


#  Тест на принятие кириллицы поля "имя", с использованием 1 сивола (кирилица)
def test_register_name_number_2(browser, first_name_data):
    reg_name = SearchHelper(browser)
    reg_name.go_to_site()
    reg_name.click_on_button_register_first_str()
    reg_name.enter_first_name(first_name_data[8])
    reg_name.click_register_button()
    assert reg_name.error_first_name() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# Тест, поля "имя" при регистрации, на возможность ввода символов "Ан-", кириллица.
def test_register_first_name_cyr(browser, first_name_data):
    reg_name = SearchHelper(browser)
    reg_name.go_to_site()
    reg_name.click_on_button_register_first_str()
    reg_name.enter_first_name(first_name_data[6])
    assert reg_name.value_first_name() == "Ан-"


# Тест, поля "фамилия" при регистрации, на возможность ввода символов "Ан-", кириллица.
def test_register_last_name_cyr(browser, last_name_data):
    reg_name = SearchHelper(browser)
    reg_name.go_to_site()
    reg_name.click_on_button_register_first_str()
    reg_name.enter_last_name(last_name_data[9])
    assert reg_name.value_last_name() != "Ан-"


# Тест поля "фамилия" при регистрации, используя англ. символы
def test_register_name_numbers_3(browser, last_name_data):
    reg_name = SearchHelper(browser)
    reg_name.go_to_site()
    reg_name.click_on_button_register_first_str()
    reg_name.enter_last_name(last_name_data[5])
    reg_name.click_register_button()
    assert reg_name.error_text_last_name() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# Тест поля "фамилия" при регистрации, используя цифры
def test_register_name_numbers_4(browser, last_name_data):
    reg_name = SearchHelper(browser)
    reg_name.go_to_site()
    reg_name.click_on_button_register_first_str()
    reg_name.enter_last_name(last_name_data[6])
    reg_name.click_register_button()
    assert reg_name.error_text_last_name() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# Тест поля "фамилия" при регистрации, используя 31 символ (кирилица)
def test_register_name_cyr_30_sybl(browser, last_name_data):
    reg_name = SearchHelper(browser)
    reg_name.go_to_site()
    reg_name.click_on_button_register_first_str()
    reg_name.enter_last_name(last_name_data[7])
    reg_name.click_register_button()
    assert reg_name.error_text_last_name() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# Тест поля "фамилия" при регистрации, используя 1 символ (кирилица)
def test_register_name_cyr_1_sybl(browser, last_name_data):
    reg_name = SearchHelper(browser)
    reg_name.go_to_site()
    reg_name.click_on_button_register_first_str()
    reg_name.enter_last_name(last_name_data[8])
    reg_name.click_register_button()
    assert reg_name.error_text_last_name() == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


# Тест поля "Пароль" при регистрации, используя 7 цифр
def test_register_password_1(browser, password_data):
    reg_pass = SearchHelper(browser)
    reg_pass.go_to_site()
    reg_pass.click_on_button_register_first_str()
    reg_pass.enter_pass(password_data[4])
    reg_pass.click_register_button()
    assert reg_pass.error_text_password() == "Длина пароля должна быть не менее 8 символов"


# !!!!!!!Тест поля "Пароль" при регистрации, используя 7 цифр и одну заглавную букву A
def test_register_password_2(browser, password_data):
    reg_pass = SearchHelper(browser)
    reg_pass.go_to_site()
    reg_pass.click_on_button_register_first_str()
    reg_pass.enter_pass(password_data[5])
    reg_pass.click_register_button()
    assert reg_pass.error_text_password() == "Длина пароля должна быть не менее 8 символов"


# Тест поля "email(номер телефона)" при регистрации, почта не содержит часть ...@mail.ru/@yandex.ru
def test_register_email_or_phone_with_eremail(browser, email_data):
    reg_email = SearchHelper(browser)
    reg_email.go_to_site()
    reg_email.click_on_button_register_first_str()
    reg_email.enter_email_for_register(email_data[4])
    reg_email.click_register_button()
    assert reg_email.error_text_email_or_phone() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


# Тест поля "email(номер телефона)" при регистрации, номер телефона содержит 12 символов (формат +7ХХХХХХХХХХ)
def test_register_email_or_phone_with_erphone_1(browser, phone_number_data):
    reg_phone = SearchHelper(browser)
    reg_phone.go_to_site()
    reg_phone.click_on_button_register_first_str()
    reg_phone.enter_email_for_register(phone_number_data[5])
    reg_phone.click_register_button()
    assert reg_phone.error_text_email_or_phone() == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


# Тест поля "email(номер телефона)" при регистрации, номер телефона содержит 10 символов (формат +7ХХХХХХХХХ)
def test_register_email_or_phone_with_erphone_2(browser, phone_number_data):
    reg_phone = SearchHelper(browser)
    reg_phone.go_to_site()
    reg_phone.click_on_button_register_first_str()
    reg_phone.enter_email_for_register(phone_number_data[6])
    reg_phone.click_register_button()
    assert reg_phone.error_text_email_or_phone() != "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


# Тест входа в личный кабинет через яндекс почту
def test_yandex_social_med(browser):
    soc_ya = SearchHelper(browser)
    soc_ya.go_to_site()
    soc_ya.yandex_email_social_med()
    soc_ya.wait_vis()
    soc_ya.button_exit()
    assert soc_ya.main_url_lk() == ("https://b2c.passport.rt.ru/account_b2c/page?"
                                    "state=39865372-26c6-4de5-8a52-164876235fcb&client_id=account_b2c&theme=light#/")


# Тест кликабельности социальных сетей
def test_social_meds(browser):
    s_med = SearchHelper(browser)
    s_med.go_to_site()
    s_med.click_VK()
    browser.back()
    s_med.click_school()
    browser.back()
    time.sleep(3)
    s_med.click_mail_ru()
    browser.back()
    s_med.yandex_email_social_med()
    browser.back()
    assert s_med.base_url == "https://b2c.passport.rt.ru/auth"

#  Тест кликабельности кнопки "Помощь"
def test_help_button(browser):
    help_but = SearchHelper(browser)
    help_but.go_to_site()
    help_but.click_button_help()
    assert help_but.url_help == ("https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https:"
                                 "//b2c.passport.rt.ru/account_b2c/login&response_"
                                 "type=code&scope=openid&state=bedbc671-8f26-4e47-9a18-f0672f67384b&theme&auth_type")

# Тест кликабельности кнопки "пользовательское соглашение"
def test_users_aggremnt(browser):
    user_ag = SearchHelper(browser)
    user_ag.go_to_site()
    user_ag.click_button_user_aggrement()
    assert user_ag.url_use_aggrement == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"
