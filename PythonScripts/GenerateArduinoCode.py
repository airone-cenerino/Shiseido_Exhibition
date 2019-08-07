import numpy as np

# ---------------------------------------------
imageNum = 28       # 画像の枚数
folderName = "SampleImage2k\\"    # 画像フォルダ名
# ---------------------------------------------

path = "D:\Programming\okanonproject\MotorCSV\\"


def main():
    for num in range(imageNum):
        file = open("LeftMotorArrayCode" + str(num+1) + ".txt", "w")
        leftMotorStepData = np.loadtxt(
            path + folderName + "LeftMotor" + str(num+1) + ".csv", dtype=int, delimiter=",")
        for i in range(len(leftMotorStepData)):
            file.write(str(leftMotorStepData[i]) + ",")
        file.close()

        file = open("RightMotorArrayCode" + str(num+1) + ".txt", "w")
        rightMotorStepData = np.loadtxt(
            path + folderName + "RightMotor" + str(num+1) + ".csv", dtype=int, delimiter=",")
        for i in range(len(rightMotorStepData)):
            file.write(str(rightMotorStepData[i]) + ",")
        file.close()
        print(str(num+1) + "枚目の総ステップ数 : " + str(len(rightMotorStepData)))


if __name__ == '__main__':
    main()
