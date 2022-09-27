# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
    
def main(inputPath):
    allallFilePath = []
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            allFilePath = []
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file):
                    allFilePath.append(file)
            allFilePath.sort()     
            allallFilePath.append(allFilePath[-1])
    for eachFile in allallFilePath:
        print(eachFile)
    # 路径形式D:\\new，需要和移动的文件在同一个磁盘
    newFilePath = Path('D:\\new')
    myChoice = input('是否要移动以上文件到' + str(newFilePath) + ', (y)es or (n)o:')
    if myChoice.lower() in ['y', 'yes']:
        for eachFile in allallFilePath:
            newEachFilePath = newFilePath.joinpath(eachFile)
            # 是否重命名,是 = True， 否 = False
            ifRename = False
            # 文件名添加上上级文件夹的名字
            newName = newEachFilePath.parent.joinpath(newEachFilePath.parent.parent.name + ' ' + newEachFilePath.name)
            moveToPath = newFilePath.joinpath(newEachFilePath.name)
            if moveToPath.exists():
                print('文件已存在或重名')
            if not moveToPath.exists():
                if ifRename:
                    newEachFilePath.rename(newName)
                    Path(newName).replace(moveToPath)
                else:
                    Path(newEachFilePath).replace(moveToPath)
                
                
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass