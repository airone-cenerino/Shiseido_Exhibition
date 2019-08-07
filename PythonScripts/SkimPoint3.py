import numpy as np
from collections import deque
from matplotlib import pyplot

# ------------------------------------------------
imageXLen = 2000    # 画像の横サイズ
imageYLen = 2000    # 画像の縦サイズ
skimDistance = 3    # 間引く距離
imageNum = 28       # 画像の枚数
folderName = "SampleImage2k\\"    # 画像フォルダ名

始点リスト = [[1042, 922], [1036, 892], [1020, 916], [1072, 691], [1035, 795], [930, 979], [870, 373],
         [1271, 479], [1365, 454], [1320, 1012], [
             945, 378], [971, 321], [989, 325], [1074, 382],
         [1061, 364], [1042, 356], [1030, 357], [1007, 440],
         [659, 664], [540, 224], [778, 426],
         [681, 994], [670, 755], [512, 731], [476, 570], [536, 1327], [802, 1536], [995, 1064]]  # 幅優先探索開始地点のリスト


反転リスト = [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]  # 1なら反対から線を描く
# ------------------------------------------------


path = "D:\Programming\okanonproject\ArrayCSV\\"


def GetSkimmedArray(array, 始点):
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
                    if distance % skimDistance == 0:  # 距離が間引き距離以外なら
                        # ここで一時リストに座標をぶち込む
                        一時リスト.append([referencePoint[0] + y[i],
                                      referencePoint[1] + x[i]])

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


def ShowGraph(array):
    print(array)
    print()

    # 表を描画
    xList = list()
    yList = list()
    for data in array:
        yList.append(data[0])
        xList.append(data[1])

    pyplot.plot(xList, yList)
    pyplot.show()


def main():
    for num in range(imageNum):
        print(num)
        reverseFlg = 反転リスト[num]

        dataArray = np.loadtxt(path + folderName + "array" + str(num+1) +
                               ".csv", delimiter=",")  # 0と1の配列を取得
        resultArray = GetSkimmedArray(
            dataArray, 始点リスト[num])            # 間引いた後の座標リストを取得

        if reverseFlg == 1:
            reversedArray = list()
            for 座標 in resultArray:
                reversedArray.insert(0, 座標)

            np.savetxt("skimmedArray" + str(num + 1) +
                       ".csv", reversedArray, delimiter=",")
            # ShowGraph(reversedArray)
        else:
            np.savetxt("skimmedArray" + str(num + 1) +
                       ".csv", resultArray, delimiter=",")
            # ShowGraph(resultArray)


if __name__ == '__main__':
    main()
