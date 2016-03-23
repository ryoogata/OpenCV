# -*- coding: UTF-8 -*-
import cv2
import sys
 
if __name__ == '__main__':

    # カメラからキャプチャー
    cap = cv2.VideoCapture(0)
 
    while(True):
 
        # 動画ストリームからフレームを取得
        ret, frame = cap.read()
 
        # 結果を保存するための変数を用意しておく。
        img_result = frame

        # HoG特徴量の計算
        hog = cv2.HOGDescriptor()

        # SVMによる人検出
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
        hogParams = {'winStride': (8, 8), 'padding': (32, 32), 'scale': 1.05}

        # 人を検出した座標
        human, r = hog.detectMultiScale(frame, **hogParams)

        # 長方形で人を囲う
        for (x, y, w, h) in human:
            cv2.rectangle(frame, (x, y),(x+w, y+h),(0,50,255), 3)

        # 表示
        cv2.imshow("Show FACES Image", frame)
 
        # qを押したら終了。
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
 
    cap.release()
    cv2.destroyAllWindows()
