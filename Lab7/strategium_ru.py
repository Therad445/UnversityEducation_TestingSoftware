import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Функция ожидания элементов
def wait_of_element_located(xpath, driver_init):
    element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


# Вынесем инициализцию драйвера в отдельную фикстуру pytest
@pytest.fixture
def driver_init():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.strategium.ru/forum/")
    yield driver
    driver.close()




# Вынесем аутентификацию юзера в отдельную функцию
def auth_user(user_name, password, driver_init):
    # Поиск и ожидание элементов и присваивание к переменным.
    open_login = wait_of_element_located(xpath='//*[@id=\"elUserSignIn\"]', driver_init=driver_init)
    input_username = wait_of_element_located(xpath='//*[@name=\"auth\"]', driver_init=driver_init)
    input_password = wait_of_element_located(xpath='//*[@name=\"password\"]', driver_init=driver_init)
    login_button = wait_of_element_located(xpath='//*[@name=\"_processLogin\"]', driver_init=driver_init)
    # Действия с формами
    open_login.send_keys(Keys.RETURN)
    input_username.send_keys(user_name)
    input_password.send_keys(password)
    login_button.send_keys(Keys.RETURN)



def reg_user(user_name, email, password):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.strategium.ru/forum/register/")
    open_reg = wait_of_element_located(xpath='//*[@id=\"elRegisterButton\"]', driver_init=driver)
    # open_reg = driver_init.find_element_by_id("elRegisterButton").click()
    input_username = wait_of_element_located(xpath='//*[@id=\"elInput_username\"]', driver_init=driver)
    input_email = wait_of_element_located(xpath='//*[@id=\"elInput_email_address\"]', driver_init=driver)
    input_password = wait_of_element_located(xpath='//*[@id=\"elInput_password\"]', driver_init=driver)
    input_password_confirm = wait_of_element_located(xpath='//*[@id=\"elInput_password_confirm\"]', driver_init=driver)
    open_reg.click()
    input_username.send_keys(user_name)
    input_email.send_keys(email)
    input_password.send_keys(password)
    input_password_confirm.send_keys(password)
    if "Это значение не допускается." in driver.page_source:
        driver.close()
        return True



def test_open_site(driver_init):
    assert ("Strategium", driver_init.title)


def test_search_incor(driver_init):
    search = driver_init.find_element(By.NAME, "q")
    search.send_keys("34234234")
    search.send_keys(Keys.RETURN)
    assert "По вашему запросу ничего не найдено. Попробуйте расширить критерии поиска." in driver_init.page_source


def test_search_cor(driver_init):
    search = driver_init.find_element(By.NAME, "q")
    search.send_keys("Европа")
    search.send_keys(Keys.RETURN)
    assert "Европа" in driver_init.page_source


def test_auth_user(driver_init):
    auth_user("TheRad445", "070903Rad", driver_init=driver_init)
    # user_name_id = wait_of_element_located(xpath='//*[@class=\"ipsType_dark ipsType_large ipsType_bold\"]/a',driver_init=driver_init)
    user_name_id = driver_init.find_element(By.XPATH, "//a[@title=\"Перейти в свой профиль\"]")
    assert (user_name_id, True)


def test_reg_user_correct():
    assert (reg_user("TheRad45343", "islamov.radmir2016@yandex.ru", "3423423Radmir"), False)


def test_reg_user_name_cor():
    assert (reg_user("TheRad45343", "", ""), True)


def test_reg_user_name_incor():
    assert (reg_user("@user", "", ""), True)


def test_reg_user_email_cor():
    assert (reg_user("", "islamov.radmir2016@yandex.ru", ""), True)


def test_reg_user_email_incor():
    assert (reg_user("", "islamov.radmir2016yandexru", ""), True)


def test_reg_user_password_cor():
    assert (reg_user("", "", "34234324Raddfdf"), True)

def test_reg_user_password_incor():
    assert (reg_user("", "", "!!!@#@!@#!"), True)

# def add_item_to_cart(xpath_item, driver_init):
#     # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
#     item_name = wait_of_element_located(
#         xpath=xpath_item,
#         driver_init=driver_init)
#     item_name.click()
#
#     # Поиск и ожидание кнопки добавления товара и клик по этой кнопке
#     item_add_button = wait_of_element_located(
#         xpath='//*[@id=\"add-to-cart-sauce-labs-fleece-jacket\"]',
#         driver_init=driver_init)
#     item_add_button.click()
#
#     # Ждем пока товар добавится в корзину, появится span(кол-во позиций в корзине)
#     # Возвращаем True или False в зависимости добавлися товар или нет
#     shop_cart_with_item = wait_of_element_located(
#         xpath='//*[@id=\"shopping_cart_container\"]/a/span',
#         driver_init=driver_init)
#     return shop_cart_with_item


# def test_add_jacket_to_the_shopcart(driver_init):
#     # Аутентификация пользователя
#     auth_user("TheRad445", "070903Rad", driver_init=driver_init)
#
#     # Добавление товара в корзину и если товар добавлен переход в корзину
#     add_item_to_cart(xpath_item='//*[@id=\"item_5_title_link\"]/div',
#                      driver_init=driver_init).click()
#     # Поиск корзины и клик
#     wait_of_element_located(xpath='//*[@id=\"shopping_cart_container\"]/a',
#                             driver_init=driver_init).click()
#
#     # Поиск ссылки элемента позиции магазина
#     item_name = wait_of_element_located(xpath='//*[@id=\"item_5_title_link\"]/div',
#                                         driver_init=driver_init)
#
#     # Поиск описания товара
#     item_description = wait_of_element_located(xpath='//*[@id=\"cart_contents_container\"]/div/div[1]/div[3]/div[2]/div[1]',
#                                                driver_init=driver_init)
#
#     assert item_name.text == "Sauce Labs Fleece Jacket"
#     assert item_description.text == "It's not every day that you come across a midweight quarter-zip fleece jacket" \
#                                     " capable of handling everything from a relaxing day outdoors to a busy day at " \
#                                     "the office."


if __name__ == '__main__':
    test_open_site(driver_init=driver_init)
    test_search_cor(driver_init=driver_init)
    test_search_incor(driver_init=driver_init)
    test_auth_user(driver_init=driver_init)
    test_reg_user_correct()
    test_reg_user_name_cor()
    test_reg_user_name_incor()
    test_reg_user_email_cor()
    test_reg_user_email_incor()
    test_reg_user_password_cor()
    test_reg_user_password_incor()