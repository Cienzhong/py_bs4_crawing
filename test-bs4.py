#beautifulsoup4库练习

import re
import requests
from bs4 import BeautifulSoup

req=requests.get('http://www.mapgoo.net/html/NewsContent.html?type=&id=195')
req.encoding='utf-8'
if req.status_code == 200:
	soup = BeautifulSoup(req.text, "html.parser")
	bodydoc = soup.body
	for child in bodydoc.find_all(['a','p','span','li', 'dd', 'dt', 'td']):
		if len(child.contents)==1:
			if child.name == 'a':
				print('href:' + child['href'])
			print(child.contents[0])
