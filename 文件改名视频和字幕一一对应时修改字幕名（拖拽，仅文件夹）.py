# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.2

from pathlib import Path
import sys
import re

from typing import List, Union

# 把可以更改的设置都放在这里
CONFIG = {
    # True = ，False = 
    'Option01': False,
    # True = ，False = 
    'option02': {}
}

def validFileName(oldFileName):
    # '/ \ : * ? " < > |'
    # 替换为下划线
    validChars = r"[\/\\\:\*\?\"\<\>\|]"  
    newFileName = re.sub(validChars, "_", oldFileName)
    return newFileName
    
def writefile(fileName: Path, allFileContent: list[str]) -> None:
    try:
        with open(fileName, mode='w', encoding='UTF-8') as newfile:
            newfile.writelines(allFileContent)
    except Exception as e:
        print(f'写入文件失败：{fileName}，错误：{str(e)}')

def readfile(fileName: Path) -> list[str]:
    try:
        with open(fileName, mode='r', encoding='UTF-8') as newfile:
            return newfile.readlines()
    except Exception as e:
        print(f'读取文件失败：{fileName}，错误：{str(e)}')
        return []

def doConvert(folderName: Path) -> None:
    # 设置视频和字幕文件类型
    videoTypes = {'.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.rmvb'}
    subtitleTypes = {'.srt', '.ass', '.ssa', '.sub', '.idx', '.vtt'}
    
    try:
        print(f'处理文件夹：{folderName}')
        
        # 收集所有视频和字幕文件
        videoFiles = []
        subtitleFiles = []
        
        for eachFile in folderName.glob('*'):
            if eachFile.is_file():
                if eachFile.suffix.lower() in videoTypes:
                    videoFiles.append(eachFile)
                elif eachFile.suffix.lower() in subtitleTypes:
                    subtitleFiles.append(eachFile)
        
        if not videoFiles or not subtitleFiles:
            print('未找到视频文件或字幕文件')
            return
            
        print(f'找到 {len(videoFiles)} 个视频文件和 {len(subtitleFiles)} 个字幕文件')
        
        # 检查视频和字幕文件数量是否相同
        if len(videoFiles) != len(subtitleFiles):
            print('错误：视频文件和字幕文件数量不相同，无法进行匹配')
            return
            
        # 按文件名排序
        videoFiles.sort(key=lambda x: x.name)
        subtitleFiles.sort(key=lambda x: x.name)
        
        # 尝试通过文件名中的数字匹配
        video_numbers = {}
        for video in videoFiles:
            # 提取文件名中的数字
            numbers = re.findall(r'\d+', video.stem)
            if numbers:
                # 使用第一个数字作为集数标识
                episode_num = numbers[0]
                video_numbers[episode_num] = video
        
        # 匹配字幕文件
        matches = []
        unmatched_subtitles = []
        
        for subtitle in subtitleFiles:
            numbers = re.findall(r'\d+', subtitle.stem)
            if numbers and numbers[0] in video_numbers:
                matches.append((video_numbers[numbers[0]], subtitle))
            else:
                unmatched_subtitles.append(subtitle)
        
        # 检查是否所有视频和字幕都匹配成功
        if len(matches) != len(videoFiles):
            print('错误：无法为所有视频找到对应的字幕文件')
            print(f'成功匹配：{len(matches)}，视频总数：{len(videoFiles)}')
            
            # 显示未匹配的字幕
            if unmatched_subtitles:
                print('\n未匹配的字幕文件:')
                for sub in unmatched_subtitles:
                    print(f'- {sub.name}')
            
            # 如果匹配数量不足，尝试按顺序匹配
            user_input = input('\n是否尝试按文件名排序顺序匹配? (y/n): ')
            if user_input.lower() == 'y':
                matches = []
                for i in range(len(videoFiles)):
                    matches.append((videoFiles[i], subtitleFiles[i]))
            else:
                return
        
        # 输出匹配结果
        print('\n匹配结果:')
        for i, (video, subtitle) in enumerate(matches):
            print(f'{i+1}. 视频: {video.name} -> 字幕: {subtitle.name}')
        
        # 询问用户是否确认重命名
        user_input = input('\n确认以上匹配并重命名字幕文件? (y/n): ')
        
        if user_input.lower() == 'y':
            for video, subtitle in matches:
                # 创建新的字幕文件名，保持原扩展名
                new_subtitle_name = video.stem + subtitle.suffix
                new_subtitle_path = subtitle.parent / new_subtitle_name
                
                # 重命名字幕文件
                subtitle.rename(new_subtitle_path)
                print(f'已重命名: {subtitle.name} -> {new_subtitle_name}')
            
            print('所有字幕文件重命名完成')
        else:
            print('操作已取消')
            
    except Exception as e:
        print(f'处理文件夹时出错：{folderName}，错误：{str(e)}')
    input('按回车键继续...')

def main(inputPath: list[str]) -> None:
    try:
        for eachPath in inputPath[1:]:
            eachPath = Path(eachPath)
            if eachPath.is_dir():
                doConvert(eachPath)
    except Exception as e:
        print(f'程序执行出错：{str(e)}')

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
        else:
            print('请拖拽文件到本脚本，或者命令行运行时添加文件路径')
    except IndexError:
        pass