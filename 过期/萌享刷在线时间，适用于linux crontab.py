# encoding:utf-8

import requests
import time

# 本脚本使用前提：
# 1.网上搜索，安装python和pip插件，在命令提示符输入pip install schedule requests
# 2.cookie设置：
# 只需要填写下面的myCookie和myAgent，如果无法访问url，可以试着改成其他帖子的地址，其他的不用改
# 萌享首页，chrome或edge按f12，网络，刷新页面，名称里选index.php，右侧请求标头，右键cookie和user-agent，复制值到下面myCookie和myAgent后，别忘了引号。
# myCookie只需复制8017a_c_stamp=前面的部分，例：
# someCookie = "8017a_ck_info=/	; 8017a_jobpop=1; 8017a_threadlog=,6,4,16,22,2,; 8017a_ckquestion=xxxxxxxxxxxxxxxxxxxxxxx; zh_choose=n; 8017a_winduser=xxxxxxxxxxxxxxxxxxxxxxx; 8017a_ipstate=1658973831; 8017a_c_stamp="
# someAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.131 Safari/537.36 Edg/103.0.1264.70"

timeInterval = 5
myCookie = "8017a_c_stamp="

myAgent = ""

# 帖子地址
url = 'https://moeshare.cc/hack.php?H_name=integral'

headers = {"User-Agent": myAgent,
           "Cookie": myCookie + str(int(round(time.time()))) + "; 8017a_lastpos=index;  8017a_lastvisit=566	" + str(int(round(time.time())) - timeInterval * 60) + "	/index.php"}

#session = requests.session()
response = requests.post(url, headers=headers)
if response.status_code == 200:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
