from selenium import webdriver
import os

configs = {
	'driver_path': os.environ.get('CHROMEDRIVER_PATH') or '/usr/bin/chromedriver',
	'binary_location': os.environ.get('GOOGLE_CHROME_BIN') or '/usr/bin/google-chrome-stable'
}

selenium_options = webdriver.ChromeOptions()
selenium_options.binary_location = configs['binary_location'] 
selenium_options.add_argument('--headless')
selenium_options.add_argument('--disable-dev-shm-usage')
selenium_options.add_argument('--no-sandbox')