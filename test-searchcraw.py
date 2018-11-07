# 搜索引擎爬虫（360搜索）
# python F:\workspace\git_python\test-searchcraw.py
import re
import requests
from bs4 import BeautifulSoup
import analyse.get_tagtext
import analyse.get_emailaddr

key = '洗碗机'
url = 'https://www.so.com/s?ie=utf-8&pn=3&fr=none&src=360sou_newhome&q=' + key
#分页 &pn=2

def getdockey(url):
    if url == '' or url == None:
        return
    text_arr = analyse.get_tagtext.get_text(url)
    mailaddrs = []
    #print('text_arr len:' + str(len(text_arr)))
    for s in text_arr:
        mails = analyse.get_emailaddr.get_emails(s)
        if mails != None and len(mails) > 0:
            mailaddrs.extend(mails)
    for m in mailaddrs:
        print(m)

    #print('mail len:' + str(len(mailaddrs)))

def bsfindlist(htmldoc):
	if htmldoc == '' or htmldoc == None:
		return
	soup = BeautifulSoup(htmldoc, 'html.parser')
	bodydoc = soup.body
	print('url:')
	for child in bodydoc.find_all("h3", class_="res-title"):
		print(child.a['href'])
	print('email addr:')
	for child in bodydoc.find_all("h3", class_="res-title"):
		getdockey(child.a['href'])


def _main():
	req=requests.get(url)
	req.encoding='utf-8'
	if req.status_code == 200:
		bsfindlist(req.text)
		#print(req.text)

if 1 > 0:
	_main()

