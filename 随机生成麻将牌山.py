import random

# 日本麻将发牌配牌模拟
# 136张牌，p筒s索m万123456789，z字东南西北白发中，0红宝牌
# 从北家右手方向顺时针生成
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

for i in range(0, len(rawMahjong)):
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
getNum1 = touzi1[random.randint(0, 5)]
getNum2 = touzi2[random.randint(0, 5)]
getNum = getNum1 + getNum2
getDirection = ''

#判断拿牌起始位置

if (getNum in changfengDong):
    getDirection = '东'
    startIndex = 2 * getNum + 102
elif (getNum in changfengNan):
    getDirection = '南'
    startIndex = 2 * getNum + 68
elif (getNum in changfengXi):
    getDirection = '西'
    startIndex = 2 * getNum + 34
elif (getNum in changfengBei):
    getDirection = '北'
    startIndex = 2 * getNum

# 每家配牌
playerDong = []
playerNan = []
playerXi = []
playerBei = []
# 王牌
wangPai = []
   
# 重置牌谱，第一张配牌的为起始，前面的添加到后面，并分出王牌
newRandomMahjong = []
newnewRandomMahjong = []
for i in range(startIndex, len(randomMahjong)):
    newRandomMahjong.append(randomMahjong[i])
for i in range(0, startIndex):
    newRandomMahjong.append(randomMahjong[i])
newnewRandomMahjong = list(newRandomMahjong)
newStartIndex = 0

index = 0
while index < 3:
    playerDong = playerDong + newnewRandomMahjong[0: 4]
    del newnewRandomMahjong[0: 4]
    playerNan = playerNan + newnewRandomMahjong[0: 4]
    del newnewRandomMahjong[0: 4]
    playerXi = playerXi + newnewRandomMahjong[0: 4]
    del newnewRandomMahjong[0: 4]
    playerBei = playerBei + newnewRandomMahjong[0: 4]
    del newnewRandomMahjong[0: 4]
    index = index + 1

playerDong.append(newnewRandomMahjong[0])
playerDong.append(newnewRandomMahjong[4])
playerNan.append(newnewRandomMahjong[1])
playerXi.append(newnewRandomMahjong[2])
playerBei.append(newnewRandomMahjong[3])
del newnewRandomMahjong[0: 5]
wangPai = wangPai + newnewRandomMahjong[len(newnewRandomMahjong) - 14: len(newnewRandomMahjong)]

print('骰子: ' + str(getNum1) + ' + ' + str(getNum2))
print()
print('配牌方向: ' + getDirection)
print()
print('初始牌山（北家右侧起，数量' + str(len(randomMahjong)) + '）: ')
for i in randomMahjong:
    print(i, end = '')
print('\n')
print('配牌牌山（拿起第一组起，数量' + str(len(newRandomMahjong)) + '）: ')
for i in newRandomMahjong:
    print(i, end = '')
print('\n')
print('东家配牌（数量' + str(len(playerDong)) + '）: ')
for i in playerDong:
    print(i, end = '')
print('\n')
print('南家配牌（数量' + str(len(playerNan)) + '）: ')
for i in playerNan:
    print(i, end = '')
print('\n')
print('西家配牌（数量' + str(len(playerXi)) + '）: ')
for i in playerXi:
    print(i, end = '')
print('\n')
print('北家配牌（数量' + str(len(playerBei)) + '）: ')
for i in playerBei:
    print(i, end = '')
print('\n')
print('剩余牌山（数量' + str(len(newnewRandomMahjong) - 14) + '，不含王牌）: ')
for i in range(0, len(newnewRandomMahjong) - 14):
    print(newnewRandomMahjong[i], end = '')
print('\n')
print('王牌（数量14）: ')
for i in wangPai:
    print(i, end = '')
print('\n')
print('宝牌: ')
print(newnewRandomMahjong[-6], end = '')
input()