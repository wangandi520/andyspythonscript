# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# pip install pillow

from PIL import Image
from pathlib import Path
import sys
  
def main(inputPath):
    # 图片高度
    imgHeight = 4000
    # 设置文件类型
    #fileType = ['.png']
    fileType = ['.png','.jpg']
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix in fileType:
                    img = Image.open(file)
                    imgWidth = int(img.size[0] / (img.size[1] / imgHeight ))
                    img = img.resize((imgWidth, imgHeight),Image.ANTIALIAS) 
                    img.save(file.parent.joinpath(file.stem + '_' + str(imgHeight) + file.suffix)) 
                
        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix in fileType: 
                img = Image.open(Path(aPath))
                imgWidth = int(img.size[0] / (img.size[1] / imgHeight ))
                img = img.resize((imgWidth, imgHeight),Image.ANTIALIAS) 
                img.save(Path(aPath).parent.joinpath(Path(aPath).stem + '_' + str(imgHeight) + Path(aPath).suffix)) 

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass