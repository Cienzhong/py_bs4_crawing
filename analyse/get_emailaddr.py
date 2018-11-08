# 获取邮箱地址，正则表达式匹配
# 参考 https://blog.csdn.net/a6225301/article/details/46548933

import re

# return email string
# if have not email, return None
def compile_email(str):
    regx = "\\w+@\\w+(\\.\\w+)+"
    if(re.compile(regx).match(str)):
        return str

def find_email(str):
    regex = re.compile(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b", re.IGNORECASE)
    mails = re.findall(regex, str)
    return mails

def split_key(str):
	_keys = []
	for partstr in str.split():
		if partstr != '' and partstr != None:
			if _keys.count(partstr) > 0:
				continue
			_keys.append(partstr)
	for partstr in str.split(':'):
		if partstr != '' and partstr != None:
			if _keys.count(partstr) > 0:
				continue
			_keys.append(partstr)
	for partstr in str.split('：'):
		if partstr != '' and partstr != None:
			if _keys.count(partstr) > 0:
				continue
			_keys.append(partstr)
	return _keys

# 返回邮箱地址数组
def get_emails(text):
	_mails = []
	keys = split_key(text)
	for k in keys:
		if compile_email(k) != None:
			_mails.append(k)
	return _mails