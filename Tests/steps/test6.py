from behave import given, when, then
from controller import Controller


@given('the calculator is turned on')
def step_impl(context):
    context.controller = Controller()


@when('I enter "{num1}" and "+" and "{num2}" and "С"')
def step_impl(context, num1, num2):
    context.controller.on_button_click(int(num1))
    context.controller.on_button_click('+')
    context.controller.on_button_click(int(num2))
    context.controller.on_button_click('С')


@then('he calculator displays "{result}"')
def step_impl(context, result):
    assert context.controller.view.value_var.get() == str(result)
