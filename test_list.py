# 调试列表(list)语法
# python F:\workspace\git_python\test_list.py

import requests
from bs4 import BeautifulSoup

'''
keys = ['a','abs','b','c','123','bb', 'a']
print(keys.count('a'))


str = '李先生  ligo202002@163.com 1'
for partstr in str.split():
	print(partstr)
'''

'''
# 重定向的doc内容：
<meta content="always" name="referrer">
<script>window.location.replace("http://www.yzxwj.com/")</script>
<noscript>
<meta http-equiv="refresh" content="0;URL='http://www.yzxwj.com/'">
</noscript>
'''

'''
url = 'http://www.so.com/link?m=aTWIAtdGb%2FenpvqUeabutQ0jd1tclfWVxzyqW%2BuWdll%2Fhf%2FJtFOGhMydW28nwjeE8XfTQRNZNnANiypyzbtd6qw0N8vrbHXYEQKU6lo%2BeKxE%3D'
#url = 'http://www.yzxwj.com/'
r = requests.get(url)
if r.status_code == 200:
	soup = BeautifulSoup(r.text, 'html.parser')
	if soup.meta['name'] == 'referrer':
		equiv = soup.find('meta', attrs={"http-equiv":"refresh"})
		reUrl = equiv['content'].split('URL=')[1].replace("'","")
	else:
		print('getnow')


s1 = 'hello world!'
s2 = 'world'
if s2 in s1:
	print('ok')
else:
	print('none')
print(s1.find(s2))
'''

pn = 1
while(pn<=10):
	print(pn)
	pn=pn+1;
