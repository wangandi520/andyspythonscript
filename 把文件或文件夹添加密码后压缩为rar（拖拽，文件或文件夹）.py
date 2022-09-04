# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# 需要Rar.exe

from pathlib import Path
import sys
import os

def doAddToEncryptedRar(filePath):
    # type(filePath): Path
    # 设置密码为1234
    myPassword = '1234'
    # 新文件名 = 密码1234_ + 旧文件名.扩展名 + .rar
    newFileName = '密码' + myPassword + '_' + Path(filePath).name + '.rar'
    # 新文件名 = 密码1234_ + 旧文件名 + .rar
    #newFileName = '密码' + myPassword + '_' + Path(filePath).stem + '.rar'
    # 新文件名 = 旧文件名 + .rar
    # newFileName = Path(filePath).stem + '.rar'
    print('正在处理...' + filePath.name)
    # -ep不包含路径
    # -ep1包含一层目录
    # -m0压缩方式存储
    # -hp加密
    if Path.is_file(filePath):
        os.system('Rar.exe -ep -m0 -hp' + myPassword + ' a "' + str(filePath.parent.joinpath(newFileName)) + '" "' + str(filePath) + '"')
    if Path.is_dir(filePath):
        os.system('Rar.exe -ep1 -m0 -hp' + myPassword + ' a "' + str(filePath.parent.joinpath(newFileName)) + '" "' + str(filePath) + '"')
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