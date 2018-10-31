# 搜索引擎爬虫（360搜索）
# python e:\exercise\python-hello\test-searchcraw.py
import re
import requests
from bs4 import BeautifulSoup

key = 'beautifulsoup'
url = 'https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q=' + key
#分页 &pn=2

def bsfindlist(htmldoc):
	if htmldoc == '' or htmldoc == None:
		return
	soup = BeautifulSoup(htmldoc, 'html.parser')
	bodydoc = soup.body
	arr_text = []
	arr_href = []
	arr_div = []
	for child in bodydoc.find_all("h3", class_="res-title"):
		print(child.a['href'])


def _main():
	req=requests.get(url)
	req.encoding='utf-8'
	if req.status_code == 200:
		bsfindlist(req.text)
		#print(req.text)

if 1 > 0:
	_main()

