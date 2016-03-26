# -*- coding: utf-8 -*-

import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
while(1):
 
    # フレームを取得
    ret, frame = cap.read()
 
    # フレームをHSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
    # 取得する色の範囲を指定する

    # 黄色の場合
    # lower_color = np.array([20, 50, 50])
    # upper_color = np.array([100, 255, 255])

    # 肌色の場合
    lower_color = np.array([0, 58, 88])
    upper_color = np.array([25, 173, 229])
 
    # 指定した色に基づいたマスク画像の生成
    img_mask = cv2.inRange(hsv, lower_color, upper_color)
 
    # フレーム画像とマスク画像の共通の領域を抽出する。
    img_color = cv2.bitwise_and(frame, frame, mask=img_mask)
 
    cv2.imshow("SHOW COLOR IMAGE", img_color)
 
    # qを押したら終了
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()
