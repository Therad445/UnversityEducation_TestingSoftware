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

@when(u'Open Homepage')
def openHomepage(context):
    context.driver.get("https://www.strategium.ru/forum/")

@then('Open Search "{str1}"')
def openSearch(context,str1):
    search = context.driver.find_element(By.NAME, "q")
    search.send_keys(str1)
    search.send_keys(Keys.RETURN)

@then(u'Verify "{data}"')
def enterSearch(context, data):
    assert data in context.driver.page_source

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()