from behave import *
from selenium import webdriver

@given(u'Launch Chrome browser')
def launchBrowser(context):
    context.driver=webdriver.Chrome(executable_path=r"C:\Python\chromedriver.exe")

@when(u'Open Registration')
def step_impl(context):


@then(u'Enter Data')
def step_impl(context):

@then(u'Close browser')
def closeBrowser(context):