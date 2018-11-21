# 搜索引擎爬虫类（360搜索）
import requests
from bs4 import BeautifulSoup
import time
import v12.get_detail

class CrawSearchSO:
    key = '洗碗机'
    url = 'https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome'

    def search_list(self, pageNum):
        req = requests.get(self.url + '&q=' + self.key + '&pn=' + str(pageNum))
        req.encoding = 'utf-8'
        if req.status_code == 200:
            self.__find_url(req.text)

    def __find_url(self, text):
        soup = BeautifulSoup(text, 'html.parser')
        for child in soup.body.find_all("h3", class_="res-title"):
            target_url = self.__get_url_CheckRedirect(child.a['href'])
            json_details = v12.get_detail.req_websitebody(target_url)
            print(json_details)

    def __get_url_CheckRedirect(self, url):
        reUrl = url
        if 'so.com' in url:
            req = requests.get(url)
            if req.status_code == 200:
                soup = BeautifulSoup(req.text, 'html.parser')
                equiv = soup.find('meta', attrs={"http-equiv": "refresh"})
                reUrl = equiv['content'].split('URL=')[1].replace("'", "")  # 重定向url

        return reUrl


print('开始爬虫: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
pn = 1
c = CrawSearchSO()
while(pn <= 5):
    c.search_list(pn)
    pn = pn + 1
print('结束爬虫: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
