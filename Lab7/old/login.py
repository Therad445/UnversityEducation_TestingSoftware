import time

from behave import *
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


@given(u'Launch Chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome()
    # context.driver=webdriver.Chrome(executable_path=r"C:\Python\chromedriver.exe")


@when(u'Open Login')
def openLogin(context):
    context.driver.get("https://www.strategium.ru/forum/")
    open_login = context.driver.find_element(By.ID, "elUserSignIn")
    open_login.send_keys(Keys.RETURN)

@then('enter username "{log}" password "{pas}"')
def enterData(context, log, pas):
    input_username = context.driver.find_element(By.NAME, "auth")
    input_password = context.driver.find_element(By.NAME, "password")
    login_button = context.driver.find_element(By.ID, "elSignIn_submit")
    input_username.send_keys(log)
    input_password.send_keys(pas)
    login_button.send_keys(Keys.RETURN)

@then(u'Verify "{data}"')
def enterSearch(context, data):
    assert data in context.driver.page_source

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()

