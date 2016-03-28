# -*- coding: UTF-8 -*-
import cv2
import numpy as np

if __name__ == '__main__':
    # カメラからキャプチャー
    cap = cv2.VideoCapture(0)

    template = cv2.imread('photo/cap_empty.png',0)
    w, h = template.shape[::-1]
    
    # All the 6 methods for comparison in a list
    #methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

    method = "cv2.TM_CCOEFF"

    while(True):

        # 動画ストリームからフレームを取得
        ret, frame = cap.read()

        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        # Apply template Matching
        res = cv2.matchTemplate(img_gray,template,eval(method))
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(frame,top_left, bottom_right, 255, 2)

        # 表示
        cv2.imshow("Show FACES Image", frame)
 
        # qを押したら終了。
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
 
    cap.release()
    cv2.destroyAllWindows()
