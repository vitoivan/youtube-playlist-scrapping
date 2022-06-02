from time import sleep
from bs4 import BeautifulSoup
from app.utils import get_list_url, get_video_id, get_video_title
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from app.configs import configs, selenium_options

def get_playlist_videos(url):

	formatted_videos = []

	# Starting chromedriver service
	service = ChromeService(configs['driver_path'])
	service.start()

	# starting chromedriver app (--headless)
	driver = webdriver.Remote(service.service_url, options=selenium_options)
	driver.implicitly_wait(2)

	driver.get(get_list_url(url))
	sleep(10)

	page = BeautifulSoup(driver.page_source, 'html.parser')
	vlist = page.select('#playlist-items')

	for _, video in enumerate(vlist):
		formatted_videos.append({
			'title': get_video_title(video),
			'youtube_id': get_video_id(video.a)
		})

	driver.close()
	return formatted_videos