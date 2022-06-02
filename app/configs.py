from selenium import webdriver

configs = {
	'driver_path': '/usr/bin/chromedriver',
}

selenium_options = webdriver.ChromeOptions()
selenium_options.add_argument('--headless')