from behave import given, when, then
from model import Model
from view import View
from controller import Controller

@given('the calculator is turned on')
def step_impl(context):
    context.controller = Controller()

@when('I enter "{num1}" and "{operation}" and "{num2}" and "="')
def step_impl(context, num1, num2, operation):
    context.controller.on_button_click(int(num1))
    context.controller.on_button_click(operation)
    context.controller.on_button_click(int(num2))
    context.controller.on_button_click('=')

@then('the calculator displays "{result}"')
def step_impl(context, result):
    assert context.controller.view.value_var.get() == str(result)
