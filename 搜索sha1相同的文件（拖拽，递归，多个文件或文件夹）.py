# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
from hashlib import sha1
import sys

def getSha1(filename):
    sha1Obj = sha1()
    with open(filename, 'rb') as f:
        sha1Obj.update(f.read())
    return sha1Obj.hexdigest()
    
def main(inputPath):

    # 显示完整路径 = True，只显示文件名 = False
    showAllLocation = True
    
    fileSha1 = {}
    
    del inputPath[0]
    print()
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file):
                    tmpSha1 = getSha1(file)
                    if (tmpSha1 not in fileSha1):
                        if (showAllLocation):
                            fileSha1[tmpSha1] = Path(file).parent.joinpath(file)
                        if (not showAllLocation):
                            fileSha1[tmpSha1] = file.name
                    elif (tmpSha1 in fileSha1):
                        if (showAllLocation):
                            print(str(fileSha1[tmpSha1]))
                            print(str(Path(file).parent.joinpath(file)))
                            print()
                        if (not showAllLocation):
                            print(fileSha1[tmpSha1])
                            print(file.name)
                            print()
                
        if Path.is_file(Path(aPath)):
            tmpSha1 = getSha1(aPath)
            if (tmpSha1 not in fileSha1):
                if (showAllLocation):
                    fileSha1[tmpSha1] = Path(aPath).parent.joinpath(aPath)
                if (not showAllLocation):
                    fileSha1[tmpSha1] = aPath.name
            elif (tmpSha1 in fileSha1):
                if (showAllLocation):
                    print(str(fileSha1[tmpSha1]))
                    print(str(Path(aPath).parent.joinpath(aPath)))
                    print()
                if (not showAllLocation):
                    print(fileSha1[tmpSha1])
                    print(aPath)
                    print()
      
    print()
    input('按回车退出')
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass
