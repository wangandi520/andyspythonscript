# encoding:utf-8

# pip install requests

import requests
import time
import sys

# 水区帖子tid
tid = '211701'
page = '1'
# 帖子地址
url = 'https://moeshare.cc/read-htm-tid-' + tid + '-page-' + page + '.html'
mytime = int(round(time.time()))
newtimetmp = int(round(time.time() * 1000))
# 脚本累计加过的活跃度
addhuoyue = 0

# cookie
# 萌享首页，chrome或edge按f12，网络，刷新页面，名称里选index.php，右侧请求标头，右键user-agent和cookie，复制值到下面冒号后，别忘了引号。
# f12查看自己的cookie并修改，只需复制8017a_c_stamp=前面的部分

mycookie = "8017a_c_stamp="

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
         "Cookie": mycookie + str(mytime) + "; 8017a_lastvisit=0	" + str(mytime) + "	/index.php"}

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取活跃度数值
jifenUrl = 'https://moeshare.cc/userpay.php'
response5 = requests.get(jifenUrl,headers=headers)
se5 = requests.Session()
if response5.status_code == 200:
    tmpIndex5 = (response5.text).find('<li class="w mb5">活跃度')
    tmpIndex6 = (response5.text).find('<li class="w mb5">YQBD')
    huoyue = response5.text[tmpIndex5 + 18: tmpIndex6 - 6]
    huoyueNum = int(huoyue.split('：')[1])
    addhuoyue = addhuoyue + huoyueNum
    index = (response5.text).find('verifyhash')
    myveri = ((response5.text)[index + 14: index + 22])
    print('verifyhash :' + myveri)
    print(response5.text[tmpIndex5 + 18: tmpIndex6 - 6])
    time.sleep(3)
        
if (huoyueNum < 14):
    se = requests.Session()
    response = requests.get(url,headers=headers)
    if (' ' in myveri):
        print('Cookie 获取出错: veryify = ' + myveri + ' (8位数字字母组合且无空格)')
        sys.exit()
        
    # 获取MD MB
    tmpIndex2 = (response.text).find('枚</a>')
    tmpIndex3 = (response.text).find('点</a>')
    getMB = (response.text)[tmpIndex2 - 8: tmpIndex2].split('>')[1]
    getMD = (response.text)[tmpIndex3 - 8: tmpIndex3].split('>')[1]
    print('现在MB: ' + getMB + ' MD: ' + getMD)
    time.sleep(3)

    # 获取倒数第二页数=最新页数-1
    tmpIndex = (response.text).find('<div class="fl">共')
    newpage = str(int((response.text)[tmpIndex + 17: tmpIndex + 21]) - 1)
    url = 'https://moeshare.cc/read-htm-tid-' + tid + '-page-' + newpage + '.html'
    response = requests.get(url,headers=headers)
    
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
            # time.sleep(3)
            response2 = requests.post(shuiquUrl,headers=headers2,data=formData)
            se2 = requests.Session()
            newtimetmp = newtime2
            if response2.status_code == 200:
                #print(response2.text)
                if ('活跃度' in response2.text):
                    addhuoyue = addhuoyue + 1
                    print('页数: ' + newpage + ' PID: ' + eachPid + ' 活跃度： ' + addhuoyue)
                else:
                    print('页数: ' + newpage + ' PID: ' + eachPid + ' Error: ' + response2.text)
        time.sleep(3)

# 签到
# qiandaoUrl = 'https://moeshare.cc/jobcenter.php?action=punch&verify=' + myveri + '&step=2&nowtime=' + str(int(round(time.time() * 1000))) + '&verify=' + myveri
mytime3 = int(round(time.time()))
headers3={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69",
         "Cookie": mycookie +  + str(mytime3) + "; 8017a_lastvisit=0	" + str(mytime3) + "	/index.php"}      
qiandaoUrl = 'https://moeshare.cc/jobcenter.php?action=punch&step=2'
response4 = requests.get(qiandaoUrl,headers=headers3)
se4 = requests.Session()
if response4.status_code == 200:
    print(response4.text)