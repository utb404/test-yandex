from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage):
	def should_see_search_string(self):
		assert self.is_element_present(*MainPageLocators.SEARCH_STRING), \
			'На странице отсутствует поле поиска'

	def insert_word_to_search_string(self, word):
		search_string = self.browser.find_element(*MainPageLocators.SEARCH_STRING)
		search_string.send_keys(word)

	def should_see_suggest(self):
		assert self.is_element_present(*MainPageLocators.SUGGEST), \
			'На странице отсутствует таблица с подсказками'

	def press_enter(self):
		search_string = self.browser.find_element(*MainPageLocators.SEARCH_STRING)
		search_string.send_keys(Keys.ENTER)

	def should_see_image(self):
		assert self.is_element_present(*MainPageLocators.IMAGES), \
    	    'На странице отсутствует ссылка "Картинки"'

	def open_images(self):
		images = self.browser.find_element(*MainPageLocators.IMAGES)
		images.click()
		self.browser.switch_to.window(self.browser.window_handles[1])
