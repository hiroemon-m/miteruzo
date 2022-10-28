# camera.py

import cv2

# カメラの設定に関するクラス
class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(-1)
        print("インスタンス生成")
        print(self.video)

    def __del__(self):
        self.video.release()
        print("deleted")

    # カメラから撮ってきた画像をjpegにする
    def get_frame(self):
        success, image = self.video.read()
        # print("カメラから画像を読み込む")
        # print(success, image)
        ret, frame = cv2.imencode('.jpg', image)
        # print("画像をjpgにエンコード")
        print(ret, frame)
        return frame