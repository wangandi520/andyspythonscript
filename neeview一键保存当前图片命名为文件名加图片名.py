# encoding:utf-8
# https://github.com/wangandi520/andyspythonscript
# by Andy
# v0.1

from pathlib import Path
import sys

def doConvert():
    oldFilePath = sys.argv[1]
    newFilePath = Path(oldFilePath).parent.joinpath(Path(sys.argv[2]))
    if not Path(newFilePath).exists():
        Path(oldFilePath).rename(Path(newFilePath))

def main(inputPath):
    doConvert()

if __name__ == '__main__':
    try:
        if len(sys.argv) > 2:
            main(sys.argv)
    except IndexError:
        pass