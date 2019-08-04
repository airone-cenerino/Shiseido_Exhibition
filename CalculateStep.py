import numpy as np
import math

# ---------------------------------------------
xLen = 200      # 紙の横の長さ(cm)
yLen = 200      # 紙の縦の長さ(cm)
imageXLen = 500  # 画像の横サイズ
imageYLen = 500  # 画像の縦サイズ
centiToDegreeRatio = 60.0    # 1cm伸ばすのに必要な回転角度
# ---------------------------------------------


def CalculateMotorMoveValue(lastPoint, nextPoint):
    # print("last:" + str(lastPoint))
    # print("next:" + str(nextPoint))

    # 現在のひもの長さを計算
    last直交座標y = lastPoint[0] / imageYLen * yLen
    last直交座標x = lastPoint[1] / imageXLen * xLen
    lastLeftStringLen = math.sqrt(last直交座標y ** 2 + last直交座標x ** 2)
    lastRightStringLen = math.sqrt(last直交座標y ** 2 + (xLen - last直交座標x) ** 2)

    # print("last : (" + str(lastLeftStringLen) +
    #       ", " + str(lastRightStringLen) + ")")

    # 次の点でのひもの長さを計算
    next直交座標y = nextPoint[0] / imageYLen * yLen
    next直交座標x = nextPoint[1] / imageXLen * xLen
    nextLeftStringLen = math.sqrt(next直交座標y ** 2 + next直交座標x ** 2)
    nextRightStringLen = math.sqrt(next直交座標y ** 2 + (xLen - next直交座標x) ** 2)

    # print("next : (" + str(nextLeftStringLen) +
    #       ", " + str(nextRightStringLen) + ")")

    # 差分を返す
    return centiToDegreeRatio * (nextLeftStringLen - lastLeftStringLen), centiToDegreeRatio * (nextRightStringLen - lastRightStringLen)


def main():
    startPoint = [imageYLen/2, imageYLen/2]  	# 基準点
    lastPoint = startPoint  					# ペンがどこにいるか
    array = np.loadtxt("skimmedArray.csv", delimiter=",")  # 0と1の配列を取得

    for point in array:
        print()
        print("(" + str(point[0]) + ", " + str(point[1]) + ")")

        left, right = CalculateMotorMoveValue(lastPoint, point)
        lastPoint = point

        print(str(left) + ", " + str(right))

    # ここで終点から原点に戻すコードを書く


if __name__ == '__main__':
    main()
