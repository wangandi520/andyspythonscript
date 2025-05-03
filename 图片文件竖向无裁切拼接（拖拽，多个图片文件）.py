# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.2

from pathlib import Path
import sys
import re
from PIL import Image

from typing import List, Union

# 把可以更改的设置都放在这里
CONFIG = {
    # 输出图片格式：'PNG'或'JPEG'
    'output_format': 'JPEG',
    # 图片质量(1-100)，仅对JPEG有效
    'quality': 60,
    # 是否调整图片大小
    'resize_images': False,
    # 调整后的最大宽度(像素)
    'max_width': 1200
}

def doConvert(imagePaths: list[Path]) -> None:
    try:
        if not imagePaths:
            print('没有找到图片文件')
            return
        print(f'本脚本仅做简单拼接，无法保证图片质量，请保留原图片备份...')
        # 打开所有图片
        images = []
        for imgPath in imagePaths:
            try:
                img = Image.open(imgPath)
                # 确保图片已完全加载
                img = img.convert('RGB')  # 转换为RGB模式，避免透明通道问题
                
                # 如果启用了调整大小选项且图片宽度超过最大宽度
                if CONFIG.get('resize_images', False) and img.width > CONFIG.get('max_width', 1200):
                    # 计算缩放比例
                    ratio = CONFIG.get('max_width', 1200) / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((CONFIG.get('max_width', 1200), new_height), Image.LANCZOS)
                images.append(img)
            except Exception as e:
                print(f'无法打开图片 {imgPath}: {str(e)}')
        if not images:
            print('没有可用的图片')
            return
        print(f'成功加载了 {len(images)} 张图片')
        # 获取所有图片的宽度
        widths = [img.width for img in images]
        # 使用最宽的图片宽度
        width = max(widths)   
        # 计算总高度
        total_height = sum(img.height for img in images)
        # 创建新图片，使用白色背景 (255, 255, 255)
        merged_image = Image.new('RGB', (width, total_height), color=(255, 255, 255))
        # 拼接图片
        y_offset = 0
        for i, img in enumerate(images):
            # 粘贴到新图片上，不进行任何裁切或缩放
            merged_image.paste(img, (0, y_offset))
            y_offset += img.height
        
        # 保存拼接后的图片
        format_ext = '.jpg' if CONFIG.get('output_format', 'JPEG').upper() == 'JPEG' else '.png'
        output_path = Path(imagePaths[0].parent, f"拼接图片_{imagePaths[0].stem}{format_ext}")
        
        # 根据设置的格式保存
        if CONFIG.get('output_format', 'JPEG').upper() == 'JPEG':
            merged_image.save(output_path, format='JPEG', quality=CONFIG.get('quality', 85))
        else:
            merged_image.save(output_path, format='PNG', optimize=True)
        print(f'总共拼接了 {len(images)} 张图片')
        print(f'拼接完成，已保存到: {output_path}')
    except Exception as e:
        print(f'处理图片时出错：{str(e)}')
    input('按回车键继续...')

def main(inputPath: list[str]) -> None:
    fileType = {'.jpg', '.jpeg', '.png', '.bmp', '.gif'}  # 使用集合而不是列表，查找更快
    try:
        allFilePaths = []
        for eachPath in inputPath[1:]:
            eachPath = Path(eachPath)
            if eachPath.is_file() and eachPath.suffix.lower() in fileType:
                allFilePaths.append(eachPath)
        # 按文件名排序
        allFilePaths.sort(key=lambda x: x.name)
        doConvert(allFilePaths)
    except Exception as e:
        print(f'程序执行出错：{str(e)}')

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
        else:
            print('请拖拽图片文件或包含图片的文件夹到本脚本，或者命令行运行时添加文件路径')
    except IndexError:
        pass