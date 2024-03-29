# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install opencv-python

import cv2
import time
import re

# 萤石摄像头地址rtsp://用户名:密码@ip地址:554/h264/ch1/main/av_stream，
# 萤石摄像头开启rtsp，手机萤石云视频app，我的，工具，局域网设备预览，开始扫描，选择设备，密码是6位大写英文，在摄像头下面贴纸上
# crontab每五分钟运行 */5 * * * *
rtspUrl = ['rtsp://用户名:密码@ip地址01', 'rtsp://用户名:密码@ip地址02']
for eachUrl in rtspUrl:
    # 提取ip地址命名截图
    checkIP = re.compile(r"((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))")
    getIP = checkIP.search(eachUrl)
    if getIP:
        print('正在截图' + getIP.group())
        imageName = time.strftime(getIP.group() + "_%Y%m%d_%H%M%S", time.localtime()) + '.png'
    else:
        print('正在截图')
        imageName = time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.png'
    VideoCap = cv2.VideoCapture(eachUrl)
    ret, frame = VideoCap.read()
    if ret:
        cv2.imwrite(imageName, frame)
        print('截图成功')
    VideoCap.release()