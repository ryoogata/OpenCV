# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import sys

def half_size(im):
        hight = im.shape[0]
        width = im.shape[1]
        half_size = cv2.resize(im,(hight/2,width/2))

        cv2.imshow("half_size",half_size)
        cv2.waitKey(0)

        # 画像保存
        out_file_name = "after.jpg"
        cv2.imwrite(out_file_name,half_size)

        cv2.destroyAllWindows()  

if __name__ == '__main__':
    param = sys.argv

    im = cv2.imread(param[1])
    if not (im == None):
        half_size(im)
    else:
        print 'Not exist'
