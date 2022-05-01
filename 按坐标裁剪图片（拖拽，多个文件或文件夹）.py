# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from PIL import Image
from pathlib import Path
import sys
  
def main(inputPath):
    # 设置文件类型
    #fileType = ['.png']
    fileType = ['.png','.jpg']
    # 新图片的尺寸(左下角横坐标, 左下角纵坐标, 右上角横坐标, 右上角纵坐标)
    newImgSize =  (0, 0, 200 / 2, 100)
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix in fileType:
                    img = Image.open(file)
                    newImg = img.crop(newImgSize) 
                    newImg.save(file.parent.joinpath(file.stem + '_new' + file.suffix)) 
                
        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix in fileType: 
                img = Image.open(Path(aPath))
                newImg = img.crop(newImgSize) 
                newImg.save(Path(aPath).parent.joinpath(Path(aPath).stem + '_new' + Path(aPath).suffix)) 

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass