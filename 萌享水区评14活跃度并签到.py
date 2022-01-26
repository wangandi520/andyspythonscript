# encoding:utf-8

# pip install requests

import requests
import time

# cookie
# 萌享首页，chrome或edge按f12，网络，刷新页面，名称里选index.php，右侧请求标头，右键user-agent和cookie，复制值到下面冒号后，别忘了引号。

# 水区帖子tid
tid = '211701'
page = '1'
# 帖子地址
url = 'https://moeshare.cc/read-htm-tid-' + tid + '-page-' + page + '.html'

mytime = int(round(time.time()))
newtimetmp = int(round(time.time() * 1000))
#print(mytime)

# f12查看自己的cookie并修改
mycookie = "8017a_c_stamp=" + str(mytime) + "; 8017a_lastvisit=0	" + str(mytime) + "	/index.php"

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
         "Cookie": mycookie}
         
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

se = requests.Session()
response = requests.get(url,headers=headers)
if response.status_code == 200:
    resp = se.get(url)
    #print('status code: ' + str(resp.status_code))
index = (response.text).find('verifyhash')

# 获取MD MB

tmpIndex2 = (response.text).find('枚</a>')
tmpIndex3 = (response.text).find('点</a>')

getMB = (response.text)[tmpIndex2 - 8: tmpIndex2].split('>')[1]
getMD = (response.text)[tmpIndex3 - 8: tmpIndex3].split('>')[1]
time.sleep(5)

# 获取倒数第二页数=最新页数-1
tmpIndex = (response.text).find('<div class="fl">共')
newpage = str(int((response.text)[tmpIndex + 17: tmpIndex + 21]) - 1)
#print(newpage)

url = 'https://moeshare.cc/read-htm-tid-' + tid + '-page-' + newpage + '.html'
response = requests.get(url,headers=headers)
if response.status_code == 200:
    resp = se.get(url)
    
# 获取倒数第二页所有pid
pidArray = []
newStart = 0
for i in range(0,14):
    tmpIndex5 = (response.text[newStart:]).find('showping_')
    tmpPid = ((response.text[newStart:])[tmpIndex5 + 9: tmpIndex5 + 16])
    newStart = newStart + tmpIndex5 + 16
    pidArray.append(tmpPid)

# 添加活跃度
if (index == -1):
    print('也许cookie设置错误')
elif (index != -1):
    for eachPid in pidArray:
        myveri = ((response.text)[index + 14: index + 22])
        # print('verifyhash: ' + myveri)
        newtime2 = int(round(time.time() * 1000))
        myreferer = 'https://moeshare.cc/read-htm-tid-211701-page-' + newpage + '.html'
        shuiquUrl = 'https://moeshare.cc/operate.php?action=showping&ajax=1&nowtime=' + str(newtime2) + '&verify=' + myveri
        preCookie = mycookie.split('8017a_c_stamp')[0]
        addCookieUrl = ' 8017a_c_stamp="' + str(newtimetmp) + '"; 8017a_lastvisit=0	' + str(newtime2) + ' /operate.php?ajax1&actionshowping&tid211701&' + 'pid' + eachPid + '&page' + newpage + '&nowtime' + str(newtime2) + '&verify' + myveri
        newCookie = preCookie + addCookieUrl
        #print(newCookie)
        headers2={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
                 "Cookie": newCookie,
                 "Referer": myreferer}
        formData = {
            "verify":myveri,
            "page":newpage,
            "tid":"211701",
            "selid[]":eachPid,
            "step":"1",
            "cid[]":"currency",
            "addpoint[]":"1"
        }
        time.sleep(5)
        response2 = requests.post(shuiquUrl,headers=headers2,data=formData)
        se2 = requests.Session()
        newtimetmp = newtime2
        if response2.status_code == 200:
            resp2 = se2.get(url)
            #print(response2.text)
            if ('活跃度' in response2.text):
                print('页数: ' + newpage + ' PID: ' + eachPid + ' 活跃度+1')
            else:
                print('Error: ' + response2.text)
                
    # 签到
    time.sleep(5)
    qiandaoUrl = 'https://moeshare.cc/jobcenter.php?action=punch&verify=' + myveri + '&step=2&nowtime=' + str(int(round(time.time() * 1000))) + '&verify=' + myveri
    response4 = requests.get(qiandaoUrl,headers=headers)
    se4 = requests.Session()
    if response4.status_code == 200:
        resp4 = se4.get(url)
    print('现在MB: ' + getMB + ' MD: ' + getMD)