import numpy as np
from collections import deque
from matplotlib import pyplot

# ------------------------------------------------
imageXLen = 2000    # 画像の横サイズ
imageYLen = 2000    # 画像の縦サイズ
skimDistance = 10    # 間引く距離
imageNum = 14       # 画像の枚数
folderName = "Drawing3"    # 画像フォルダ名

始点リスト = [[729, 926], [667, 903], [733, 850], [665, 901], [664, 927], [553, 1135], [857, 1217], [975, 1039], [985, 965], [983, 990], [1146, 927], [1165, 880], [1173, 872], [1514, 945]]
# Drawing 1[[386, 723], [392, 603], [337, 669], [338, 686], [259, 521], [376, 844], [588, 664], [564, 656], [562, 683], [700, 743], [391, 1397], [386, 1277], [337, 1331], [338, 1313], [260, 1478], [376, 1155], [588, 1335], [700, 1257], [565, 1316], [564, 1344], [1586, 604], [1591, 603], [1487, 714], [1436, 552], [1724, 521], [1387, 713], [1385, 676], [1247, 531], [1586, 1394], [1591, 1397], [1487, 1285], [1436, 1449], [1707, 1209], [1386, 1324], [1247, 1469], [1387, 1286], [985, 1000], [963, 1019]]

# Drawing 2[[785, 920], [802, 924], [803, 799], [809, 804], [814, 814], [816, 825], [819, 835], [821, 845], [823, 860], [821, 873], [818, 885], [813,
#897], [808, 908], [782, 840], [799, 863], [741, 1053], [778, 1189], [793, 1187], [792, 1183], [797, 1176], [803, 1165], [808, 1153], [813,
#1142], [816, 1125], [815, 1106], [814, 1095], [812, 1083], [810, 1071], [772, 1103], [778, 1124], [935, 941], [935, 1039], [961, 956], [962, 1028], [1080, 880], [1058, 948], [1102, 928], [759, 729], [759, 717], [1456, 1533], [1191, 850], [1141, 1166], [1338, 1398], [1409, 550], [1338, 1399]]
# Drawing 3


反転リスト = [1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]  # 1なら反対から線を描く
# ------------------------------------------------

arrayCsvPath = "C:\\Users\kasahara\pro\OkanonProject\ArrayCSV\\"
skimmedArraypath = "C:\\Users\kasahara\pro\OkanonProject\SkimmedArrayCSV\\"
# arrayCsvPath = "D:\Programming\okanonproject\ArrayCSV\\"
# skimmedArraypath = "D:\Programming\okanonproject\SkimmedArrayCSV\\"


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

        dataArray = np.loadtxt(arrayCsvPath + folderName + "\\array" + str(num+1) +
                               ".csv", delimiter=",")  # 0と1の配列を取得
        resultArray = GetSkimmedArray(
            dataArray, 始点リスト[num])            # 間引いた後の座標リストを取得

        if reverseFlg == 1:
            reversedArray = list()
            for 座標 in resultArray:
                reversedArray.insert(0, 座標)

            np.savetxt(skimmedArraypath + folderName + "\\skimmedArray" + str(num + 1) +
                       ".csv", reversedArray, delimiter=",")
            # ShowGraph(reversedArray)
        else:
            np.savetxt(skimmedArraypath + folderName + "\\skimmedArray" + str(num + 1) +
                       ".csv", resultArray, delimiter=",")
            # ShowGraph(resultArray)


if __name__ == '__main__':
    main()
