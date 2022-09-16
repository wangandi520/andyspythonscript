# encoding:utf-8

# https://ebook.tongli.com.tw/reader/FireBase2.html?bookID=550c8f0c-e231-46eb-4e54-08da895fe379&isLogin=false&isSerial=true
# https://tongli-ebook-cdn.azureedge.net/comic/550C8F0CE23146EB4E5408DA895FE379/1?sv=2020-08-04&sr=b&st=2022-09-07T13:48:33Z&se=2022-09-07T13:54:03Z&sp=r&spr=https&rsct=binary&sig=RaUNmpjaycO2Z%2bQCKtR9jqddoNtfxg8fCRyYr2YL7%2b4%3d

# sv: 2020-08-04
# sr: b
# st: 2022-09-07T13:48:33Z
# se: 2022-09-07T13:54:03Z
# sp: r
# spr: https
# rsct: binary
# sig: RaUNmpjaycO2Z+QCKtR9jqddoNtfxg8fCRyYr2YL7+4=

import requests
import time

# 帖子地址
myUrl = 'https://ebook.tongli.com.tw/reader/FireBase2.html?bookID=550c8f0c-e231-46eb-4e54-08da895fe379&isLogin=false&isSerial=true'
myProxies = {
    'https': 'http://127.0.0.1:7890',
    'http': 'http://127.0.0.1:7890'  
}
myHeaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}       
session = requests.session()
response = session.get(myUrl, proxies = myProxies, headers = myHeaders)

# if response.status_code == 200:
print(response.text)