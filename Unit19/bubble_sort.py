# 오름차순으로 버블 소트
aList = [5, 4, 21, 3, 15, 2, 95, 11, 43, 76]

for i in range(len(aList)-1):
    for k in range(i+1, len(aList)):
        if aList[i] > aList[k]:
            aList[i], aList[k] = aList[k], aList[i]


print(aList)
