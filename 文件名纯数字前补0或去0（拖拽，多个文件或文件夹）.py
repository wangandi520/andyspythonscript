# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys

def renameBySomeZero(filePath):
    # type(filePath): Path
    # 只对纯数字文件名有效
    # fileNameFill，处理后的文件名，文件名长度大于这个数字去0，填3时，0001->001，00001->001。文件名长度小于这个数字补0，01->001
    fileNameFill = 3
    if filePath.stem.isdigit():
        fileNameLength = len(str(filePath.stem))
        if (fileNameLength < fileNameFill):
            newFilePath = filePath.parent.joinpath(filePath.stem.zfill(fileNameFill) + filePath.suffix)
            if not newFilePath.exists():
                filePath.rename(newFilePath)
        
        if (fileNameLength > fileNameFill):
            ifRename = True
            for count in range(0, fileNameLength - fileNameFill):
                if str(filePath.stem)[count] != '0':
                    ifRename = False
            if ifRename and fileNameLength > fileNameFill:
                newFilePath = filePath.parent.joinpath(filePath.stem[fileNameLength - fileNameFill:] + filePath.suffix)
                if not newFilePath.exists():
                    filePath.rename(newFilePath)   
            
def main(inputPath):
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            # 修改文件夹名，使用33行，行首加#代表注释，不生效的意思
            #renameBySomeZero(Path(aPath))
            # 修改文件夹内的文件，使用35，36行
            for file in Path(aPath).glob('**/*'):
                renameBySomeZero(file)
        if Path.is_file(Path(aPath)):
            renameBySomeZero(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass