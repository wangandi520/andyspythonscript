# encoding:utf-8

import requests
import time
import sys
import json
import calendar
import math

# 使用github的action离线签到，见https://andi.wang/2024/02/11/%E4%BD%BF%E7%94%A8github%E7%9A%84action%E9%85%8D%E5%90%88python%E6%AF%8F%E5%A4%A9%E7%AD%BE%E5%88%B0/
# 本脚本原理：
# 使用cookie模拟登录，给帖子每层楼评分1活跃度，自己也获得1活跃度，10活跃度后签到
# 20240531，论坛改版，lv0，1，2每天能加的活跃度是1，2，6，所以现在需要用其他方式补充，lv3才可以正常使用这个脚本
# 新脚本会把时辰转换成缺少的活跃度，如果你是lv1，可以加5点活跃，需要有3以上的时辰才能签到成功
# 保存时间：https://moeshare.cc/hack.php?H_name=integral，换成活跃度：https://moeshare.cc/userpay.php?action=change
# 本脚本使用前提：
# 1.网上搜索，安装python和pip插件，在命令提示符输入pip install requests
# 2.账号能进入萌享会员自由交流区https://moeshare.cc/thread-htm-fid-16.html，每天10活跃度签到，月底道具中心买全满勤奖后使用
# 3.确定签到步骤，30和32行
# 4.cookie设置：
# 只需要填写下面的myCookie和myAgent，其他的不用改
# 萌享首页，chrome或edge按f12，网络，刷新页面，名称里选index.php，右侧请求标头，右键cookie和user-agent，复制值到下面myCookie和myAgent后，别忘了引号。
# myCookie只需复制8017a_c_stamp=前面的部分，例：
# myCookie = "8017a_ck_info=/	; 8017a_jobpop=1; 8017a_threadlog=,6,4,16,22,2,; 8017a_ckquestion=asdfaawgawegawegawegawegwaegawegawegawegawe; zh_choose=n; 8017a_winduser=awegwaegawegwaegawegawegawegawegwaeg; 8017a_ipstate=1658973831; 8017a_readlog=,241573,241587,; 8017a_c_stamp="
# myAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.70"

myCookie = "8017a_c_stamp="

myAgent = ""

myProxies = {
    'https': '',
    'http': ''  
}
# myProxies = {
    # 'https': 'http://127.0.0.1:7890',
    # 'http': 'http://127.0.0.1:7890'  
# }

# 是否回复一帖，回复一次+1活跃度，是 = True，否 = False
ifReply = True
# 是否保存时辰
ifSaveTime = True
# 是否把时辰转换成缺少活跃度，1时辰 = 2活跃度，是 = True，否 = False
ifOnlineTimeToHuoyue = False
# 不管活跃度多少，都用掉全部可以评价的数量
ifUseAllHuoyue = True
# 水区帖子tid，第一个用于加活跃度，全部帖都会回复，回复几贴加几活跃度
tid = ['211701', '211817']
# 每一帖回复的内容，相邻的内容不能一样，数量和tid数量一致
myReply = ['先水一帖，每天打卡活跃下。',
        '先水水帖，今天打卡活跃下。']
if ifReply and len(tid) != len(myReply):
    print('myReply和tid长度不一致。')
page = '1'
# 帖子地址，tid[0]
url = 'https://moeshare.cc/read-htm-tid-' + tid[0] + '-page-' + page + '.html'
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
myUrl = 'https://moeshare.cc/index.php'
#response6 = requests.get(myUrl, headers=headers)
response6 = requests.get(myUrl, proxies = myProxies, headers=headers)
# 我的等级
myLevel = 0
# 我的等级每日可用活跃度
eachLevelHuoyue = 0
if response6.status_code == 200:
    tmpIndex11 = (response6.text).find('>Lv')
    myLevel = int(response6.text[tmpIndex11 + 4 : tmpIndex11 + 5])
    huoyueArray = [1, 2, 6, 20, 40, 100]
    eachLevelHuoyue = huoyueArray[myLevel]
    print('用户等级：Lv.' + str(myLevel) + '。每日可用活跃度：' + str(eachLevelHuoyue))
    time.sleep(3)
    
