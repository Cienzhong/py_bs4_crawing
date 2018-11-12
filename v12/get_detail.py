# 打印搜索到的页面html进行解析

import re
import requests
from bs4 import BeautifulSoup
import analyse.get_emailaddr

# get请求超时时间(秒)
TIMEOUT_REQUESTS_GET_SECOND = 20

# 在哪些标签里面提取关键字
KEYS_HTMLTAG_ARR = ['li', 'p', 'a', 'span', 'b', 'dd', 'td', 'strong', 'label', 'h3', 'h4']

#使用正常的字符替换HTML中特殊的字符实体.
#你可以添加新的实体字符到CHAR_ENTITIES中,处理更多HTML字符实体.
#@param htmlstr HTML字符串.'''
def replaceCharEntity(htmlstr):
    CHAR_ENTITIES={'nbsp':'','160':'',
                    'lt':'<','60':'<',
                    'gt':'>','62':'>',
                    'amp':'&','38':'&',
                    'quot':'"''"','34':'"'}
    re_charEntity=re.compile(r'&#?(?P<name>\w+);') #命名组,把 匹配字段中\w+的部分命名为name,可以用group函数获取
    sz=re_charEntity.search(htmlstr)
    while sz:
        #entity=sz.group()
        key=sz.group('name') #命名组的获取
        try:
            htmlstr=re_charEntity.sub(CHAR_ENTITIES[key],htmlstr,1) #1表示替换第一个匹配
            sz=re_charEntity.search(htmlstr)
        except KeyError:
            htmlstr=re_charEntity.sub('',htmlstr,1)
            sz=re_charEntity.search(htmlstr)
    return htmlstr

def comp_tag(htmlstr):
    re_h = re.compile(r'</?\w+[^>]*>')
    text = re_h.sub('', htmlstr)
    text = replaceCharEntity(text)
    #re_br = re.compile('<br\s*?/?>')
    #text = re_br.sub('\n', text)
    text = text.replace("\n", "")
    text = text.strip()
    return text

# 返回联系方式链接元组
def get_connectlinks(linkstr):
    connect_links = []
    if linkstr.find('about') >= 0 or linkstr.find('connect') >= 0 or linkstr.find('href') >= 0:
        if linkstr.find('http://') >= 0 or linkstr.find('https://') >= 0:
            if linkstr not in connect_links:
                connect_links.append(linkstr)
    return connect_links

'''
获取网站的body内容，请务必保证url值有效
解析节点@邮箱地址
解析节点url
返回网址、邮箱地址
[
    {"url": "http://url/1", "emails": [ "mm@gg.com", "mm1@gg.com" ]},
    {"url": "http://url/2", "emails": [ "mm@gg.com", "mm1@gg.com" ]},
    {"url": "http://url/3", "emails": [ "mm@gg.com", "mm1@gg.com" ]}
]
'''
def req_websitebody(url, findChild):
    details = []
    requests.adapters.DEFAULT_RETRIES = 5  # 增加重试连接次数
    sessions = requests.session()
    sessions.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
    sessions.keep_alive = False  # 关闭多余的连接
    try:
        resp = sessions.get(url, timeout=TIMEOUT_REQUESTS_GET_SECOND)
        resp.encoding = 'utf-8'
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            nodes = soup.body.find_all(KEYS_HTMLTAG_ARR)
            addrs = []
            tag_text = ''
            tag_strs = []
            connect_links = []
            linkstr = ''
            #开始遍历节点
            for n in nodes:
                tag_text = str(n)
                if n.name == 'a':
                    linkstr = n['href']
                    if '@' in linkstr:  # 找到包含"@"的链接内容
                        addrs.extend(analyse.get_emailaddr.find_email(linkstr))  # 匹配邮箱地址，存入预先声明好的数组
                    connect_links.extend(get_connectlinks(linkstr))  # 获取
                if '@' in tag_text:
                    tag_strs.append(comp_tag(tag_text))  # 找到包含"@"的节点内容
            for tag_str in tag_strs:
                addrs.extend(analyse.get_emailaddr.find_email(tag_str))  # 匹配邮箱地址，存入预先声明好的数组
            details.append({
                "url": url,
                "emails": addrs
            })
            if findChild == True:
                # 对子链接(关于、联系、帮助)进一步爬虫
                for link in connect_links:
                    details.extend(req_websitebody(link, False))
    except:
        print('发生了异常')
    return details