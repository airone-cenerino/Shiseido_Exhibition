import numpy as np
from collections import deque
from matplotlib import pyplot

# ------------------------------------------------
imageXLen = 1000     # 画像の横サイズ
imageYLen = 1000     # 画像の縦サイズ
skimDistance = 5    # 間引く距離
始点 = [753, 418]    # 幅優先探索開始座標  1000(817, 970)  beautiful(753, 418)
# ------------------------------------------------


def GetSkimmedArray(array):
    y = [1, -1, 0, 0, 1, 1, -1, -1]
    x = [0, 0, 1, -1, 1, -1, 1, -1]
    q = deque()                 # キュー
    q.append(始点)
    skimmedArray = list()       # これが間引いた後の座標が入るリスト
    skimmedArray.append(始点)
    distance = 0                # 支点からの距離
    lastPoint = list()          # 終点を記録するためだけに作った

    while q:
        distance += 1
        points = list()
        一時リスト = []

        while q:    # 距離distance-1の点たちをすべて取り出す
            points.append(q.pop())

        for referencePoint in points:
            for i in range(8):
                if array[referencePoint[0] + y[i]][referencePoint[1] + x[i]] == 1:  # 隣り合う点が見つかったら
                    if distance%skimDistance == 0:  # 距離が間引き距離以外なら
                        # ここで一時リストに座標をぶち込む
                        一時リスト.append([referencePoint[0] + y[i], referencePoint[1] + x[i]])
                    
                    q.append([referencePoint[0] + y[i],
                                referencePoint[1] + x[i]])
                    array[referencePoint[0] + y[i]
                            ][referencePoint[1] + x[i]] = 0

                    lastPoint = [referencePoint[0] +
                                    y[i], referencePoint[1] + x[i]]
        
        # ここで一時リストの重心点をskimmedArrayにアペンドする
        if 一時リスト != []:
            xSum = 0
            ySum = 0
            for 点 in 一時リスト:
                ySum += 点[0]
                xSum += 点[1]

            skimmedArray.append([ySum/len(一時リスト), xSum/len(一時リスト)])
    
    skimmedArray.append(lastPoint)

    return skimmedArray


def main():
    dataArray = np.loadtxt("array.csv", delimiter=",")  # 0と1の配列を取得
    resultArray = GetSkimmedArray(dataArray)
    print(resultArray)
    np.savetxt("skimmedArray.csv", resultArray, delimiter=",")
    
    # 表を描画
    xList = list()
    yList = list()
    for data in resultArray:
        yList.append(data[0])
        xList.append(data[1])

    pyplot.plot(xList, yList)
    pyplot.show()


if __name__ == '__main__':
    main()