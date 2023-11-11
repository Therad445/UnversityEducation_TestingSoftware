Feature: Calculator Operations
  As a user
  I want to use a calculator
  So that I can perform basic arithmetic operations

  Scenario: Addition
    Given the calculator is turned on
    When I enter "5" and "+" and "3" and "="
    Then the calculator displays "8"

  Scenario: Subtraction
    Given the calculator is turned on
    When I enter "9" and "-" and "4" and "="
    Then the calculator displays "5"

  Scenario: Multiplication
    Given the calculator is turned on
    When I enter "6" and "*" and "7" and "="
    Then the calculator displays "42"

  Scenario: Division
    Given the calculator is turned on
    When I enter "20" and "/" and "4" and "="
    Then the calculator displays "5"

  Scenario: Percentage
    Given the calculator is turned on
    When I enter "18" and "+" and "400" and "%"
    Then the calculator displays "4"
