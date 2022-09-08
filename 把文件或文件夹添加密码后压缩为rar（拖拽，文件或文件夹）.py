# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# 需要Rar.exe

from pathlib import Path
import sys
import os
import random
import string

def doAddToEncryptedRar(filePath):
    # type(filePath): Path
    # randomPassword = 0时设置密码为1234，randomPassword = N（N >= 1）设置为随机N位数密码
    randomPassword = 16
    if randomPassword > 0:
        tempPunctuation = string.punctuation
        for each in tempPunctuation:
            if each in '\/:*?"<>|,':
                tempPunctuation = tempPunctuation.replace(each, '')
        # 密码组合：字母+数字+符号
        passwordComponent = string.ascii_letters + string.digits + tempPunctuation
        # 密码长度
        passwordLength = randomPassword
        # 生成密码
        passwordGenerate = random.sample(passwordComponent, passwordLength)
        myPassword = ''.join(passwordGenerate)
    elif  randomPassword == 0:
        myPassword = '1234'
    # 新文件名 = N位密码1234_ + 旧文件名.扩展名 + .rar
    newFileName = str(len(myPassword)) + '位密码' + myPassword + '文件名' + Path(filePath).name + '.rar'
    # 新文件名 = N位密码1234_ + 旧文件名 + .rar
    #newFileName = str(len(myPassword)) + '位密码' + myPassword + '文件名' + Path(filePath).stem + '.rar'
    # 新文件名 = 旧文件名 + .rar
    # newFileName = Path(filePath).stem + '.rar'
    print('正在处理...' + filePath.name)
    # -ep 不包含路径
    # -ep1 包含一层目录
    # -m0 压缩方式存储
    # -hp 加密
    # -rr3p 添加3%恢复记录-_+=.,
    if Path.is_file(filePath):
        os.system('Rar.exe -rr3p -ep -m0 -hp' + myPassword + ' a "' + str(filePath.parent.joinpath(newFileName)) + '" "' + str(filePath) + '"')
    if Path.is_dir(filePath):
        os.system('Rar.exe -rr3p -ep1 -m0 -hp' + myPassword + ' a "' + str(filePath.parent.joinpath(newFileName)) + '" "' + str(filePath) + '"')
    print('完成')
            
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        doAddToEncryptedRar(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass