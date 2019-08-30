import numpy as np
import math

# ---------------------------------------------
xLen = 104          # 紙の横の長さ(cm)
yLen = 104          # 紙の縦の長さ(cm)
imageXLen = 2000    # 画像の横サイズ
imageYLen = 2000    # 画像の縦サイズ
cmToStepRatio = 400  # 1cm伸ばすのに必要なステップ数
imageNum = 28       # 画像の枚数
folderName = "SampleImage2k"    # 画像フォルダ名
# ---------------------------------------------

skimmedArrayPath = "C:\\Users\kasahara\pro\OkanonProject\SkimmedArrayCSV\\"
MotorCSVPath = "C:\\Users\kasahara\pro\OkanonProject\MotorCSV\\"
# skimmedArrayPath = "D:\Programming\okanonproject\SkimmedArrayCSV\\"
# MotorCSVPath = "D:\Programming\okanonproject\MotorCSV\\"


startPointStringLen = [math.sqrt(
    (yLen/2)**2 + (xLen/2)**2), math.sqrt((yLen/2)**2 + (xLen/2)**2)]  # 基準点でのひもの長さ (cm)
lastStep = [0, 0]         # 直前の原点からのステップ数


def CalculateMotorMoveValue(nextPoint):
    global lastStep

    直交座標 = [nextPoint[0] / imageYLen * yLen,
            nextPoint[1] / imageXLen * xLen]   # 点の直交座標での座標
    StringLen = [math.sqrt(直交座標[0] ** 2 + 直交座標[1] ** 2),
                 math.sqrt(直交座標[0] ** 2 + (xLen - 直交座標[1]) ** 2)]   # その点でのひもの長さ
    原点からの変化量 = [StringLen[0]-startPointStringLen[0],
                StringLen[1]-startPointStringLen[1]]
    原点からのステップ変化量 = [原点からの変化量[0] * cmToStepRatio, 原点からの変化量[1] * cmToStepRatio]
    前回からのステップ変化量 = [原点からのステップ変化量[0]-lastStep[0], 原点からのステップ変化量[1]-lastStep[1]]

    lastStep = 原点からのステップ変化量

    return 前回からのステップ変化量


def main():
    global lastStep

    現在位置 = [0, 0]
    テスト用配列左 = list()
    テスト用配列右 = list()

    for num in range(imageNum):
        array = np.loadtxt(skimmedArrayPath + folderName + "\\skimmedArray"+str(num+1)+".csv",
                           delimiter=",")  # 座標のデータを取得
        left = list()
        right = list()

        for point in array:
            step = CalculateMotorMoveValue(point)  # 次の点を渡して、動かすステップ数を取得
            left.append(int(step[0]))
            right.append(int(step[1]))
            現在位置[0] += int(step[0])
            現在位置[1] += int(step[1])
            テスト用配列左.append(int(step[0]))
            テスト用配列右.append(int(step[1]))

        if num + 1 == imageNum:
            # 絵の最後は原点に戻る
            left.append(-現在位置[0])
            right.append(-現在位置[1])
            テスト用配列左.append(-現在位置[0])
            テスト用配列右.append(-現在位置[1])

            現在位置[0] -= 現在位置[0]
            現在位置[1] -= 現在位置[1]

        np.savetxt(MotorCSVPath + folderName + "\\LeftMotor" +
                   str(num+1)+".csv", left, delimiter=",")
        np.savetxt(MotorCSVPath + folderName + "\\RightMotor" +
                   str(num + 1) + ".csv", right, delimiter=",")
        np.savetxt(MotorCSVPath + folderName +"\\LeftMotor.csv", テスト用配列左, delimiter=",")
        np.savetxt(MotorCSVPath + folderName +"\\RightMotor.csv", テスト用配列右, delimiter=",")

        print(str(num + 1) + "番目の画像")
        print(現在位置)

        lastStep = 現在位置


if __name__ == '__main__':
    main()
