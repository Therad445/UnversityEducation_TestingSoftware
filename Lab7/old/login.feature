Feature: Login Strategium.ru

Scenario: Correct Auth
    Given Launch Chrome browser
    When Open Login
    Then enter username "TheRad445" password "070903Rad"
    Then Verify "Перейти в свой профиль"
    Then Close browser

Scenario: Incorrect Login
    Given Launch Chrome browser
    When Open Login
    Then enter username "TheRad45343" password "070903Rad"
    Then Verify "не связан ни с одним аккаунтом"
    Then Close browser

Scenario: Incorrect Password
    Given Launch Chrome browser
    When Open Login
    Then enter username "TheRad445" password "3423423Radmir"
    Then Verify "Введённый пароль является некорректным"
    Then Close browser