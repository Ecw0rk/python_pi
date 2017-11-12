import os, requests, bs4

req = requests.get(
    url='http://www.zhihu.com/',
    headers={
        'Referer':'https://www.zhihu.com',
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
)
print(req.text)