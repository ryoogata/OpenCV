# -*- coding: utf-8 -*-
# 彩度の平均を計算

import cv2
import numpy as np
import sys

if __name__ == '__main__':
    param = sys.argv

    # 写真の読み込み
    img_bgr = cv2.imread(param[1])
    
    # 画像をBGRからHSV色空間に変換
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    
    # 彩度が0より大きい点のみを採用
    valid_hue_list = [[ hsv[0] for hsv in img_line if hsv[1] > 0] for img_line in img_hsv]
    
    # 彩度の平均を計算
    average_hue = (sum([sum(line) for line in valid_hue_list]) /
    float(sum([len(line) for line in valid_hue_list])))
    
    print average_hue
