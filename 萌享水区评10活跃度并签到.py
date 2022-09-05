# encoding:utf-8

import requests
import time
import sys
import json
import calendar
import math

# 本脚本原理：
# 使用cookie模拟登录，给帖子每层楼评分1活跃度，自己也获得1活跃度，10活跃度后签到
# 20220831，论坛改版，lv0,1每天能加的活跃度是2,5，所以现在需要用其他方式补充，lv2刚好每天10点
# 新脚本会把在线时间转换成缺少的活跃度，如果你是lv1，可以加5点活跃，需要有3以上的在线时间才能签到成功
# 保存时间：https://moeshare.cc/hack.php?H_name=integral，换成活跃度：https://moeshare.cc/userpay.php?action=change
# 本脚本使用前提：
# 1.网上搜索，安装python和pip插件，在命令提示符输入pip install requests
# 2.账号能进入萌享会员自由交流区https://moeshare.cc/thread-htm-fid-16.html，每天10活跃度签到，月底道具中心买全满勤奖后使用
# 3.cookie设置：
# 只需要填写下面的myCookie和myAgent，其他的不用改
# 萌享首页，chrome或edge按f12，网络，刷新页面，名称里选index.php，右侧请求标头，右键cookie和user-agent，复制值到下面myCookie和myAgent后，别忘了引号。
# myCookie只需复制8017a_c_stamp=前面的部分，例：
# someCookie = "8017a_ck_info=/	; 8017a_jobpop=1; 8017a_threadlog=,6,4,16,22,2,; 8017a_ckquestion=asdfaawgawegawegawegawegwaegawegawegawegawe; zh_choose=n; 8017a_winduser=awegwaegawegwaegawegawegawegawegwaeg; 8017a_ipstate=1658973831; 8017a_readlog=,241573,241587,; 8017a_c_stamp="
# someAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.70"

myCookie = "8017a_c_stamp="

myAgent = "Edg/103.0.1264.70"

