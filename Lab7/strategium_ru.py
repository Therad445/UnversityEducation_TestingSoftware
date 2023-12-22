from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.lambdatest.com")
email_input = driver.find_element_by_link_text('Start Free Testing')