# 获取活跃度数值
headers = {"User-Agent": myAgent,
           "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
jifenUrl = 'https://moeshare.cc/userpay.php'
#response5 = requests.get(jifenUrl, headers=headers)
response5 = requests.get(jifenUrl, proxies = myProxies, headers=headers)
if response5.status_code == 200:
    tmpIndex5 = (response5.text).find('<li class="w mb5">活跃度')
    tmpIndex6 = (response5.text).find('<li class="w mb5">YQBD')
    tmpIndex7 = (response5.text).find('<li class="w mb5">本月打卡')
    tmpIndex8 = (response5.text).find('<li class="w mb5">时辰')
    tmpIndex9 = (response5.text).find('<h5 class="h5"><a class="fr" href="userpay.php?action=log">进入积分日志')
    getHuoyueNum = response5.text[tmpIndex5 + 18: tmpIndex6 - 6]
    daka = response5.text[tmpIndex7 + 23: tmpIndex5 - 6]
    onlineTime = response5.text[tmpIndex8 + 21: tmpIndex9 - 12]
    print('本月打卡: ' + daka)
    print('时辰: ' + onlineTime)
    try:
        huoyueAddedByScript = int(getHuoyueNum.split('：')[1])
        print('现在活跃度：' + str(huoyueAddedByScript))
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
# if (daka == str(today)):
    # print('今天已经打过卡了。')
# elif (huoyueAddedByScript >= 10):
    # print('活跃度 >= 10')
# elif (daka != time.strftime("%d", time.localtime()) and (ifReply and (huoyueAddedByScript < 10 - len(tid)))):
if (daka == str(today)):
    print('今天已经打过卡了。')
if (huoyueAddedByScript >= 10):
    print('活跃度 >= 10')
if ifUseAllHuoyue:
    headers2 = {"User-Agent": myAgent,
           "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
    #response = requests.get(url, headers=headers2)
    response = requests.get(url, proxies = myProxies, headers=headers2)
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
    url = 'https://moeshare.cc/read-htm-tid-' + tid[0] + '-page-' + newpage + '.html'
    headers7 = {"User-Agent": myAgent,
                "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
    #response7 = requests.get(url, headers=headers7)
    response7 = requests.get(url, proxies = myProxies, headers=headers7)

    # 获取倒数第二页所有pid
    pidArray = []
    newStart = 0
    #if eachLevelHuoyue >= 10:
        #for i in range(0, 10 - huoyueAddedByScript):
        # for i in range(0, 10):
            # tmpIndex5 = (response7.text[newStart:]).find('showping_')
            # tmpPid = ((response7.text[newStart:])[tmpIndex5 + 9: tmpIndex5 + 16])
            # if not tmpPid.isdigit():
                # print('PID 获取错误，不是数字：tmpPid = ' + tmpPid)
                # sys.exit()
            # newStart = newStart + tmpIndex5 + 16
            # pidArray.append(tmpPid)
    #if eachLevelHuoyue < 10:
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
            myreferer = 'https://moeshare.cc/read-htm-tid-' + tid[0] + '-page-' + newpage + '.html'
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
                "tid": tid[0],
                "selid[]": eachPid,
                "step": "1",
                "cid[]": "currency",
                "addpoint[]": "1"
            }
            response2 = requests.post(
                shuiquUrl, proxies = myProxies,headers=headers2, data=formData)
                #shuiquUrl, headers=headers2, data=formData)
            newtimetmp = newtime2
            if response2.status_code == 200:
                if ('活跃度' in response2.text):
                    huoyueAddedByScript = huoyueAddedByScript + 1
                    print('页数: ' + str(newpage) + ' PID: ' +
                          str(eachPid) + ' 活跃度： ' + str(huoyueAddedByScript))
                elif ('不能超过您的评分上限' in response2.text):
                    print('不能超过您的评分上限')
                    break;
                else:
                    print('页数: ' + str(newpage) + ' PID: ' +
                          str(eachPid) + ' Error: ' + response2.text)          
            time.sleep(3)
        
        print('现在活跃度：' + str(huoyueAddedByScript))
    
    # 保存时辰
    if ifSaveTime:
        saveOnlineTimeUrl = 'https://moeshare.cc/hack.php?H_name=integral&action=save'
        formData3 = {
            "integralsubmit": '1',
            "Submit": '保存积分'
        }
        headers = {"User-Agent": myAgent,
               "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
        #response12 = requests.post(saveOnlineTimeUrl, headers=headers, data=formData3)
        response12 = requests.post(saveOnlineTimeUrl, proxies = myProxies, headers=headers, data=formData3)
        if response12.status_code == 200:
            if ('可以保存的积分小于1') in response12.text:
                print('可以保存的现在时间小于1')
            elif ('一共转存了'):
                print('转存成功')
        time.sleep(3)

    # 时辰转换成活跃度
    if ifOnlineTimeToHuoyue:
        if int(onlineTime) / 2 + 1 > 10 - huoyueAddedByScript:
            onlineTimeToHuoyueUrl = 'https://moeshare.cc/userpay.php?action=change&'
            transOnTime = str(math.ceil((10 - huoyueAddedByScript) / 2))
            formData2 = {
                "step": '3',
                "type": '3_currency',
                "verify": myveri,
                "change": transOnTime
            }
            print(transOnTime + '时辰转换成活跃度')
            headers = {"User-Agent": myAgent,
               "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
            #response13 = requests.post(onlineTimeToHuoyueUrl, headers=headers, data=formData2)
            response13 = requests.post(onlineTimeToHuoyueUrl, proxies = myProxies, headers=headers, data=formData2)
            if response13.status_code == 200:
                if ('完成积分转换') in response13.text:
                    print('完成积分转换')
                    huoyueAddedByScript = huoyueAddedByScript + int(transOnTime)
                    print('现在活跃度：' + str(huoyueAddedByScript))
        else:
            print('时辰不足，无法签到')
        time.sleep(3)
        
# 回复一帖
if ifReply:
    for eachIndex in range(0, len(tid)):
        replyUrl = 'https://moeshare.cc/post.php?fid=16&nowtime=' + str(int(round(time.time()))) + '&verify=' + myveri
        formData3 = {
            'atc_usesign': '1',
            'replytouser': '',
            'atc_convert': '1',
            'atc_autourl': '1',
            'step': '2',
            'type': 'ajax_addfloor',
            'action': 'reply',
            'fid': '16',
            'cyid': '',
            'tid': tid[eachIndex],
            'stylepath': 'wind8black',
            'ajax': '1',
            'verify': myveri,
            '_hexie': 'd8507211',
            'iscontinue': '0',
            'atc_title': '',
            'atc_content': myReply[eachIndex],
            'attachment_1': '(二进制)',
            'atc_desc1': ''
        }
        headers = {"User-Agent": myAgent,
           "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
        #response14 = requests.post(replyUrl, headers=headers, data=formData3)
        response14 = requests.post(replyUrl, proxies = myProxies, headers=headers, data=formData3)
        if response14.status_code == 200:
            if (myReply[eachIndex]) in response14.text:
                print('tid=' + tid[eachIndex] + '回帖成功')
                huoyueAddedByScript = huoyueAddedByScript + 1
                print('现在活跃度：' + str(huoyueAddedByScript))
        print('15秒后回复下一帖')
        time.sleep(15)
    
# def writefile(filereadlines):
    # # 写入日志文件
    # newfile = open('/srv/script/meng_qiandao.json', mode='w', encoding='UTF-8')
    # newfile.writelines(filereadlines)
    # newfile.close()

# 签到
if (huoyueAddedByScript >= 10 and (daka != str(today))):
    headers13 = {"User-Agent": myAgent,
                "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastvisit=0	" + str(int(round(time.time()))) + "	/index.php"}
    qiandaoUrl = 'https://moeshare.cc/jobcenter.php?action=punch&step=2'
    #response13 = requests.get(qiandaoUrl,headers=headers13)
    response13 = requests.get(qiandaoUrl, proxies = myProxies, headers=headers13)
    if response13.status_code == 200:
        if ('打卡成功' in response13.text):
            print('打卡成功!获得 2MB。' +
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            #outputData = {'meng_qiandao': time.strftime("%Y-%m-%d", time.localtime())}
            #writefile(json.dumps(outputData))
print('签到完成')   
