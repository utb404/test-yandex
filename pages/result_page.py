from .base_page import BasePage
from .locators import ResultPageLocators


class SearchResultPage(BasePage):
	def query_in_result(self):
		urls_in_result = []
		first_result = self.browser.find_element(*ResultPageLocators.FIRST_RESULT)
		search_result = self.browser.find_elements(*ResultPageLocators.NEXT_RESULTS)
		urls_in_result.append(first_result.text)
		for url in search_result:
			urls_in_result.append(url.text)
		assert 'tensor.ru' in urls_in_result[:5], \
			'Ссылка на tensor.ru отсутствует в первых пяти результатах'