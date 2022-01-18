import random

# 日本麻将发牌配牌模拟
# 136张牌，p筒s索m万123456789，z字东南西北白发中，0红宝牌
# 从北家右手方向逆时针生成
rawMahjong = [
'1p', '1p', '1p', '1p', 
'2p', '2p', '2p', '2p', 
'3p', '3p', '3p', '3p', 
'4p', '4p', '4p', '4p', 
'5p', '5p', '5p', '0p', 
'6p', '6p', '6p', '6p', 
'7p', '7p', '7p', '7p', 
'8p', '8p', '8p', '8p', 
'9p', '9p', '9p', '9p', 
'1s', '1s', '1s', '1s', 
'2s', '2s', '2s', '2s', 
'3s', '3s', '3s', '3s', 
'4s', '4s', '4s', '4s', 
'5s', '5s', '5s', '0s', 
'6s', '6s', '6s', '6s', 
'7s', '7s', '7s', '7s', 
'8s', '8s', '8s', '8s', 
'9s', '9s', '9s', '9s', 
'1m', '1m', '1m', '1m', 
'2m', '2m', '2m', '2m', 
'3m', '3m', '3m', '3m', 
'4m', '4m', '4m', '4m', 
'5m', '5m', '5m', '0m', 
'6m', '6m', '6m', '6m', 
'7m', '7m', '7m', '7m', 
'8m', '8m', '8m', '8m', 
'9m', '9m', '9m', '9m', 
'1z', '1z', '1z', '1z', 
'2z', '2z', '2z', '2z', 
'3z', '3z', '3z', '3z', 
'4z', '4z', '4z', '4z', 
'5z', '5z', '5z', '5z', 
'6z', '6z', '6z', '6z', 
'7z', '7z', '7z', '7z', 
]

# 随机生成的牌谱
randomMahjong = []

for i in range(0, len(rawMahjong) - 1):
    randomIndex = random.randint(0, len(rawMahjong) - 1)
    randomMahjong.append(rawMahjong[randomIndex])
    del rawMahjong[randomIndex]

# 场风盘
changfengDong = [5, 9]
changfengNan = [2, 6, 10]
changfengXi = [3, 7, 11]
changfengBei = [4 ,8, 12]

# 骰子
touzi1 = [1, 2, 3, 4, 5, 6]
touzi2 = [1, 2, 3, 4, 5, 6]
getNum = touzi1[random.randint(0, 5)] + touzi2[random.randint(0, 5)]
getDirection = ''

#判断拿牌起始位置

if (getNum in changfengDong):
    getDirection = 'Dong'
elif (getNum in changfengNan):
    getDirection = 'Nan'
elif (getNum in changfengXi):
    getDirection = 'Xi'
elif (getNum in changfengBei):
    getDirection = 'Bei'

# 打印牌谱，北家右侧起，上下上下
# 北牌堆
#for i in range(0, 33):
#    print(randomMahjong[i], end = '')
#print('\n')
# 西牌堆
#for i in range(34, 67):
#    print(randomMahjong[i], end = '')
# 南牌堆
#print('\n')
#for i in range(68, 101):
#    print(randomMahjong[i], end = '')
# 东牌堆
#print('\n')
#for i in range(102, 135):
#    print(randomMahjong[i], end = '')

# 每家配牌
playerDong = []
playerNan = []
playerXi = []
playerBei = []
# 王牌
wangPai = []

if (getDirection == 'Dong'):
    startIndex = 2 * getNum + 102
elif (getDirection == 'Nan'):
    startIndex = 2 * getNum + 68
elif (getDirection == 'Xi'):
    startIndex = 2 * getNum + 34
elif (getDirection == 'Bei'):
    startIndex = 2 * getNum
    
# 重置牌谱，第一张配牌的为起始，前面的添加到后面，并分出王牌
newRandomMahjong = []
for i in range(startIndex, len(randomMahjong)):
    newRandomMahjong.append(randomMahjong[i])
for i in range(0, startIndex):
    newRandomMahjong.append(randomMahjong[i])

newStartIndex = 0
playerDong = playerDong + newRandomMahjong[newStartIndex + 0: newStartIndex + 4]
playerNan = playerNan + newRandomMahjong[newStartIndex + 4: newStartIndex + 8]
playerXi = playerXi + newRandomMahjong[newStartIndex + 8: newStartIndex + 12]
playerBei = playerBei + newRandomMahjong[newStartIndex + 12: newStartIndex + 16]
playerDong = playerDong + newRandomMahjong[newStartIndex + 16: newStartIndex + 20]
playerNan = playerNan + newRandomMahjong[newStartIndex + 20: newStartIndex + 24]
playerXi = playerXi + newRandomMahjong[newStartIndex + 24: newStartIndex + 28]
playerBei = playerBei + newRandomMahjong[newStartIndex + 28: newStartIndex + 32]
playerDong = playerDong + newRandomMahjong[newStartIndex + 32: newStartIndex + 36]
playerNan = playerNan + newRandomMahjong[newStartIndex + 36: newStartIndex + 40]
playerXi = playerXi + newRandomMahjong[newStartIndex + 40: newStartIndex + 44]
playerBei = playerBei + newRandomMahjong[newStartIndex + 44: newStartIndex + 48]
playerDong = playerDong + newRandomMahjong[newStartIndex + 48: newStartIndex + 49]
playerDong = playerDong + newRandomMahjong[newStartIndex + 52: newStartIndex + 53]
playerNan = playerNan + newRandomMahjong[newStartIndex + 49: newStartIndex + 50]
playerXi = playerXi + newRandomMahjong[newStartIndex + 50: newStartIndex + 51]
playerBei = playerBei + newRandomMahjong[newStartIndex + 51: newStartIndex + 52]

lastIndex = 53

wangPai = wangPai + newRandomMahjong[len(newRandomMahjong) - 14: len(newRandomMahjong)]

print('骰子: ' + str(getNum))
print()
if (getDirection == 'Dong'):
    print('配牌方向: 东')
if (getDirection == 'Nan'):
    print('配牌方向: 南')
if (getDirection == 'Xi'):
    print('配牌方向: 西')
if (getDirection == 'Bei'):
    print('配牌方向: 北')
print()
print('牌山: ')
for i in newRandomMahjong:
    print(i, end = '')
print('\n')
print('东家配牌: ')
for i in playerDong:
    print(i, end = '')
print('\n')
print('南家配牌: ')
for i in playerNan:
    print(i, end = '')
print('\n')
print('西家配牌: ')
for i in playerXi:
    print(i, end = '')
print('\n')
print('北家配牌: ')
for i in playerBei:
    print(i, end = '')
print('\n')
print('剩余牌山（不含王牌）: ')
for i in range(53, len(newRandomMahjong) - 14):
    print(newRandomMahjong[i], end = '')
print('\n')
print('王牌: ')
for i in wangPai:
    print(i, end = '')
print('\n')
print('宝牌: ')
print(newRandomMahjong[-6], end = '')