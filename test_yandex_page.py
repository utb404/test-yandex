from pages.main_page import MainPage
from pages.result_page import SearchResultPage
from pages.image_page import ImageSearchPage

url = 'https://yandex.ru'
word_for_search = 'тензор'

@pytest.mark.search
def test_search_string(browser):
	main_page = MainPage(browser, url)
	main_page.open()
	main_page.should_see_search_string()
	main_page.insert_word_to_search_string(word_for_search)
	main_page.should_see_suggest()
	main_page.press_enter()
	result_page = SearchResultPage(browser, browser.current_url)
	result_page.query_in_result()

	
@pytest.mark.image
def test_image_search(browser):
	main_page = MainPage(browser, url)
	main_page.open()
	main_page.should_see_image()
	main_page.open_images()
	image_page = ImageSearchPage(browser, browser.current_url)
	image_page.check_url()
	image_page.open_first_category()
	image_page.open_first_image()
	first_image = image_page.get_image_src()
	image_page.open_next_image()
	image_page.check_next_image(first_image)
	image_page.open_previuos_image()
	image_page.check_previous_image(first_image)
