# -*- coding: UTF-8 -*-
 
import cv2
import sys
 
if __name__ == '__main__':
    param = sys.argv

    # 画像の読み込み
    img_src = cv2.imread(param[1], 1)

    #フォントの指定
    font = cv2.FONT_HERSHEY_COMPLEX
    #font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    #font = cv2.FONT_HERSHEY_DUPLEX
    #font = cv2.FONT_HERSHEY_PLAIN
    #font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    #font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #font = cv2.FONT_HERSHEY_TRIPLEX
    #font = cv2.FONT_ITALIC

    text = "sosuke"
    font_size = 3

    #文字の書き込み
    cv2.putText(img_src,text,(100,100),font, font_size,(0,0,0))
 
    # 表示
    cv2.imshow("Show FACES Image", img_src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
