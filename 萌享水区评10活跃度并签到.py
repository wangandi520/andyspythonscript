# encoding:utf-8

import requests
import time
import sys
import json
import calendar

暂时运行不了，待测试

# 本脚本原理：
# 使用cookie模拟登录，给帖子每层楼评分1活跃度，自己也获得1活跃度，10活跃度后签到
# 20220831，论坛改版，lv0,1,2每天能加的活跃度是1,2,5，所以现在需要用其他方式补充，lv3刚好每天10点
# 本脚本使用前提：
# 1.网上搜索，安装python和pip插件，在命令提示符输入pip install requests
# 2.账号能进入萌享会员自由交流区https://moeshare.cc/thread-htm-fid-16.html，不能进的话每天10活跃度签到，月底道具中心买全满勤奖后使用
# 3.cookie设置：
# 只需要填写下面的myCookie和myAgent，其他的不用改
# 萌享首页，chrome或edge按f12，网络，刷新页面，名称里选index.php，右侧请求标头，右键cookie和user-agent，复制值到下面myCookie和myAgent后，别忘了引号。
# myCookie只需复制8017a_c_stamp=前面的部分，例：
# someCookie = "8017a_ck_info=/	; 8017a_jobpop=1; 8017a_threadlog=,6,4,16,22,2,; 8017a_ckquestion=asdfaawgawegawegawegawegwaegawegawegawegawe; zh_choose=n; 8017a_winduser=awegwaegawegwaegawegawegawegawegwaeg; 8017a_ipstate=1658973831; 8017a_readlog=,241573,241587,; 8017a_c_stamp="
# someAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.70"

myCookie = ";;;;8017a_c_stamp="
myAgent = "Edg/103.0.1264.70"

# 水区帖子tid
tid = '211701'
page = '1'
# 帖子地址
url = 'https://moeshare.cc/read-htm-tid-' + tid + '-page-' + page + '.html'
mytime = int(round(time.time()))
newtimetmp = int(round(time.time() * 1000))
# 脚本累计加过的活跃度
addhuoyue = 0
headers = {"User-Agent": myAgent,
           "Cookie": myCookie + str(mytime) + "; 8017a_lastvisit=0	" + str(mytime) + "	/index.php"}
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取活跃度数值
jifenUrl = 'https://moeshare.cc/userpay.php'
response5 = requests.get(jifenUrl, headers=headers)
if response5.status_code == 200:
    tmpIndex5 = (response5.text).find('<li class="w mb5">活跃度')
    tmpIndex6 = (response5.text).find('<li class="w mb5">YQBD')
    tmpIndex7 = (response5.text).find('<li class="w mb5">本月打卡')
    huoyue = response5.text[tmpIndex5 + 18: tmpIndex6 - 6]
    daka = response5.text[tmpIndex7 + 23: tmpIndex5 - 6]
    print('本月打卡: ' + daka)
    try:
        huoyueNum = int(huoyue.split('：')[1])
    except IndexError:
        print('也许cookie设置错误。01')
        sys.exit()
    addhuoyue = addhuoyue + huoyueNum
    index = (response5.text).find('verifyhash')
    myveri = ((response5.text)[index + 14: index + 22])
    print('verifyhash :' + myveri)
    print(response5.text[tmpIndex5 + 18: tmpIndex6 - 6])
    time.sleep(3)
      
year = int(time.strftime("%Y", time.localtime()))
month = int(time.strftime("%m", time.localtime()))
today = int(time.strftime("%d", time.localtime()))
lastDay = calendar.monthrange(year, month)[1]

#if (daka == str(today) and lastDay == today):
if (huoyueNum >= 10):
    print('活跃 >= 10')
elif (daka == str(today)):
    print('今天已经打过卡了，by python.')
elif (daka != time.strftime("%d", time.localtime())):
    response = requests.get(url, headers=headers)
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
    mytime7 = int(round(time.time()))
    headers7 = {"User-Agent": myAgent,
                "Cookie": myCookie + str(mytime7) + "; 8017a_lastvisit=0	" + str(mytime7) + "	/index.php"}
    response7 = requests.get(url, headers=headers7)

    # 获取倒数第二页所有pid
    pidArray = []
    newStart = 0
    for i in range(0, 10 - addhuoyue):
        tmpIndex5 = (response7.text[newStart:]).find('showping_')
        tmpPid = ((response7.text[newStart:])[tmpIndex5 + 9: tmpIndex5 + 16])
        if not tmpPid.isdigit():
            print('PID 获取错误，不是数字：tmpPid = ' + tmpPid)
            sys.exit()
        newStart = newStart + tmpIndex5 + 16
        pidArray.append(tmpPid)

    # 添加活跃度
    if (index == -1):
        print('也许cookie设置错误。02')
    elif (index != -1):
        for eachPid in pidArray:
            newtime2 = int(round(time.time() * 1000))
            myreferer = 'https://moeshare.cc/read-htm-tid-211701-page-' + newpage + '.html'
            shuiquUrl = 'https://moeshare.cc/operate.php?action=showping&ajax=1&nowtime=' + \
                str(newtime2) + '&verify=' + myveri
            preCookie = myCookie.split('8017a_c_stamp')[0]
            addCookieUrl = ' 8017a_c_stamp="' + str(newtimetmp) + '"; 8017a_lastvisit=0	' + str(
                newtime2) + ' /operate.php?ajax1&actionshowping&tid211701&' + 'pid' + eachPid + '&page' + newpage + '&nowtime' + str(newtime2) + '&verify' + myveri
            newCookie = preCookie + addCookieUrl
            headers2 = {"User-Agent": myAgent,
                        "Cookie": newCookie,
                        "Referer": myreferer}
            formData = {
                "verify": myveri,
                "page": newpage,
                "tid": "211701",
                "selid[]": eachPid,
                "step": "1",
                "cid[]": "currency",
                "addpoint[]": "1"
            }
            response2 = requests.post(
                shuiquUrl, headers=headers2, data=formData)
            newtimetmp = newtime2
            if response2.status_code == 200:
                if ('活跃度' in response2.text):
                    addhuoyue = addhuoyue + 1
                    print('页数: ' + str(newpage) + ' PID: ' +
                          str(eachPid) + ' 活跃度： ' + str(addhuoyue))
                else:
                    print('页数: ' + str(newpage) + ' PID: ' +
                          str(eachPid) + ' Error: ' + response2.text)
            time.sleep(3)

# def writefile(filereadlines):
    # # write file
    # newfile = open('/srv/script/meng_qiandao.json', mode='w', encoding='UTF-8')
    # newfile.writelines(filereadlines)
    # newfile.close()

# 签到
# if (huoyueNum >= 10):
mytime3 = int(round(time.time()))
headers3 = {"User-Agent": myAgent,
            "Cookie": myCookie + str(mytime3) + "; 8017a_lastvisit=0	" + str(mytime3) + "	/index.php"}
qiandaoUrl = 'https://moeshare.cc/jobcenter.php?action=punch&step=2'
response4 = requests.get(qiandaoUrl, headers=headers3)
if response4.status_code == 200:
    if ('打卡成功' in response4.text):
        print('打卡成功!获得 2MB。' +
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')
        #outputData = {'meng_qiandao': time.strftime("%Y-%m-%d", time.localtime())}
        #writefile(json.dumps(outputData))
input()