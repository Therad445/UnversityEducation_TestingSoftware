from behave import given, when, then
from controller import Controller


@given('the calculator is turned on')
def step_impl(context):
    context.controller = Controller()


@when('I enter "{num1}" and press "+" and enter "{num2}" and press "="')
def step_impl(context, num1, num2):
    context.controller.on_button_click(num1)
    context.controller.on_button_click('+')
    context.controller.on_button_click(num2)
    context.controller.on_button_click('=')


@then('the result should be "{result}" on the display')
def step_impl(context, result):
    assert context.controller.view.value_var.get() == str(result)
