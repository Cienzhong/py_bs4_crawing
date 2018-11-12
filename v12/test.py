import v12.get_detail

url = "https://post.smzdm.com/p/522605/"
json_details = v12.get_detail.req_websitebody(url, True)
print(json_details)
