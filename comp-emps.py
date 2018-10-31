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

url = "http://www.sohu.com/a/272245079_157534"
resp = requests.get(url)
resp.encoding = 'utf-8'
if resp.status_code == 200:
    soup = BeautifulSoup(resp.text, 'html.parser')
    arr_li = soup.body.findAll('li')
    for i in arr_li:
        print(comp_tag(str(i)))
    arr_p = soup.body.findAll('p')
    for i in arr_p:
        print(comp_tag(str(i)))
    '''
    arr_a = soup.body.findAll('a')
    for i in arr_a:
        print(i)
    '''
