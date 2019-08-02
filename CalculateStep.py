import numpy as np


def CalculateMotorMoveValue(lastPoint, nextPoint):
        # 現在のひもの長さを計算
        # 次の点でのひもの長さを計算
        # 差分を返す

    return nextPoint[0] - lastPoint[0], nextPoint[1] - lastPoint[1]


def main():
    startPoint = [250, 250]  # 基準点

    lastPoint = startPoint  # ペンがどこにいるか
    array = np.loadtxt("skimmedArray.csv", delimiter=",")  # 0と1の配列を取得

    for point in array:
        print("(" + str(point[0]) + ", " + str(point[1]) + ")")

        left, right = CalculateMotorMoveValue(lastPoint, point)
        lastPoint = point

        print(str(left) + ", " + str(right))


if __name__ == '__main__':
    main()
