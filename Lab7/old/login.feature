Feature: Login Strategium.ru

Scenario: Correct Auth
    Given Launch Chrome browser
    When Open Login
    Then Enter TheRad445 070903Rad
    And  Verify data
    And Close browser

Scenario: Incorrect Auth
    Given Launch Chrome browser
    When Open Login
    Then Enter "TheRad45343" "3423423Radmir"
    And  Verify data
    And Close browser