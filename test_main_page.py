from pages.main_page import MainPage

url = 'https://yandex.ru'
word_for_search = 'тензор'

def test_search_string(browser):
	main_page = MainPage(browser, url)
	main_page.open()
	main_page.should_see_search_string()
	main_page.insert_word_to_search_string(word_for_search)
	main_page.should_see_suggest()
	main_page.press_enter()