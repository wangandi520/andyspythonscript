# encoding:utf-8
# pip install requests

import requests
import time

# 使用github的action离线签到，见https://andi.wang/2024/02/11/%E4%BD%BF%E7%94%A8github%E7%9A%84action%E9%85%8D%E5%90%88python%E6%AF%8F%E5%A4%A9%E7%AD%BE%E5%88%B0/
# 时间
currentTime = str(int(round(time.time())))
# 状态
myHeader = {
"User-Agent": "chrome或其他浏览器F12，刷新网页，点上面网络，下面选一个php页面或其他，右侧标头，复制里面的user-agent",
"Cookie": "同上，复制里面的cookie，如果有类似1657208800的十位数字，用上面的currentTime参数代替，注意引号",
"Referer": "同上，复制里面的referer，可不填"}
# 显示当前时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 签到按钮的网址，F12查看，有的网站比较隐蔽
qiandaoUrl = 'https://www.xx.com/plugin.php'
# F12，网络，点击网址，右侧负载。可忽略
myData = {
                "formhash": "abcdefgh",
                "todaysay": "天气不错签到一下",
                "fastreply": "1"
            }
response = requests.get(qiandaoUrl, headers=myHeader, data=myData)
if response.status_code == 200:
    print(response.text)
    