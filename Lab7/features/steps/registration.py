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


@when(u'Open Registration')
def openLogin(context):
    context.driver.get("https://www.strategium.ru/forum/register/")
    open_regis = context.driver.find_element(By.ID, "elRegisterButton")
    open_regis.click()

@then('enter username "{log}" email "{em}" password "{pas}"')
def enterData(context, log, em, pas):
    input_username = context.driver.find_element(By.ID, "elInput_username")
    input_email = context.driver.find_element(By.ID, "elInput_email_address")
    input_password = context.driver.find_element(By.ID, "elInput_password")
    # regis_button = context.driver.find_element(By.ID, "elSignIn_submit")
    input_username.send_keys(log)
    input_email.send_keys(em)
    input_password.send_keys(pas)
    time.sleep(2)
    # regis_button.send_keys(Keys.RETURN)

@then('Verify "{data}"')
def verifyData(context, data):
    assert data in context.driver.page_source

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()

