from .base_page import BasePage
from .locators import ImagePageLocators


class ImageSearchPage(BasePage):
    def check_url(self):
    	assert self.browser.current_url == 'https://yandex.ru/images/?utm_source=main_stripe_big', \
    	    f'Перешли не на https://yandex.ru/images/, а на {self.browser.current_url}'

    def open_first_category(self):
    	category_name = self.browser.find_element(*ImagePageLocators.CATEGORY)
    	category = self.browser.find_element(*ImagePageLocators.CATEGORY)
    	category.click()
    	text_in_search_string = self.browser.find_element(*ImagePageLocators.TEXT_IN_SEARCH_STRING)
    	assert category_name.text == text_in_search_string.get_attribute('value'), \
    	    'Открывшаяся категория не совпадает с первой категорией прошлой страницы'

    def open_first_image(self):
    	image = self.browser.find_element(*ImagePageLocators.FIRST_IMAGE)
    	image.click()

    def get_image_src(self):
    	image = self.browser.find_element(*ImagePageLocators.IMAGE_DATA)
    	image_src = image.get_attribute('src')
    	return str(image_src)

    def open_next_image(self):
    	button = self.browser.find_element(*ImagePageLocators.NEXT_IMAGE_BUTTON)
    	button.click()

    def check_next_image(self, first_image):
    	image = self.browser.find_element(*ImagePageLocators.IMAGE_DATA)
    	image_src = image.get_attribute('src')
    	assert str(image_src) != first_image, \
    	    'Открывшееся изображение не отличается от предыдущего'

    def open_previuos_image(self):
    	button = self.browser.find_element(*ImagePageLocators.PREVIOUS_IMAGE_BUTTON)
    	button.click()

    def check_previous_image(self, first_image):
        image = self.browser.find_element(*ImagePageLocators.IMAGE_DATA)
        image_src = image.get_attribute('src')
        assert str(image_src) == first_image, \
             'Изображение отличается от того, что было раньше'

