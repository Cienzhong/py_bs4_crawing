# 搜索引擎爬虫（360搜索）
# python F:\workspace\git_python\test-searchcraw.py
import re
import requests
from bs4 import BeautifulSoup
import analyse.get_tagtext
import analyse.get_emailaddr
import time

key = '洗碗机'
url = 'https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q=' + key + '&pn='
#分页 &pn=2

def getdockey(url):
    if url == '' or url == None:
        return
    text_arr = analyse.get_tagtext.get_text(url)
    fidtext = []
    mailaddrs = []
    # 查找符合的段落
    for s in text_arr:
        if '@' in s:
            fidtext.extend(s.split())
    # 查找符合的语句
    for m in fidtext:
        if '@' in m:
            mailaddrs.append(m)
    mailsplit = []
    for addr in mailaddrs:
        for a in addr.split():
            if '@' in a:
                mailsplit.append(a)
    addrs = []
    for ma in mailsplit:
        addrs.extend(analyse.get_emailaddr.find_email(ma))
    for em in addrs:
        print(em)

# 获取目标的地址
def gettargeturl(url):
    reUrl = url
    if 'so.com' in url:
        req = requests.get(url)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, 'html.parser')
            equiv = soup.find('meta', attrs={"http-equiv":"refresh"})
            reUrl = equiv['content'].split('URL=')[1].replace("'","") # 重定向url

    return reUrl

def bsfindlist(htmldoc):
    if htmldoc == '' or htmldoc == None:
        return
    soup = BeautifulSoup(htmldoc, 'html.parser')
    bodydoc = soup.body
    print('target url:')
    for child in bodydoc.find_all("h3", class_="res-title"):
        target_url = gettargeturl(child.a['href'])
        print(target_url)
        getdockey(target_url)

def _main():
    print('begin:'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    req=requests.get(url+'2')
    req.encoding='utf-8'
    if req.status_code == 200:
        bsfindlist(req.text)
    req = requests.get(url + '3')
    if req.status_code == 200:
        bsfindlist(req.text)
    req = requests.get(url + '4')
    if req.status_code == 200:
        bsfindlist(req.text)
    print('end:' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

if 1 > 0:
    _main()

