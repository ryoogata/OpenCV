# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import sys

if __name__ == '__main__':
    param = sys.argv

    # 画像の読み込み
    im = cv2.imread(param[1])

    # 画像のサイズを取得
    hight = im.shape[0]
    width = im.shape[1]

    # 画像サイズの変更
    half_size = cv2.resize(im,(width/2,hight/2))

    # 画像の表示
    cv2.imshow("Show Image", half_size)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
