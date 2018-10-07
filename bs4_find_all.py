import requests
from bs4 import BeautifulSoup

html_doc = """
<div>
    <p class="boys">Open the book.</p>
    <p>If I am a boy, I will do it.</p>
    <span>labels</span>
</div>
<div>
    <li>Name</li>
    <ul>
        <li><p>529781013@qq.com</p></li>
        <li><p>Go to</p></li>
        <b>zhzhi2008@126.com</b>
    </ul>
</div>
"""
re_soup = BeautifulSoup(html_doc, 'html.parser')
list_p = re_soup.find_all('p')
for object in list_p:
    print(object.string)