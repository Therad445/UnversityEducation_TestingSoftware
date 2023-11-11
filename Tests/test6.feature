Feature: Clearing the calculator of the calculator

Scenario: Clearing the calculator
Given the calculator is turned on
When I enter "5" and "+" and "3" and "C"
Then the calculator displays "0"