"""
This scripts scrapes the link provided for a play list on Anghami and gets links for the same songs on youtube music.
It writes these links to a .txt file. Hence, it can be then chained with another script which constructs a play list 
on youtube music from the links in the .txt file.
"""

import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from os import getcwd
from os.path import isfile, getsize, join

anghami_url = 'https://play.anghami.com/album/905098?branchId=%2FvCkl3A4ISdb'
local_copy_file = 'anghami songs.html'
local_copy_path = join(getcwd(), local_copy_file)

if not (isfile(local_copy_path) and getsize(local_copy_path)):
	r = requests.get(anghami_url)
	with open(local_copy_file, 'wb') as output_file:
		output_file.write(r.content)

the_file = open(local_copy_path, 'rb')
soup = BeautifulSoup(the_file.read(), 'html.parser')
the_file.close()



song_names = [element.contents[0].contents[0] for element in soup.find_all(class_='cell cell-title')]

songs_list_file_name = 'Songs List.csv'
with open(songs_list_file_name, 'w') as file:
	for name in song_names:
		file.write(name+'\n')


music_url = 'https://music.youtube.com/search?q='
search_enhancer = ' الشيخ إمام'
songs_url_on_music = []
urls_file_name = 'Playlist links on Youtube Music.txt'
urls_file_path = join(getcwd(),urls_file_name)
browser = Chrome()

if not (isfile(urls_file_path) and getsize(urls_file_path)):
	for name in song_names:
		browser.get(music_url+name+search_enhancer)
		browser.find_element_by_xpath('/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[2]/ytmusic-responsive-list-item-renderer/div[1]').click()
		songs_url_on_music.append(browser.current_url.rsplit('&')[0])
	browser.quit()

	with open(urls_file_name, 'w') as file:
		for url in songs_url_on_music:
			file.write(url+'\n')
