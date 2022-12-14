# camera.py

import cv2

# カメラの設定に関するクラス
class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    # カメラから撮ってきた画像をjpegにする
    def get_frame(self):
        success, image = self.video.read()
        ret, frame = cv2.imencode('.jpg', image)
        return frame