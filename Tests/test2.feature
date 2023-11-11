Feature: Percentage calculation of the calculator

Scenario: Percentage calculation
    Given the calculator is turned on
    When I enter "20" and "%" and "="
    Then the calculator displays "0.2"