# 水区帖子tid
tid = '211701'
page = '1'
# 帖子地址
url = 'https://moeshare.cc/read-htm-tid-' + tid + '-page-' + page + '.html'
# 时间戳
mytime = int(round(time.time()))
newtimetmp = int(round(time.time() * 1000))
# 脚本累计加过的活跃度
huoyueAddedByScript = 0
# 登录信息
headers = {"User-Agent": myAgent,
           "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
#当前时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取用户等级
myUrl = 'https://moeshare.cc/u.php'
response6 = requests.get(myUrl, headers=headers)
# 我的等级
myLevel = 0
# 我的等级每日可用活跃度
eachLevelHuoyue = 0
if response6.status_code == 200:
    tmpIndex11 = (response6.text).find('>Lv')
    myLevel = int(response6.text[tmpIndex11 + 4 : tmpIndex11 + 5])
    huoyueArray = [2, 5, 10, 20, 50, 100]
    eachLevelHuoyue = huoyueArray[myLevel]
    print('用户等级：Lv.' + str(myLevel) + '。每日可用活跃度：' + str(eachLevelHuoyue))
    time.sleep(3)
    
# 获取活跃度数值
jifenUrl = 'https://moeshare.cc/userpay.php'
response5 = requests.get(jifenUrl, headers=headers)
if response5.status_code == 200:
    tmpIndex5 = (response5.text).find('<li class="w mb5">活跃度')
    tmpIndex6 = (response5.text).find('<li class="w mb5">YQBD')
    tmpIndex7 = (response5.text).find('<li class="w mb5">本月打卡')
    tmpIndex8 = (response5.text).find('<li class="w mb5">在线时间')
    tmpIndex9 = (response5.text).find('<h5 class="h5"><a class="fr" href="userpay.php?action=log">进入积分日志')
    getHuoyueNum = response5.text[tmpIndex5 + 18: tmpIndex6 - 6]
    daka = response5.text[tmpIndex7 + 23: tmpIndex5 - 6]
    onlineTime = response5.text[tmpIndex8 + 23: tmpIndex9 - 12]
    print('本月打卡: ' + daka)
    print('在线时间: ' + onlineTime)
    try:
        huoyueAddedByScript = int(getHuoyueNum.split('：')[1])
    except IndexError:
        print('也许cookie设置错误。01')
        sys.exit()
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
if (daka == str(today)):
    print('今天已经打过卡了。')
elif (huoyueAddedByScript >= 10):
    print('活跃 >= 10')
elif (daka != time.strftime("%d", time.localtime())):
    headers2 = {"User-Agent": myAgent,
           "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
    response = requests.get(url, headers=headers2)
    if (' ' in myveri):
        print('Cookie 获取出错: veryify = ' + myveri + ' (8位数字字母组合且无空格)')
        sys.exit()

    # 获取MD MB
    try:
        tmpIndex2 = (response.text).find('枚</a>')
        tmpIndex3 = (response.text).find('点</a>')
        getMB = (response.text)[tmpIndex2 - 8: tmpIndex2].split('>')[1]
        getMD = (response.text)[tmpIndex3 - 8: tmpIndex3].split('>')[1]
        print('现在MB: ' + getMB + ' MD: ' + getMD)
    except IndexError:
        print('MB,MD获取异常')
    time.sleep(3)

    # 获取倒数第二页数=最新页数-1
    tmpIndex = (response.text).find('<div class="fl">共')
    # 第几页
    newpage = str(int((response.text)[tmpIndex + 17: tmpIndex + 21]) - 1)
    url = 'https://moeshare.cc/read-htm-tid-' + tid + '-page-' + newpage + '.html'
    headers7 = {"User-Agent": myAgent,
                "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
    response7 = requests.get(url, headers=headers7)

    # 获取倒数第二页所有pid
    pidArray = []
    newStart = 0
    if eachLevelHuoyue >= 10:
        for i in range(0, 10 - huoyueAddedByScript):
            tmpIndex5 = (response7.text[newStart:]).find('showping_')
            tmpPid = ((response7.text[newStart:])[tmpIndex5 + 9: tmpIndex5 + 16])
            if not tmpPid.isdigit():
                print('PID 获取错误，不是数字：tmpPid = ' + tmpPid)
                sys.exit()
            newStart = newStart + tmpIndex5 + 16
            pidArray.append(tmpPid)
    if eachLevelHuoyue < 10:
        for i in range(0, eachLevelHuoyue):
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
                    huoyueAddedByScript = huoyueAddedByScript + 1
                    print('页数: ' + str(newpage) + ' PID: ' +
                          str(eachPid) + ' 活跃度： ' + str(huoyueAddedByScript))
                elif ('不能超过您的评分上限' in response2.text):
                    break;
                else:
                    print('页数: ' + str(newpage) + ' PID: ' +
                          str(eachPid) + ' Error: ' + response2.text)
            time.sleep(3)
            
    # 在线时间转换成活跃度
    saveOnlineTimeUrl = 'https://moeshare.cc/hack.php?H_name=integral&action=save'
    formData3 = {
        "integralsubmit": '1',
        "Submit": '保存积分'
    }
    headers = {"User-Agent": myAgent,
           "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
    response12 = requests.post(saveOnlineTimeUrl, headers=headers, data=formData3)
    if response12.status_code == 200:
        if ('可以保存的积分小于1') in response12.text:
            print('可以保存的现在时间小于1')
        elif ('一共转存了'):
            print('转存成功')
    time.sleep(3)
    
    if int(onlineTime) / 2 + 1 > 10 - huoyueAddedByScript:
        onlineTimeToHuoyueUrl = 'https://moeshare.cc/userpay.php?action=change&'
        transOnTime = str(math.ceil((10 - huoyueAddedByScript) / 2))
        formData2 = {
            "step": '3',
            "type": '3_currency',
            "verify": myveri,
            "change": transOnTime
        }
        print(transOnTime + '在线时间转换成活跃度')
        headers = {"User-Agent": myAgent,
           "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
        response13 = requests.post(onlineTimeToHuoyueUrl, headers=headers, data=formData2)
        if response13.status_code == 200:
            if ('完成积分转换') in response13.text:
                print(response13.text)
                huoyueAddedByScript = huoyueAddedByScript + int(transOnTime)
    time.sleep(3)

# def writefile(filereadlines):
    # # 写入日志文件
    # newfile = open('/srv/script/meng_qiandao.json', mode='w', encoding='UTF-8')
    # newfile.writelines(filereadlines)
    # newfile.close()

# 签到
if (huoyueAddedByScript >= 10):
    headers13 = {"User-Agent": myAgent,
                "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
    qiandaoUrl = 'https://moeshare.cc/jobcenter.php?action=punch&step=2'
    response13 = requests.get(qiandaoUrl, headers=headers13)
    if response13.status_code == 200:
        if ('打卡成功' in response13.text):
            print('打卡成功!获得 2MB。' +
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')
            #outputData = {'meng_qiandao': time.strftime("%Y-%m-%d", time.localtime())}
            #writefile(json.dumps(outputData))
input()