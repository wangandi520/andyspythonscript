# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript

from pathlib import Path
import sys
import re
       
def main(inputPath):
    del inputPath[0]
    for aPath in inputPath:
        if Path.is_file(Path(aPath)):
            fileName = Path(aPath).name
            nameParts = re.findall("(\\[[^\\]]*\\])", fileName)
            if len(nameParts) >= 2:
                workName = nameParts[0][1:-1]
                authorName = nameParts[1][1:-1]
                authorPath = Path(aPath).parent.joinpath(Path(authorName))
                if not authorPath.exists():
                    Path.mkdir(authorPath)
                workPath = Path(authorPath).joinpath(Path(workName))
                if not workPath.exists():
                    Path.mkdir(workPath)
                oldFilePath = Path(aPath)
                newFilePath = Path(workPath).joinpath(Path(aPath).name)
                Path(oldFilePath).replace(newFilePath)
        
if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            main(sys.argv)
    except IndexError:
        pass