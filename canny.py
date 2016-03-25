# -*- coding: UTF-8 -*-
 
import cv2
import math
import numpy as np
import os
import sys
 
if __name__ == '__main__':
    param = sys.argv

    # 画像の読み込み
    img_src = cv2.imread(param[1], 1)
 
    lines = img_src.copy()

    # 輪郭を抽出する
    canny = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    canny = cv2.GaussianBlur(canny, (5, 5), 0)
    canny = cv2.Canny(canny, 50, 100)
    cv2.imshow('canny', canny)
 
    # 表示
    cv2.waitKey(0)
    cv2.destroyAllWindows()
