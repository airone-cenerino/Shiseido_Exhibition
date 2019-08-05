import numpy as np
import math

# ---------------------------------------------
xLen = 200      # 紙の横の長さ(cm)
yLen = 200      # 紙の縦の長さ(cm)
imageXLen = 1000  # 画像の横サイズ
imageYLen = 1000  # 画像の縦サイズ
cmToStepRatio = 400    # 1cm伸ばすのに必要なステップ数
# ---------------------------------------------

startPointStringLen = [math.sqrt((yLen/2)**2 + (xLen/2)**2), math.sqrt((yLen/2)**2 + (xLen/2)**2)]  # 基準点でのひもの長さ (cm)
lastStep = [0, 0]         # 直前の原点からのステップ数

print(startPointStringLen)

def CalculateMotorMoveValue(nextPoint):
    global lastStep

    直交座標 = [nextPoint[0] / imageYLen * yLen, nextPoint[1] / imageXLen * xLen]   # 点の直交座標での座標
    StringLen = [math.sqrt(直交座標[0] ** 2 + 直交座標[1] ** 2), math.sqrt(直交座標[0] ** 2 + (xLen - 直交座標[1]) ** 2)]   # その点でのひもの長さ
    原点からの変化量 = [StringLen[0]-startPointStringLen[0], StringLen[1]-startPointStringLen[1]]
    原点からのステップ変化量 = [原点からの変化量[0] * cmToStepRatio, 原点からの変化量[1] * cmToStepRatio]
    前回からのステップ変化量 = [原点からのステップ変化量[0]-lastStep[0], 原点からのステップ変化量[1]-lastStep[1]] 

    lastStep = 原点からのステップ変化量

    return 前回からのステップ変化量

def main():
    array = np.loadtxt("skimmedArray.csv", delimiter=",")  # 座標のデータを取得
    left = list()
    right = list()
    

    for point in array:
        step = CalculateMotorMoveValue(point)  # 次の点を渡して、動かすステップ数を返す
        left.append(int(step[0]))
        right.append(int(step[1]))

    np.savetxt("LeftMotor.csv", left, delimiter=",")
    np.savetxt("RightMotor.csv", right, delimiter = ",")

    print(sum(left))    # 原点からの総ステップ
    print(sum(right))

if __name__ == '__main__':
    main()
