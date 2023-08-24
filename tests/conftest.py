import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def email_data():
    valid_email = 'Uchebask@yandex.ru'
    sec_email = 'Uchebaskqw@yandex.ru'
    th_email = 'AndreiKondratev104@yandex.ru'
    fou_email = 'vasya9678@yandex.ru'
    fiv_email = 'pupa327'
    return valid_email, sec_email,th_email,fou_email,fiv_email


@pytest.fixture(scope='session')
def password_data():
    valid_pass = 'uchebaK12'
    sec_pass = 'uch123'
    th_pass = 'unitA322'
    fou_pass = '1234ht'
    fiv_pass = '1234567'
    six_pass = '1234567A'
    return valid_pass,sec_pass,th_pass,fou_pass,fiv_pass,six_pass

@pytest.fixture(scope='session')
def phone_number_data():
    valid_phone = '9277555567'
    sec_phone = '9275555678'
    th_phone = '9275678246'
    fou_phone = '9679688720'
    fiv_phone = '9679567801'
    six_phone = '927755556875'
    sev_phone = '927766631'
    eth_phone = '375957395849'
    return valid_phone,sec_phone,th_phone,fou_phone,fiv_phone,six_phone,sev_phone,eth_phone

@pytest.fixture(scope='session')
def first_name_data():
    fst_name = 'Иван'
    sec_name = 'Андрей'
    th_name = 'Зина'
    fou_name = 'Саша'
    fiv_name = 'Andrey'
    six_name = '23585'
    # Кирилица
    sev_name = 'Ан-'
    eth_name = 'ьииаскилдьсакьисадидклькскьааис'
    nine_name =  'с'
    return fst_name,sec_name,th_name,fou_name,fiv_name,six_name,sev_name,eth_name,nine_name

@pytest.fixture(scope='session')
def last_name_data():
    fst_name = 'Воробьев'
    sec_name = 'Иванов'
    th_name = 'Капитонова'
    fou_name = 'Сизов'
    fiv_name = 'Есипов'
    six_name = 'Kondratev'
    sev_name = '23585'
    eth_name = 'ваоввИвиИсовттИоИвоводааапдневн'
    nine_name = 'е'
    ten_name = 'Ан-'
    return fst_name,sec_name,th_name,fou_name,fiv_name,six_name, sev_name,eth_name,nine_name,ten_name

@pytest.fixture(scope='session')
def region_data():
    fst_reg = 'Воронежская область'
    sec_reg = 'Ростовская область'
    th_reg = 'Саратовская область'
    fou_reg = 'Самарская область'
    return fst_reg,sec_reg,th_reg,fou_reg

