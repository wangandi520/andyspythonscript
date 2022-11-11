import os
import fitz
import sys
from pathlib import Path

# pip install fitz frontend pymupdf

#使用fitz 库直接提取pdf的图像
#参数：    pdf      源pdf文件完整路径
#参数：    picPath  提取图像的路径
def muExtractImages(filePath):
    fileType = ['.pdf']
    if filePath.suffix.lower() in fileType:
        pdfname = filePath.name  #获取文件名
        pdfname1 = filePath.stem  #获取不带扩展名的文件名
        print(filePath)
        #print(pdfsplit)
        #print(pdfname)
        #print(pdfname1)
        # 打开pdf，打印PDF的相关信息
        doc = fitz.open(filePath)
        # 图片计数
        imgcount = 0
        lenXREF = doc.xref_length()    #获取pdf文件对象总数

        # 打印PDF的信息
        print("文件名:{}, 页数: {}, 对象: {}".format(filePath, len(doc), lenXREF - 1))
        newFolderPath = filePath.parent.joinpath(filePath.stem)
        if not newFolderPath.exists():
            Path.mkdir(newFolderPath)
        #遍历doc，获取每一页
        for page in doc: 
            try:
                imgcount +=1
                tupleImage = page.get_images()
                lstImage = list(tupleImage)           
                xref0 = lstImage[0]    #取第一个元组
                xref1 = list(xref0)     #元组转化为列表            
                xref = xref1[0]   #最终取得xref  ok
                print("imgID:    %s" % imgcount)    
                print("xref:  %s" % xref)
                img = doc.extract_image(xref)   #获取文件扩展名，图片内容 等信息
                imageFilename = ("%s-%s." % (imgcount, xref) + img["ext"])
                imageFilename = pdfname1 + "_" + imageFilename  #合成最终 的图像的文件名
                imageFilename = newFolderPath.joinpath(imageFilename)   #合成最终图像完整路径名
                
                print(imageFilename)
                imgout = open(imageFilename, 'wb')   #byte方式新建图片
                imgout.write(img["image"])   #当前提取的图片写入磁盘
                imgout.close
            except:
                continue
    
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                muExtractImages(file)
                
        if Path.is_file(Path(aPath)):
            muExtractImages(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass