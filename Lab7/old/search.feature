Feature: Search Strategium.ru

Scenario: Incorrect Data
    Given Launch Chrome browser
    When Open Homepage
    Then Open Search "47891234612343421"
    Then Verify "Найдено 0 результатов"
    Then Close browser

Scenario: Correct Data
    Given Launch Chrome browser
    When Open Homepage
    Then Open Search "Европа"
    Then Verify "data-page="1""
    Then Close browser