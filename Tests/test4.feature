Feature: Multiplication of two numbers of the calculator

Scenario: Multiplication of two numbers
Given the calculator is turned on
When I enter "6" and "*" and "7" and "="
Then the calculator displays "42"