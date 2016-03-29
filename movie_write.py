# -*- coding: UTF-8 -*-
import numpy as np
import cv2
 
if __name__ == '__main__':

    # カメラからキャプチャー
    cap = cv2.VideoCapture(0)

    # 画像サイズの指定
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
    #cap.set(cv2.CAP_PROP_FPS,30)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))

    while(True):
 
        # 動画ストリームからフレームを取得
        ret, frame = cap.read()

        # フレームの保存
        out.write(frame)
 
        # 表示
        cv2.imshow("Show FACES Image", frame)
 
        # qを押したら終了。
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
 
    cap.release()
    out.release()
    cv2.destroyAllWindows()
