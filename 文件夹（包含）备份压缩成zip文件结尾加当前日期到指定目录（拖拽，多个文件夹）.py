# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.1

from pathlib import Path
import sys
import zipfile
import datetime

# 把可以更改的设置都放在这里
CONFIG = {
    # 需要备份的文件夹路径，格式：r'D:\new01',r'D:\new02'
    "allFolderPath": [
        r'D:\new01',
        r'D:\new02'
    ],
    # 压缩包保存的路径（如为空则保存在目标文件夹同级目录）
    "zipSaveDir": r'D:\backup'
}

def doZipFolder(inputPath):
    print(f"开始压缩文件夹: {inputPath}")
    # 每个文件夹压缩成zip文件，包含这个文件夹，zip文件=文件夹名
    # 压缩方式：存储（速度最快），体积和压缩前差不多
    myZipType = zipfile.ZIP_STORED
    # 压缩方式：标准（速度一般），体积会变小
    #myZipType = zipfile.ZIP_DEFLATED
    # 保存位置：在脚本所在的目录
    #myZipSavePath = inputPath.stem + '.zip'
    # getTime，格式如：2025年05月05日23时11分11秒
    getTime = datetime.datetime.now().strftime("%Y年%m月%d日%H时%M分%S秒")
    zip_name = inputPath.stem + getTime + '.zip'
    zip_save_dir = CONFIG.get("zipSaveDir")
    if zip_save_dir:
        myZipSavePath = Path(zip_save_dir).joinpath(zip_name)
    else:
        myZipSavePath = inputPath.parent.joinpath(zip_name)
    myZipFile = zipfile.ZipFile(myZipSavePath, 'w', myZipType)
    print('正在新建压缩文件：' + str(myZipSavePath))
    for eachFilePath in inputPath.glob('**/*'):
        myZipFile.write(eachFilePath, eachFilePath.relative_to(inputPath.parent))
    myZipFile.close()
    print(f"完成压缩: {myZipSavePath}\n")

def main():
    folder_list = CONFIG["allFolderPath"]
    print("开始批量压缩文件夹")
    print(f"需要备份的文件夹数量: {len(folder_list)}")
    print(f"压缩包保存路径: {CONFIG.get('zipSaveDir') or '目标文件夹同级目录'}")
    for aPath in folder_list:
        if Path(aPath).is_dir():
            doZipFolder(Path(aPath))
        else:
            print(f"跳过（不是文件夹或不存在）: {aPath}")
    print("所有任务完成")
    input('按任意键继续...')

if __name__ == '__main__':
    try:
        main()
    except IndexError:
        print("发生异常，程序退出。")