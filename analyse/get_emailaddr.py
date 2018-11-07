# 获取邮箱地址，正则表达式匹配

import re

# return email string
# if have not email, return None
def compile_email(str):
    regx = "\\w+@\\w+(\\.\\w+)+"
    if(re.compile(regx).match(str)):
        return str

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