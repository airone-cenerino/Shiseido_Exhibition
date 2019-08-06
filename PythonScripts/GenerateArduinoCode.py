import numpy as np

leftFileName = "LeftMotorArrayCode.txt"
rightFileName = "RightMotorArrayCode.txt"


def main():
    file = open(leftFileName, "w")
    leftMotorStepData = np.loadtxt("LeftMotor.csv", dtype=int, delimiter=",")
    for i in range(len(leftMotorStepData)):
        file.write(str(leftMotorStepData[i]) + ",")
    file.close()

    file = open(rightFileName, "w")
    rightMotorStepData = np.loadtxt("RightMotor.csv", dtype=int, delimiter=",")
    for i in range(len(rightMotorStepData)):
        file.write(str(rightMotorStepData[i]) + ",")
    file.close()

    print("総ステップ数 : " + str(len(rightMotorStepData)))


if __name__ == '__main__':
    main()
