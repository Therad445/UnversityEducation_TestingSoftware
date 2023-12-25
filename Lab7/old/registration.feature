Feature: Registration Strategium.ru

Scenario: Incorrect User
    Given Launch Chrome browser
    When Open Registration
    Then enter username "!@#!" email "fdsf@mail.ru" password "fdsf1221"
    Then Verify "Это значение не допускается"
    Then Close browser

Scenario: Incorrect Emai
    Given Launch Chrome browser
    When Open Registration
    Then enter username "!@#!" email "@#!@!#" password "fdsfs123"
    Then Verify "Это значение не допускается"
    Then Close browser

Scenario: Incorrect Passwor
    Given Launch Chrome browser
    When Open Registration
    Then enter username "thrad42432" email "fdsf@mail.ru" password "123"
    Then Verify "Очень слабый"
    Then Close browser