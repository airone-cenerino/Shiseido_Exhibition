import numpy as np
from collections import deque

array = np.loadtxt("array.csv", delimiter=",")

for i in range(500):
    for j in range(500):
        if array[i][j] == 1:
            referencePoint = [i, j]
            array[i][j] = 0
            break
    else:
        continue
    break


y = [1, -1, 0, 0, 1, 1, -1, -1]
x = [0, 0, 1, -1, 1, -1, 1, -1]
q = deque()                 # キュー
q.append(referencePoint)
referencePoints = list()    # 支点の座標
distance = 0                # 支点からの距離
skimDistance = 10           # 間引く距離
skimmmedArray = list()  # これが間引いた後の座標が入るリスト

skimmmedArray.append(referencePoint)

while q:
    distance += 1
    while q:    # 距離distance-1の点たちをすべて取り出す
        referencePoints.append(q.pop())

    for referencePoint in referencePoints:
        for i in range(8):
            if array[referencePoint[0] + y[i]][referencePoint[1] + x[i]] == 1:  # 隣り合う点が見つかったら
                if distance == skimDistance:  # 距離が一定以上なら
                    skimmmedArray.append(
                        [referencePoint[0] + y[i], referencePoint[1] + x[i]])  # その点を挿入

                    # ここですべてを初期化して、支店を変更してブレークしたい

                q.append([referencePoint[0] + y[i], referencePoint[1] + x[i]])
                array[referencePoint[0] + y[i]][referencePoint[1] + x[i]] = 0

                print("(" + str(referencePoint[0] + y[i]) + ","+str(referencePoint[1] + x[i]) + ") " +
                      str(array[referencePoint[0] + y[i]][referencePoint[1] + x[i]]) + " 距離:" + str(distance))


# if array[referencePoint[0] + 1][referencePoint[1]] == 1:  # 下
#     print("下")

# if array[referencePoint[0] - 1][referencePoint[1]] == 1:  # 下
#     print("下")

# if array[referencePoint[0]][referencePoint[1] + 1] == 1:  # 右
#     print("右")

# if array[referencePoint[0]][referencePoint[1] - 1] == 1:  # 左
#     print("左")

# if array[referencePoint[0] + 1][referencePoint[1] + 1] == 1:  # 右上
#     print("右上")

# if array[referencePoint[0] + 1][referencePoint[1] - 1] == 1:  # 左上
#     print("左上")

# if array[referencePoint[0] - 1][referencePoint[1] + 1] == 1:  # 右下
#     print("右下")

# if array[referencePoint[0] - 1][referencePoint[1] - 1] == 1:  # 左下
#     print("左下")
