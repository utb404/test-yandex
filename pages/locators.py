from selenium.webdriver.common.by import By


class MainPageLocators():
	SEARCH_STRING = (By.ID, 'text')
	SUGGEST = (By.CSS_SELECTOR, '[role=listbox]')

class ResultPageLocators():
	FIRST_RESULT = (By.CSS_SELECTOR, '[data-cid="0"] .organic__path b')
	NEXT_RESULTS = (By.CSS_SELECTOR, '.Organic-Path b')