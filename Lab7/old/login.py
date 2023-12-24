from behave import *
from selenium import webdriver

@given(u'Launch Chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(executable_path=r"C:\Python\chromedriver.exe")


@when(u'Open Login')
def openLogin(context):
    context.driver.get("https://www.strategium.ru/forum/")


@then(u'Enter Data')
def enterData(context):



@then(u'Verify data')
def verifyData(context):



@then(u'Close browser')
def closeBrowser(context):