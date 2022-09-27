# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import re
       
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_dir(Path(aPath)):
            folderName = Path(aPath).name
            nameParts = re.findall("(\\[[^\\]]*\\])", folderName)
            if len(nameParts) >= 2:
                workName = nameParts[0][1:-1]
                authorName = nameParts[1][1:-1]
                authorPath = Path(aPath).parent.joinpath(Path(authorName))
                if not authorPath.exists():
                    Path.mkdir(authorPath)
                workPath = Path(authorPath).joinpath(Path(workName))
                if not workPath.exists():
                    Path.mkdir(workPath)
                for file in Path(aPath).glob('*'):
                    oldFilePath = Path(aPath).joinpath(Path(file.name))
                    newFilePath = Path(workPath).joinpath(Path(file.name))
                    Path(oldFilePath).replace(newFilePath)
                Path.rmdir(Path(aPath))
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass