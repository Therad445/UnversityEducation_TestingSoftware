from selenium import webdriver
from selenium.webdriver.common.by import By

# Запуск браузера
driver = webdriver.Chrome()

# Зайти на сайт
driver.get("https://miet.ru/forum/")

# Нажать на кнопку "Регистрация"
registration_button = driver.find_element(By.CSS_SELECTOR, "#register-button")
registration_button.click()

# Ввести в поле "Имя пользователя" заведомо бессмысленный набор букв
username_field = driver.find_element(By.CSS_SELECTOR, "#username")
username_field.send_keys("qwerty")

# Ввести в поле "Пароль" заведомо бессмысленный набор букв
password_field = driver.find_element(By.CSS_SELECTOR, "#password")
password_field.send_keys("qwerty")

# Нажать кнопку "Зарегистрироваться"
register_button = driver.find_element(By.CSS_SELECTOR, "#register-button")
register_button.click()

# Проверить наличие на странице текста "Поле «Имя пользователя» не может быть пустым"
username_error_message = driver.find_element(By.CSS_SELECTOR, "#username-error")
assert username_error_message.text == "Поле «Имя пользователя» не может быть пустым"

# Проверить наличие на странице текста "Поле «Пароль» не может быть пустым"
password_error_message = driver.find_element(By.CSS_SELECTOR, "#password-error")
assert password_error_message.text == "Поле «Пароль» не может быть пустым"

# Ввести в поле "Имя пользователя" имя пользователя, которое уже существует на сайте
username_field.send_keys("ivan")

# Ввести в поле "Пароль" пароль, который соответствует имени пользователя
password_field.send_keys("ivan")

# Нажать кнопку "Зарегистрироваться"
register_button.click()

# Проверить наличие на странице текста "Пользователь с таким именем уже существует"
username_error_message = driver.find_element(By.CSS_SELECTOR, "#username-error")
assert username_error_message.text == "Пользователь с таким именем уже существует"

# Ввести в поле "Имя пользователя" имя пользователя, которое не существует на сайте
username_field.send_keys("new_user")

# Ввести в поле "Пароль" пароль, который соответствует имени пользователя
password_field.send_keys("new_user")

# Нажать кнопку "Зарегистрироваться"
register_button.click()

# Проверить наличие на странице текста "Пользователь успешно зарегистрирован"
success_message = driver.find_element(By.CSS_SELECTOR, "#success-message")
assert success_message.text == "Пользователь успешно зарегистрирован"

# Закрыть окно браузера
driver.quit()
