# encoding:utf-8
# pip3 install pymupdf
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import fitz
import sys 
    
def main(inputPath):
    # 是否显示文件大小，True，False
    showOrNoFileSize = False
    
    del inputPath[0]
    for file in inputPath:
        if Path.is_file(Path(file)):
            pdfFile = fitz.open(file)
            for getPage in range(len(pdfFile)):
                for getImage in pdfFile.get_page_images(getPage):
                    xref = getImage[0]
                    #pix = fitz.Pixmap(pdfFile, xref)
                    pix = pdfFile[getPage].getPixmap()
                    newPath = Path(file).parent.joinpath(Path(file).stem)
                    if not newPath.exists():
                        Path.mkdir(newPath)
                    pix.save(newPath.joinpath(str(getPage).zfill(3) + ".png"))
                    print(str(getPage).zfill(3) + ".png")
            
        if Path.is_dir(Path(file)):
            print('暂不支持文件夹批量转换')
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass