# -*- coding: UTF-8 -*-
import cv2
import datetime
 
if __name__ == '__main__':

    # カメラからキャプチャー
    cap = cv2.VideoCapture(0)

    # カメラスペック情報の取得
    frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

    # 画像サイズの指定
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,frame_height)
    cap.set(cv2.CAP_PROP_FPS,30)
 
    while(True):
 
        # 動画ストリームからフレームを取得
        ret, frame = cap.read()
 
        # 表示
        cv2.imshow("Show FACES Image", frame)
 
        #キーボード入力を受け付ける
        key = cv2.waitKey(1)

        if key == 27:            #escの処理
            break
        elif key == ord('s'):      #sの入力の処理
            now = datetime.datetime.now()
            cv2.imwrite("photo/{0:%Y%m%d_%H%M%S}.jpg".format(now), frame)
            break

    cap.release()
    cv2.destroyAllWindows()
