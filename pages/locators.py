from selenium.webdriver.common.by import By


class MainPageLocators():
	SEARCH_STRING = (By.ID, 'text')
	SUGGEST = (By.CSS_SELECTOR, '[role=listbox]')