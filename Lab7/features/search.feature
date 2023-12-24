Feature: Search Strategium.ru
Scenario:
    Given Launch Chrome browser
    When Open Homepage
    Then Open Search "34234234"
    Then Verify Data
    Then Close browser
