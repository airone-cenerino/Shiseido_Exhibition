import numpy as np
from collections import deque


def GetStartPoint(array):
    for i in range(500):
        for j in range(500):
            if array[i][j] == 1:
                return [i, j]


def GetNextReferencePoint(array, referencePoint):
    y = [1, -1, 0, 0, 1, 1, -1, -1]
    x = [0, 0, 1, -1, 1, -1, 1, -1]
    q = deque()                 # キュー
    q.append(referencePoint)
    referencePoints = list()    # 支点の座標
    distance = 0                # 支点からの距離
    skimDistance = 5  # 間引く距離
    lastPoint = list()  # 終点を記録するためだけに作った

    while q:
        distance += 1
        while q:    # 距離distance-1の点たちをすべて取り出す
            referencePoints.append(q.pop())

        for referencePoint in referencePoints:
            for i in range(8):
                if array[referencePoint[0] + y[i]][referencePoint[1] + x[i]] == 1:  # 隣り合う点が見つかったら
                    if distance == skimDistance:  # 距離が一定以上なら
                        return [referencePoint[0] + y[i], referencePoint[1] + x[i]], True
                    else:
                        q.append([referencePoint[0] + y[i],
                                  referencePoint[1] + x[i]])
                        array[referencePoint[0] + y[i]
                              ][referencePoint[1] + x[i]] = 0

                        lastPoint = [referencePoint[0] +
                                     y[i], referencePoint[1] + x[i]]
                        # print("(" + str(referencePoint[0] + y[i]) + ","+str(referencePoint[1] + x[i]) + ") " +
                        #       str(array[referencePoint[0] + y[i]][referencePoint[1] + x[i]]) + " 距離:" + str(distance))

    return lastPoint, False


def main():
    array = np.loadtxt("array.csv", delimiter=",")  # 0と1の配列を取得
    referencePoint = GetStartPoint(array)  # 始点を取得
    skimmmedArray = list()  # これが間引いた後の座標が入るリスト
    skimmmedArray.append(referencePoint)
    flg = True

    while flg:  # 順番に探索していく
        referencePoint, flg = GetNextReferencePoint(array, referencePoint)
        # print(referencePoint)
        if referencePoint == None:  # 終点まで来たら終わり
            break

        skimmmedArray.append(referencePoint)

    # 最後に配列をファイル出力して終了
    print(skimmmedArray)
    np.savetxt("skimmedArray.csv", skimmmedArray, delimiter=",")


if __name__ == '__main__':
    main()
