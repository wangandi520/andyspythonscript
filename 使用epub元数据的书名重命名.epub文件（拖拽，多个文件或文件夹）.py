# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# old script: https://github.com/otsuka-kohei/EpubRename2Title/blob/master/epubRename2Title.py
# pip install lxml

import sys
import zipfile
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

def validFileName(fileName):
    # 把不能作为文件的字符替换成空格
    for each in fileName:
        if each in '\/:*?"<>|,':
            fileName = fileName.replace(each, ' ')
    return fileName
      
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        # 文件格式
        fileType = ['.epub']
        
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if Path.is_file(file) and (file.suffix in fileType):
                    book = getEpubInfo(file)
                    title = validFileName(book['title']) + file.suffix
                    Path(file).rename(Path(file).parent.joinpath(title))
                    print(file.name + ' -> ' + title)

        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix in fileType:
                book = getEpubInfo(aPath)
                title = validFileName(book['title']) + Path(aPath).suffix
                Path(aPath).rename(Path(aPath).parent.joinpath(title))
                print(Path(aPath).name + ' -> ' + title)
            
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass