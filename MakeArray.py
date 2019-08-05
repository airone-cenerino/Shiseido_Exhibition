import cv2
import numpy as np

# ------------------------------------------------
imageXLen = 1000  # 画像の横サイズ
imageYLen = 1000  # 画像の縦サイズ
imageName = "1000.png"
# ------------------------------------------------

img = cv2.imread(imageName)
array = [[0 for i in range(imageXLen)]
         for j in range(imageYLen)]   # 色があるところは0、そうでなければ1の配列。


for i in range(imageYLen):
    for j in range(imageXLen):
        if not (img[i][j][0] == 255 and img[i][j][1] == 255 and img[i][j][2] == 255):
            array[i][j] = 1

np.savetxt("array.csv", array, delimiter=",")
