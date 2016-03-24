# -*- coding: UTF-8 -*-
 
import cv2
from PIL import Image
import math
import numpy as np
import os
 
if __name__ == '__main__':

    # 顔判定で使うxmlファイルを指定する。
    cascade_path =  os.path.dirname(os.path.abspath('__file__')) + "/haarcascades/haarcascade_frontalface_alt.xml"
    cascade = cv2.CascadeClassifier(cascade_path)

    # カメラからキャプチャー
    cap = cv2.VideoCapture(0)
 
    # 画像サイズの指定
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
    cap.set(cv2.CAP_PROP_FPS,10)

    while(True):
 
        # 動画ストリームからフレームを取得
        ret, frame = cap.read()
 
        # 結果を保存するための変数を用意しておく。
        img_edit = Image.fromarray(frame)
 
        # グレースケールに変換
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #顔判定
        """
        minSize で顔判定する際の最小の四角の大きさを指定できる。
        (小さい値を指定し過ぎると顔っぽい小さなシミのような部分も判定されてしまう。)
        """
        #faces  =  cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))
        faces  =  cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(50, 50))

        # 顔があった場合
        if len(faces) > 0:

            # 複数の顔があった場合、１つずつ四角で囲っていく
            for face in faces:

                # 顔を切り抜く
                cut_face = img_edit.crop((face[0],
                                          face[1],
                                          face[0]+face[2],
                                          face[1]+face[3]))
 
                # 切り抜いた画像を1/20に縮小する。
                cut_face = cut_face.resize((int(face[2]/20), int(face[3]/20)), Image.LINEAR)
 
                # 縮小した画像を本のサイズに戻す。
                cut_face = cut_face.resize(face[2:], Image.LINEAR)
 
                # 元の画像に加工した顔画像を貼り付ける。
                img_edit.paste(cut_face, tuple(face[:2]))
 
        #pillow用のデータをOpenCVデータに変換
        img_dst = np.asarray(img_edit)

        # 表示
        cv2.imshow("Show FACES Image", img_dst)
 
        # qを押したら終了。
        k = cv2.waitKey(1)
        if k == ord('q'):
            break
 
    cap.release()
    cv2.destroyAllWindows()
