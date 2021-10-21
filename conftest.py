import pytest
from selenium import webdriver

def pytest_addoption(parser):
	parser.addoption('--browser_name', action='store',
			 default='chrome', help='Выбери браузер: chrome или firefox')

@pytest.fixture
def browser(request):
	browser_name = request.config.getoption('browser_name')
	browser = None
	if browser_name == 'chrome':
		browser = webdriver.Chrome()
	else:
		browser = webdriver.Firefox()
	yield driver
	driver.quit()
