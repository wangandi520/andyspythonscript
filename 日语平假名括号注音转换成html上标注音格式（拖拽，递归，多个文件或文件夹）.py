# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys

# 可以把形(かたち)转换成<ruby>形<rt>かたち</rt></ruby>，在html中，形字上面注音的形式，也适用于hexo博客

def writefile(fileName, filereadlines):
    with open(fileName, mode='w', encoding='UTF-8') as newfile:
        newfile.writelines(filereadlines)

def readfile(filename):
    with open(filename, mode='r', encoding='UTF-8') as file:
        filereadlines = file.readlines()
    return filereadlines
    
def ifIsChinese(eachChar):
    if '\u4e00' <= eachChar <= '\u9fff':
        return True
    else:
        return False

def myStringSearch(myString, myFind):
    tempIndex = 0
    indexArray = []
    while tempIndex < len(myString):
        tempIndex = myString.find(myFind, tempIndex)
        if tempIndex == -1:
            break
        indexArray.append(tempIndex)
        tempIndex = tempIndex + 1    
    return indexArray
        
def convertToHTML(filename):
    readFileContent = readfile(filename)
    # 统计左右括号数量
    leftCount = 0
    rightCount = 0
    tempFileContent = []
    for eachLine in readFileContent:
        leftCount = leftCount + eachLine.count('（') + eachLine.count('(') 
        rightCount = rightCount + eachLine.count('）') + eachLine.count(')') 
        # 括号转换成统一样式
        tempLine = eachLine.replace('（', '(').replace('）', ')')
        tempFileContent.append(tempLine)
    readFileContent = tempFileContent
    tempFileContent = []
    if leftCount != rightCount:
        print('括号数量不匹配')
    elif leftCount == rightCount:
        for eachLine in readFileContent:
            if eachLine.find('(') == -1:
                tempFileContent.append(eachLine)
            else:
                newLine = '<ruby>'
                for tempIndex in range(0, len(eachLine)):
                    if not ifIsChinese(eachLine[tempIndex]):
                        newLine = newLine + eachLine[tempIndex] + '<rt></rt>'
                    else:
                        if ifIsChinese(eachLine[tempIndex]) and eachLine[tempIndex + 1] != '(':
                            newLine = newLine + eachLine[tempIndex]
                        if ifIsChinese(eachLine[tempIndex]) and eachLine[tempIndex + 1] == '(':
                            newLine = newLine + eachLine[tempIndex] + '<rt>'
                            getTempIndex = eachLine.find(')', tempIndex + 1, len(eachLine))
                            newLine = newLine + eachLine[tempIndex + 2: getTempIndex] + '</rt>'
                            tempIndex = getTempIndex
                newLine = newLine.replace('\n','') +  '</ruby>\n'
                if newLine.endswith('<rt></rt><rt></rt></ruby>\n'):
                    newLine = newLine[0: len(newLine) - 26] + '<rt></rt></ruby>\n'
                tempFileContent.append(newLine)
    ttempFileContent = []
    ttempIndex = 0
    for eachLine in tempFileContent:
        getLeftCount = myStringSearch(eachLine,'(<rt></rt>')
        getRightCount = myStringSearch(eachLine,'<rt></rt>)')
        addLast = False
        if '<ruby>(<rt></rt>' in eachLine and ')<rt></rt></ruby>' in eachLine:
            addLast = True
            getLeftCount = getLeftCount[1:]
            getRightCount = getRightCount[0: -1]
        getCountLength = len(getLeftCount)
        if getCountLength > 0:
            tempLine = eachLine[0: getLeftCount[0]]
            tttempIndex = 0
            while tttempIndex < getCountLength - 1:
                tempLine = tempLine + eachLine[getRightCount[tttempIndex]: getLeftCount[tttempIndex + 1]]
                tttempIndex = tttempIndex + 1
            tempLine = tempLine + eachLine[getRightCount[getCountLength - 1]:]
            tempLine = tempLine.replace(')<rt></rt>', '')
            tempLine = tempLine.replace('</rt> <rt>', '</rt>&nbsp;<rt>')
            if addLast:
                tempLine = tempLine.replace('<rt></rt></ruby>',')<rt></rt></ruby>')
            ttempFileContent.append(tempLine)
        else:
            eachLine = eachLine.replace('</rt> <rt>', '</rt>&nbsp;<rt>')
            ttempFileContent.append(eachLine)
    newFileName = filename.parent.joinpath(Path(filename).stem + '.html')
    if not Path(newFileName).exists():
        writefile(newFileName, ttempFileContent)
        
def main(inputPath):
    fileType = ['.txt', '.md', '.html']
    for aPath in inputPath[1:]:
        if Path.is_dir(Path(aPath)):
            for eachFile in Path(aPath).glob('**/*'):
                if (Path(eachFile).suffix in fileType):
                    convertToHTML(eachFile)
        if Path.is_file(Path(aPath)):
            if (Path(aPath).suffix in fileType):
                convertToHTML(aPath)

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass