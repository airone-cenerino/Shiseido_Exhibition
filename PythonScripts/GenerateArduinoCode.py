import numpy as np

# ---------------------------------------------
imageNum = 28       # 画像の枚数
folderName = "SampleImage2k"  # 画像フォルダ名
pictureNum = 0      # 何枚目の絵か
# ---------------------------------------------

MotorCSVPath = "D:\Programming\okanonproject\MotorCSV\\"
CodeTextPath = "D:\Programming\okanonproject\CodeText\\"


def main():
    file = open(CodeTextPath + folderName +
                "\\Code.txt", "w")

    for num in range(imageNum):
        leftMotorStepData = np.loadtxt(
            MotorCSVPath + folderName + "\\LeftMotor" + str(num + 1) + ".csv", dtype=int, delimiter=",")
        rightMotorStepData = np.loadtxt(
            MotorCSVPath + folderName + "\\RightMotor" + str(num + 1) + ".csv", dtype=int, delimiter=",")

        file.write("int X" + str(pictureNum) + "_" + str(num) +
                   "[] = {" + str(len(leftMotorStepData)) + ",")
        for i in range(len(leftMotorStepData)-1):
            file.write(str(leftMotorStepData[i]) + ",")
        file.write(str(leftMotorStepData[len(leftMotorStepData)-1]) + "};\n")

        file.write("int Y" + str(pictureNum) + "_" + str(num) +
                   "[] = {" + str(len(leftMotorStepData)) + ",")
        for i in range(len(rightMotorStepData)-1):
            file.write(str(rightMotorStepData[i]) + ",")
        file.write(str(rightMotorStepData[len(rightMotorStepData)-1]) + "};\n")

    file.close()


if __name__ == '__main__':
    main()
