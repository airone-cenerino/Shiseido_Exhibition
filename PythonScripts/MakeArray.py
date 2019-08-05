import cv2
import numpy as np

# ------------------------------------------------
imageXLen = 1000  # 画像の横サイズ
imageYLen = 1000  # 画像の縦サイズ
imageName = "beautifulArt.png"
# ------------------------------------------------

path = "D:\Programming\okanonproject\Images"


def main():
    img = cv2.imread(path + "\\" + imageName)   # 画像読み込み
    array = [[0 for i in range(imageXLen)]
             for j in range(imageYLen)]   # 色があるところは0、そうでなければ1の配列を宣言

    for i in range(imageYLen):
        for j in range(imageXLen):
            if not (img[i][j][0] == 255 and img[i][j][1] == 255 and img[i][j][2] == 255):
                array[i][j] = 1

    np.savetxt("array.csv", array, delimiter=",")


if __name__ == '__main__':
    main()
