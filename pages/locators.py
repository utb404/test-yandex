from selenium.webdriver.common.by import By


class MainPageLocators():
	SEARCH_STRING = (By.ID, 'text')
	SUGGEST = (By.CSS_SELECTOR, '[role=listbox]')
	IMAGES = (By.CSS_SELECTOR, '[data-statlog="services_new.item.images.2"]')

class ResultPageLocators():
	FIRST_RESULT = (By.CSS_SELECTOR, '[data-cid="0"] .organic__path b')
	NEXT_RESULTS = (By.CSS_SELECTOR, '.Organic-Path b')

class ImagePageLocators():
	CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0')
	CATEGORY_NAME = (By.CSS_SELECTOR, '.PopularRequestList-SearchText')
	TEXT_IN_SEARCH_STRING = (By.CSS_SELECTOR, '.input__box input')
	FIRST_IMAGE = (By.CSS_SELECTOR, '.serp-item__preview')
	IMAGE_DATA = (By.CSS_SELECTOR, '.MMImage-Origin')
	NEXT_IMAGE_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_next')
	PREVIOUS_IMAGE_BUTTON = (By.CSS_SELECTOR, '.CircleButton_type_prev')