# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from PIL import Image
from pathlib import Path
import sys

def doCrop(filePath):
    # 设置图片质量，越大体积越大，1到95，质量80体积差不多容差30，质量95两倍体积容差10
    setQuality = 80
    # 设置新图片的文件名结尾
    # 左页
    leftImgName = '_left'
    # 右页
    rightImgName = '_right'
    img = Image.open(filePath)
    imgWidth, imgHeight = img.size
    # 左页
    newLeftImgSize =  (0, 0, imgWidth / 2, imgHeight)
    # 右页
    newRightImgSize =  (imgWidth / 2, 0, imgWidth, imgHeight)
    newLeftImg = img.crop(newLeftImgSize) 
    newRightImg = img.crop(newRightImgSize) 
    newLeftImg.save(filePath.parent.joinpath(filePath.stem + leftImgName + filePath.suffix), quality = setQuality, subsampling=0) 
    newRightImg.save(filePath.parent.joinpath(filePath.stem + rightImgName + filePath.suffix), quality = setQuality, subsampling=0) 
    
def main(inputPath):
    # 设置文件类型
    #fileType = ['.png']
    fileType = ['.png', '.jpg', '.jpeg']
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
                if file.suffix.lower() in fileType:
                    doCrop(file)
                
        if Path.is_file(Path(aPath)):
            if Path(aPath).suffix.lower() in fileType: 
                    doCrop(Path(aPath))

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass