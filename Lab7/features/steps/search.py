from behave import *
from selenium import webdriver

@given(u'Launch Chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Firefox()
    # context.driver=webdriver.Chrome(executable_path=r"C:\Python\chromedriver.exe")

@when(u'Open Homepage')
def openHomepage(context):
    context.driver.get("https://www.strategium.ru/forum/")

@then(u'Open Search "{str}"')
def openSearch(context):
    search = context.driver.find_element(context.By.NAME, "q")
    search.send_keys(str)
    search.send_keys(context.Keys.RETURN)

@then(u'Verify Data')
def enterSearch(context):
    assert "По вашему запросу ничего не найдено. Попробуйте расширить критерии поиска." in context.driver.page_source

@then(u'Close browser')
def closeBrowser(context):
    context.driver.close()