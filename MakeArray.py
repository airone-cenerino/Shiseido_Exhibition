import cv2
import numpy as np

img = cv2.imread("test_img.png")
array = [[0 for i in range(500)]
         for j in range(500)]   # 色があるところは0、そうでなければ1の配列。
referencePoint = [-1, 0]                                # 始点

for i in range(500):
    for j in range(500):
        if not (img[i][j][0] == 255 and img[i][j][1] == 255 and img[i][j][2] == 255):
            if referencePoint[0] == -1:
                referencePoint = [i, j]
            array[i][j] = 1

np.savetxt("array.csv", array, delimiter=",")
