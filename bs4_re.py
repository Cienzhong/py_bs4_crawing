import re
import requests
from bs4 import BeautifulSoup

def find_email(str):
    regx = "\\w+@\\w+(\\.\\w+)+"
    if(re.compile(regx).match(str)):
        return str

html_doc = """
<div>
    <p class="boys">Open the book.</p>
    <p>If I am a boy, I will do it.</p>
    <span>labels</span>
    <span class="box1">_2mw33@xs112.net</span>
</div>
<div>
    <li>Name</li>
    <ul>
        <li><p>529781013@qq.com</p></li>
        <li><p>Go to</p></li>
        <b><a class="link_mail" href="http://url/a/1">zhzhi2008@126.com</a></b>
    </ul>
</div>
"""
re_soup = BeautifulSoup(html_doc, 'html.parser')
list_p = re_soup.find_all(["p","a","span"])
for text in list_p:
    mailaddr = find_email(text.string)
    if(mailaddr != None):
        print(mailaddr)

