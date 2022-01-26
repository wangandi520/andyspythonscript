# encoding:utf-8

# pip install requests

import requests
import time

url = 'https://www.manhuabudang.com/u.php'

# cookie
# 漫画补档首页，chrome或edge按f12，网络，刷新页面，名称里选index.php，右侧请求标头，右键user-agent和cookie，复制值到下面冒号后，别忘了引号。
         
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
         "Cookie": ""}
         
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

se = requests.Session()
response = requests.get(url,headers=headers)
if response.status_code == 200:
    resp = se.get(url)

index2 = (response.text).find('<li>漫画:') + 4
index3 = (response.text).find('卷</li>')
getmanhua = (response.text)[index2: index3]
index = (response.text).find('verifyhash')
myveri = ((response.text)[index + 14: index + 22])
#print('verifyhash: ' + myveri)
mytime = int(round(time.time() * 1000))

time.sleep(2)

buttonUrl = 'https://www.manhuabudang.com/jobcenter.php?action=punch&verify=' + myveri + '&step=2&nowtime=' + str(mytime) + '&verify=' + myveri

response2 = requests.get(buttonUrl,headers=headers)
se2 = requests.Session()
if response2.status_code == 200:
    resp2 = se2.get(url)
    #print('request url: ' + buttonUrl)
    #print('status code: ' + str(resp2.status_code))
    if ('你已经打卡' in response2.text):
        print('已经签到过了')
        print(getmanhua)
    elif ('漫画+2' in response2.text):
        print('签到成功')
        print(getmanhua)
    else:
        print('cookies或其他设置错误，打卡失败')
    