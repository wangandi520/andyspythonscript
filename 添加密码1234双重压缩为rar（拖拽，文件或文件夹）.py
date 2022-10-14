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
    rarFilePath = 'Rar.exe'
    # ifDoubleZip 是否双重压缩，是 = True，否 = False
    ifDoubleZip = False
    if not ifDoubleZip:
        # 单次压缩的情况下，文件名只显示原文件名 = True，否 = False
        showOnlyFileName = True
    # 文件名显示密码 = True， 不显示密码 = False
    ifShowPasswordInFilename = True
    # 是否删除第一次压缩的文件，是 = True，否 = False
    ifDeleteFirstZipFileName = False
    # 设置成随机N位密码，还是自定义密码
    # setPasswordTypeAndLength = 0时设置密码为1234或自定义，setPasswordTypeAndLength = N（N >= 1）设置成随机N位密码
    setPasswordTypeAndLength = 0
    if setPasswordTypeAndLength == 0:
        # 设置自定义密码，默认为1234
        myPassword = '1234'
    elif setPasswordTypeAndLength > 0:
        tempPunctuation = string.punctuation
        for each in tempPunctuation:
            if each in '\/:*?"<>|,':
                tempPunctuation = tempPunctuation.replace(each, '')
        # 密码组合：字母+数字
        passwordComponent = string.ascii_letters + string.digits
        # 密码组合：字母+数字+符号
        #passwordComponent = string.ascii_letters + string.digits + tempPunctuation
        # 密码长度
        passwordLength = setPasswordTypeAndLength
        # 生成密码
        passwordGenerate = random.sample(passwordComponent, passwordLength)
        myPassword = ''.join(passwordGenerate)
    if ifShowPasswordInFilename:
        showmyPassword = '[' + str(len(myPassword)) + '位密码' + myPassword + ']'
    else:
        showmyPassword = ''
    # 一次压缩文件名
    if not ifDoubleZip and showOnlyFileName:
        # 不显示原扩展名，把.name改成.stem
        newFileName01 = Path(filePath).name + '.rar'
    else:
        newFileName01 = '[一次压缩]' + showmyPassword + '[文件名' + Path(filePath).name + '].rar'
    print('正在第一次压缩...' + filePath.name)
    # -ep 不包含路径
    # -ep1 包含一层目录
    # -m0 压缩方式存储
    # -hp 加密
    # -rr3p 添加3%恢复记录
    if Path.is_file(filePath):
        firstZipFileName = filePath.parent.joinpath(newFileName01)
        os.system(rarFilePath + ' -rr3p -ep -m0 -hp' + myPassword + ' a "' + str(firstZipFileName) + '" "' + str(filePath) + '"')
    if Path.is_dir(filePath):
        isDir = True
        firstZipFileName = filePath.parent.joinpath(newFileName01)
        os.system(rarFilePath + ' -rr3p -ep1 -m0 -hp' + myPassword + ' a "' + str(firstZipFileName) + '" "' + str(filePath) + '"')
    if ifDoubleZip:
        # 二次压缩文件名
        newFileName02 =  '[二次压缩]' + showmyPassword + '[文件名' + Path(filePath).name + '].rar'
        print('正在第二次压缩...' + firstZipFileName.name) 
        secondZipFileName = firstZipFileName.parent.joinpath(newFileName02)
        os.system(rarFilePath + ' -ep -m0 -hp' + myPassword + ' a "' + str(secondZipFileName) + '" "' + str(firstZipFileName) + '"')
        # 是否删除第一次压缩的文件
        if ifDeleteFirstZipFileName:
            firstZipFileName.unlink()
    print('完成')
            
def main(inputPath):
    for aPath in inputPath[1:]:
        doAddToEncryptedRar(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass