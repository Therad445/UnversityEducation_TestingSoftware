Feature: Changing the sign of a number of the calculator

Scenario: Changing the sign of a number
Given the calculator is turned on
When I enter "5" and "+/-"
Then the calculator displays "-5"
