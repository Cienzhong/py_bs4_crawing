# 获取tag文本内容

import re
import requests
from bs4 import BeautifulSoup

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

# 重定向地址：
# http://www.so.com/link?m=aTWIAtdGb%2FenpvqUeabutQ0jd1tclfWVxzyqW%2BuWdll%2Fhf%2FJtFOGhMydW28nwjeE8XfTQRNZNnANiypyzbtd6qw0N8vrbHXYEQKU6lo%2BeKxE%3D
def get_text(url):
    _list = []
    if url == '' or url == None:
        return _list
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        if soup.body == None or soup.meta['name'] == 'referrer':
            equiv = soup.find('meta', attrs={"http-equiv":"refresh"})
            reUrl = equiv['content'].split('URL=')[1].replace("'","") # 重定向url
            resp = requests.get(reUrl)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
        arr_text = soup.body.findAll(['li','p','a','span','b','dd','td'])
        for i in arr_text:
            _list.append(comp_tag(str(i)))
        '''
        arr_href = soup.body.findAll('a')
        for hf in arr_href:
            if len(hf.contents)==1:
                _list.append(comp_tag(hf['href']))
        '''
    return _list