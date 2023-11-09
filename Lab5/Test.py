from selenium import webdriver

# Open the website in Google Chrome
driver = webdriver.Chrome()
driver.get("https://www.phpbb.com/community/")

# Verify that the search field is present
search_field = driver.find_element_by_name("keywords")
assert search_field.is_displayed()

# Verify that the text "Search Community" is present
search_text = driver.find_element_by_xpath("//h2[contains(text(), 'Search Community')]")
assert search_text.is_displayed()

# Enter a meaningless string in the search field
search_field.send_keys("qwertyuiop")
search_button = driver.find_element_by_name("search")
search_button.click()

# Verify that the text "The following words in your search query were ignored because they are too common words" is present
ignored_text = driver.find_element_by_xpath("//div[contains(text(), 'The following words in your search query were ignored because they are too common words')]")
assert ignored_text.is_displayed()

# Enter the word "phpBB" in the search field
search_field.clear()
search_field.send_keys("phpBB")
search_button.click()

# Verify that the search results table is present
results_table = driver.find_element_by_xpath("//table[@class='tablebg']")
assert results_table.is_displayed()

# Verify that the text "phpBB" is present in all cells of the table
table_cells = results_table.find_elements_by_tag_name("td")
for cell in table_cells:
    assert "phpBB" in cell.text

# Verify that the text "phpBB" is present in the "Software" category
software_category = driver.find_element_by_xpath("//a[contains(text(), 'Software')]")
assert "phpBB" in software_category.text

# Close the browser window
driver.quit()