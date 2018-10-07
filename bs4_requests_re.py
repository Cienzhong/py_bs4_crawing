import re
import requests
from bs4 import BeautifulSoup

# return email string
# if have not email, return None
def find_email(str):
    regx = "\\w+@\\w+(\\.\\w+)+"
    if(re.compile(regx).match(str)):
        return str

def init_mail_split(str):
    if(str == None):
        return
    for t in str.split():
        mailaddr = find_email(t)
        if (mailaddr != None):
            print(mailaddr)

def ergodic_key(soup):
    __list = soup.find_all(["p", "a", "span", "li"])
    for text in __list:
        init_mail_split(text.string)

def main():
    url = "http://www.mapgoo.net/html/about.aspx"
    try:
        resp = requests.get(url)
        resp.encoding = 'utf-8'
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            ergodic_key(soup)
        else:
            print('url fail.')
    except Exception as e:
        print(e)

main()