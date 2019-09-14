import cv2
import numpy as np
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed
from collections import deque


# ------------------------------------------------
imageXLen = 2000                # 画像の横サイズ
imageYLen = 2000                # 画像の縦サイズ
folderName = "Drawing3"    # 画像フォルダ名
imageNum = 14                   # 画像の枚数
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

def MakeCSV(num):
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

    return SearchStartPoint(array, 探索開始点)

def main():
    with ProcessPoolExecutor(max_workers=8) as excuter:
        始点リスト = [excuter.submit(MakeCSV, num) for num in list(range(imageNum))]

    print(始点リスト)
    li = list()
    for future in as_completed(始点リスト):
        li.append(future.result())
    print(li)

if __name__ == '__main__':
    main()
