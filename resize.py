# -*- coding: UTF-8 -*-
import cv2
import numpy as np
import sys

if __name__ == '__main__':
    param = sys.argv

    # �摜�̓ǂݍ���
    im = cv2.imread(param[1])

    # �摜�̃T�C�Y���擾
    hight = im.shape[0]
    width = im.shape[1]

    # �摜�T�C�Y�̕ύX
    half_size = cv2.resize(im,(width/2,hight/2))

    # �摜�̕\��
    cv2.imshow("Show Image", half_size)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
