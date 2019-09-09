import cv2
import numpy as np
from collections import deque


# ------------------------------------------------
imageXLen = 2000                # 画像の横サイズ
imageYLen = 2000                # 画像の縦サイズ
folderName = "Drawing2"    # 画像フォルダ名
imageNum = 45                   # 画像の枚数
# ------------------------------------------------

imagePath = "C:\\Users\kasahara\pro\OkanonProject\Images\\"
csvPath = "C:\\Users\kasahara\pro\OkanonProject\ArrayCSV\\"
#imagePath = "D:\Programming\okanonproject\Images\\"
#csvPath = "D:\Programming\okanonproject\ArrayCSV\\"

拡張子 = ".png"


def SearchStartPoint(array, 探索開始点):
    y = [1, -1, 0, 0, 1, 1, -1, -1]
    x = [0, 0, 1, -1, 1, -1, 1, -1]
    q = deque()                 # キュー
    q.append(探索開始点)
    distance = 0                # 支点からの距離
    lastPoint = list()          # 終点を記録するためだけに作った

    while q:
        distance += 1
        points = list()

        while q:    # 距離distance-1の点たちをすべて取り出す
            points.append(q.pop())

        for referencePoint in points:
            for i in range(8):
                if array[referencePoint[0] + y[i]][referencePoint[1] + x[i]] == 1:  # 隣り合う点が見つかったら
                    q.append([referencePoint[0] + y[i],
                              referencePoint[1] + x[i]])
                    array[referencePoint[0] + y[i]
                          ][referencePoint[1] + x[i]] = 0

                    lastPoint = [referencePoint[0] +
                                 y[i], referencePoint[1] + x[i]]

    return lastPoint


def main():
    始点リスト = list()
    for num in range(imageNum):
        print(str(num+1) + "枚目処理開始")

        img = cv2.imread(imagePath + folderName + "\\" +
                         str(num+1) + 拡張子)   # 画像読み込み
        array = [[0 for i in range(imageXLen)]
                 for j in range(imageYLen)]  # 色があるところは0、そうでなければ1の配列を宣言

        探索開始点 = list()

        for i in range(imageYLen):
            if i % 200 == 0:
                print("■ ", end="")
            for j in range(imageXLen):
                if not (img[i][j][0] == 255 and img[i][j][1] == 255 and img[i][j][2] == 255):
                    array[i][j] = 1
                    探索開始点 = [i, j]

        np.savetxt(csvPath + folderName + "\\array" +
                   str(num+1) + ".csv", array, delimiter=",")

        始点リスト.append(SearchStartPoint(array, 探索開始点))
        print()
        print(str(num+1) + "枚目の始点 : " + str(始点リスト[num]))

    print("始点のリスト")
    print(始点リスト)


if __name__ == '__main__':
    main()
