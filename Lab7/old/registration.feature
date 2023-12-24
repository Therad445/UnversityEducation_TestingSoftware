Feature: Registration Strategium.ru

Scenario: Correct Auth
    Given Launch Chrome browser
    When Open Registration
    Then Enter "TheRad45343", "islamov.radmir2016@yandex.ru", "3423423Radmir"
    And  Verify data
    And Close browser

Scenario: Incorrect Auth
    Given Launch Chrome browser
    When Open Registration
    Then Enter "@#!@", "islamov.radmir2016yandexru", "!@!@!@"
    And  Verify data
    And Close browser
