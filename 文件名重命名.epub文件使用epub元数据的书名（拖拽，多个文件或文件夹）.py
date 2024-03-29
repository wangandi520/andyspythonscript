# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# old script: https://github.com/otsuka-kohei/EpubRename2Title/blob/master/epubRename2Title.py
# pip install lxml

import sys
import zipfile
import re
from lxml import etree
from pathlib import Path

def getEpubInfo(filePath):
    # xmlのnamespace ディクショナリのキーは任意に定義したもの
    ns = {
        # /META-INF/container.xml の中のnamespace
        'n': 'urn:oasis:names:tc:opendocument:xmlns:container',
        # OPFファイルのいちばん外側のオブジェクト(package要素)のnamespace
        'pkg': 'http://www.idpf.org/2007/opf',
        # OPFファイルに記載されている書籍名や作者名の要素のnamespace
        'dc': 'http://purl.org/dc/elements/1.1/'
    }
    # epubファイルはzipファイル
    zip = zipfile.ZipFile(filePath)
    # /META-INF/container.xml からメタデータが記録されているファイルのパスを取得する
    txt = zip.read('META-INF/container.xml')
    tree = etree.fromstring(txt)
    opf_path = tree.xpath('n:rootfiles/n:rootfile/@full-path', namespaces=ns)[0]
    # OPFファイルのpackage要素の中のmetadata要素を取得する
    opf = zip.read(opf_path)
    tree = etree.fromstring(opf)
    metadata = tree.xpath('/pkg:package/pkg:metadata', namespaces=ns)[0]
    # metadata要素の情報をディクショナリに整形する
    res = {}
    for s in ['title', 'language', 'creator', 'date', 'identifier']:
        info = metadata.xpath('dc:{0}'.format(s), namespaces=ns)
        if(len(info) > 0):
            res[s] = metadata.xpath(
                'dc:{0}/text()'.format(s), namespaces=ns)[0]
    return res

def validFileName(oldFileName):
    # '/ \ : * ? " < > |'
    # 替换为下划线
    validChars = r"[\/\\\:\*\?\"\<\>\|]"  
    newFileName = re.sub(validChars, "_", oldFileName)
    return newFileName

def doChangeFileName(filePath):
    # type(filePath): Path
    # 文件格式
    fileType = ['.epub']
    if Path.is_file(filePath) and (filePath.suffix.lower() in fileType):
        book = getEpubInfo(filePath)
        # 文件名格式：书名 作者.扩展名
        if book.get('creator') != None:
            title = validFileName(book['title']) + ' ' + validFileName(book['creator']) + filePath.suffix
            filePath.rename(filePath.parent.joinpath(title))
            print(filePath.name + ' -> ' + title)
        elif book.get('title') != None:
            title = validFileName(book['title']) + filePath.suffix
            filePath.rename(filePath.parent.joinpath(title))
            print(filePath.name + ' -> ' + title)
        else:
            print(filePath.name + ' 无法获取信息，重命名失败')
        
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        # 文件格式
        fileType = ['.epub']
        
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                doChangeFileName(file)

        if Path.is_file(Path(aPath)):
            doChangeFileName(Path(aPath))
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass