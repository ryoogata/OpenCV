写真系
====

face.py
----
写真を入力して、顔を識別する

```
$ python face.py photo/backs.jpg 10 10
```  

hog.py
----
写真を入力して、人物を識別する


resize.py
----
写真を入力してサイズを縮小する
    * なんか比率がおかしくなる


mosaic.py
----
写真を入力して、写真全体にモザイク処理をかける

```
$ mosaic.py photo/backs.jpg    
```

canny.py
----
写真を入力して、輪郭 ( エッジ ) の画像を出力する

Canny のエッジ検出アルゴリズムを利用


動画系
===


flame_substraction.py
----
動画から、差分を識別する


movie_face.py
----
動画から顔を識別する

    
movie_hog.py
----
動画から人物を識別する