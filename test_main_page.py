from pages.main_page import MainPage

url = 'https://yandex.ru'
word_for_search = 'тензор'

def test_should_see_search_string(browser):
	main_page = MainPage(browser, url)
	main_page.open()
	main_page.should_see_search_string()
