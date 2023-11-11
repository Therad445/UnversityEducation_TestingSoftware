Feature: Subtraction of two numbers of the calculator

Scenario: Subtraction of two numbers
    Given the calculator is turned on
    When I enter "9" and "-" and "4" and "="
    Then the calculator displays "5"