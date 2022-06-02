# 2 Jun 2022

def get_list_id(url: str):
	return url.split('list=')[1].split('&')[0]

def get_list_url(url: str):
	return 'https://youtube.com/watch?v={}&list={}'\
	.format(get_video_id_from_string(url), get_list_id(url))

def get_video_id_from_string(url: str):
	return url.split('watch?v=')[1].split('&')[0]

def get_video_id(link):
	return get_video_id_from_string(link.attrs['href'])

def get_video_title(link):
	return link.select('#video-title')[0].attrs['title'] or ''