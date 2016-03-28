# -*- coding: UTF-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt
import datetime

if __name__ == '__main__':

    img = cv2.imread('../photo/20160328_125518.jpg',1)
    #img = cv2.imread('../photo/20160328_130040.jpg',1)
    template = cv2.imread('../photo/cap_empty.png',0)
    w, h = template.shape[::-1]

    # All the 6 methods for comparison in a list
    #methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    method = "cv2.TM_CCOEFF"

    # Apply template Matching
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray,template,eval(method))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    dst = img[top_left[1]:top_left[1]+h, top_left[0]:top_left[0]+w]

    # 表示
    cv2.imshow("Show FACES Image", dst)

    #キーボード入力を受け付ける
    key = cv2.waitKey(0)

    if key == 27:            #escの処理
        cv2.destroyAllWindows()
    elif key == ord('s'):      #sの入力の処理
        now = datetime.datetime.now()
        cv2.imwrite("../photo/{0:%Y%m%d_%H%M%S}.jpg".format(now), dst)
        cv2.destroyAllWindows()
