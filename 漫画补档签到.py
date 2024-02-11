# encoding:utf-8
# pip install requests

import requests
import time

# cookie
# 漫画补档首页，chrome或edge按f12，网络，刷新页面，名称里选index.php，右侧请求标头，右键user-agent和cookie，复制值到下面冒号后，别忘了引号。

headers = {"User-Agent": "",
           "Cookie": ""}
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
buttonUrl = 'https://www.manhuabudangbbs.com//jobcenter.php?action=punch&step=2'
response = requests.get(buttonUrl,headers=headers)
if response.status_code == 200:
    if ('你已经打卡' in response.text):
        print('已经签到过了\n')
    elif ('威望+2' in response.text):
    	print('签到成功，威望+2\n')
    else:
        print('cookies或其他设置错误，打卡失败\n')
