# -*- coding: utf-8 -*-
 
import cv2
import numpy as np
import sys
 
if __name__ == '__main__':
    param = sys.argv
 
    # ファイル読み込み
    img_src = cv2.imread(param[1])
    img_keypoint = img_src
 
    # キーポイントの検出
    gftt = cv2.FastFeatureDetector_create()
    keypoints = gftt.detect(img_src)
 
    # キーポイントの数をターミナル上に表示
    print(len(keypoints))
 
    # 表示
    img_keypoint = cv2.drawKeypoints(img_src, keypoints, img_keypoint)
    cv2.imshow("SHOW KEYPOINTS IMAGE", img_keypoint)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
