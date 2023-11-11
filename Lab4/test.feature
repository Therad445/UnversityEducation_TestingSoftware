Feature: Addition functionality of the calculator

Scenario: Add two positive numbers
    Given the calculator is turned on
    When I enter "5" and press "+" and enter "7" and press "="
    Then the result should be "12" on the display
