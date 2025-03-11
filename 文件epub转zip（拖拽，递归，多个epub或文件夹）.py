# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.1
# 使用trae协助编写
# 源脚本来源https://moeshare.cc/read-htm-tid-328398.html

from pathlib import Path
import sys
import zipfile
import shutil
from typing import List, Union

# 图片文件后缀名
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif'}

def zipDir(dirPath: Path, zipFile: Path, originalName: str) -> None:
    """
    将指定目录压缩为 ZIP 文件，所有图片放在一个与原始epub同名的文件夹内
    """
    with zipfile.ZipFile(zipFile, 'w') as zipf:
        dirPath = Path(dirPath)
        for filePath in dirPath.rglob('*'):
            if filePath.is_file() and filePath.suffix.lower() in IMAGE_EXTENSIONS:
                arcname = Path(originalName) / filePath.name
                zipf.write(filePath, arcname)

def doConvert(fileName: Path) -> None:
    try:
        originalName = fileName.stem
        print(f"正在处理 {fileName}...")
        # 创建 ZIP 文件并解压缩
        baseName = fileName.stem
        newPath = fileName.parent / f"{baseName}.zip"
        count = 1
        while newPath.exists():
            newPath = fileName.parent / f"{baseName}_{count:02d}.zip"
            count += 1
        newPath.write_bytes(fileName.read_bytes())
        extractDir = newPath.parent / newPath.stem
        count = 1
        while extractDir.exists():
            extractDir = newPath.parent / f"{newPath.stem}_{count:02d}"
            count += 1
        with zipfile.ZipFile(newPath, 'r') as zipRef:
            zipRef.extractall(extractDir)

        # 重命名图片文件
        extractDir = Path(extractDir)
        for filePath in extractDir.rglob('*'):
            if filePath.is_file() and filePath.suffix.lower() in IMAGE_EXTENSIONS:
                target = extractDir / filePath.name
                count = 1
                while target.exists():
                    name = filePath.stem
                    ext = filePath.suffix
                    newName = f"{name}_{count:02d}{ext}"
                    target = extractDir / newName
                    count += 1
                filePath.rename(target)

        # 删除不需要的文件和目录
        for itemPath in list(extractDir.rglob('*')):
            if itemPath.is_dir():
                shutil.rmtree(itemPath)
            elif itemPath.is_file() and not itemPath.suffix.lower() in IMAGE_EXTENSIONS:
                itemPath.unlink()

        # 统计图片数量
        imageCount = sum(1 for _ in extractDir.rglob('*') if _.is_file() and _.suffix.lower() in IMAGE_EXTENSIONS)
        print(f"共 {imageCount} 张图片...")
                
        # 重新压缩为 ZIP 文件，传入原始文件名
        zipDir(extractDir, newPath, originalName)

        # 清理临时目录
        if extractDir.exists():
            shutil.rmtree(extractDir)
    except Exception as e:
        print(f"处理 {fileName} 时出现错误: {e}")

def main(inputPath: list[str]) -> None:
    fileType = {'.epub'}
    try:
        for eachPath in inputPath[1:]:
            eachPath = Path(eachPath)
            if eachPath.is_dir():
                for eachFile in eachPath.glob('**/*'):
                    if eachFile.suffix.lower() in fileType:
                        doConvert(eachFile)
            elif eachPath.is_file() and eachPath.suffix.lower() in fileType:
                doConvert(eachPath)
    except Exception as e:
        print(f'程序执行出错：{str(e)}')

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
        else:
            print('请拖拽文件到本脚本，或者命令行运行时添加文件路径')
    except IndexError:
        pass