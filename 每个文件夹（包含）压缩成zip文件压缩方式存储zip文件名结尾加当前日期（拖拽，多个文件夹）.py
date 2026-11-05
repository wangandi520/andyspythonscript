# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.3

from pathlib import Path
import sys
import zipfile
import datetime

# 把可以更改的设置都放在这里
CONFIG = {
    "zipSaveDir": r'D:\backup' # 如果填. 就是保存在文件夹同级目录
}

def doZipFolder(inputPath):
    # 每个文件夹压缩成zip文件，包含这个文件夹，zip文件=文件夹名
    # 压缩方式：存储（速度最快），体积和压缩前差不多
    myZipType = zipfile.ZIP_STORED
    # 压缩方式：标准（速度一般），体积会变小
    #myZipType = zipfile.ZIP_DEFLATED
    # getTime，%Y%m%d%H%M%S分别是年月日时分秒，可以替换成自己需要的格式
    getTime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zipSaveDir = Path(CONFIG["zipSaveDir"])
    if CONFIG["zipSaveDir"] == ".":
        zipSaveDir = inputPath.parent
    zipSaveDir.mkdir(parents=True, exist_ok=True)
    myZipSavePath = zipSaveDir / (inputPath.stem + '_' + getTime + '.zip')
    print('正在新建压缩文件：' + str(myZipSavePath))
    with zipfile.ZipFile(myZipSavePath, 'w', myZipType) as myZipFile:
        for eachFilePath in inputPath.glob('**/*'):
            myZipFile.write(eachFilePath, eachFilePath.relative_to(inputPath.parent))

def main(inputPath):
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            doZipFolder(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass