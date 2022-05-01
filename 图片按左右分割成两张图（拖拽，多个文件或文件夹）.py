# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from PIL import Image
from pathlib import Path
import sys
  
def main(inputPath):
    # 设置文件类型
    #fileType = ['.png']
    fileType = ['.png','.jpg']
    # 设置新图片的文件名结尾
    # 左页
    leftImgName = '_left'
    # 右页
    rightImgName = '_right'
    # 新图片的尺寸(左下角横坐标, 左下角纵坐标, 右上角横坐标, 右上角纵坐标)
    # imgWidth, imgHeight = img.size
    # 左页
    # newLeftImgSize =  (0, 0, imgWidth / 2, imgHeight)
    # 右页
    # newRightImgSize =  (imgWidth / 2, 0, imgWidth, imgHeight)
    
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            for file in Path(aPath).glob('**/*'):
                if file.suffix in fileType:
                    img = Image.open(file)
                    imgWidth, imgHeight = img.size
                    # 左页
                    newLeftImgSize =  (0, 0, imgWidth / 2, imgHeight)
                    # 右页
                    newRightImgSize =  (imgWidth / 2, 0, imgWidth, imgHeight)
                    newLeftImg = img.crop(newLeftImgSize) 
                    newRightImg = img.crop(newRightImgSize) 
                    newLeftImg.save(file.parent.joinpath(file.stem + leftImgName + file.suffix)) 
                    newRightImg.save(file.parent.joinpath(file.stem + rightImgName + file.suffix)) 
                
        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix in fileType: 
                img = Image.open(Path(aPath))
                imgWidth, imgHeight = img.size
                # 左页
                newLeftImgSize =  (0, 0, imgWidth / 2, imgHeight)
                # 右页
                newRightImgSize =  (imgWidth / 2, 0, imgWidth, imgHeight)
                newLeftImg = img.crop(newLeftImgSize) 
                newRightImg = img.crop(newRightImgSize) 
                newLeftImg.save(Path(aPath).parent.joinpath(Path(aPath).stem + leftImgName + Path(aPath).suffix)) 
                newRightImg.save(Path(aPath).parent.joinpath(Path(aPath).stem + rightImgName + Path(aPath).suffix)) 

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass