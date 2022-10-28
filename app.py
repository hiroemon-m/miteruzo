import cv2
from flask import Flask, render_template, Response

from camera import Camera

app = Flask(__name__, static_folder='./templates/images')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream")
def stream():
    return render_template("stream.html")

# カメラからフレーム取得できる限り、画像を返す関数
def gen(camera):
    while True:
        frame = camera.get_frame()
        print("カメラインスタンスからフレームを取得")
        print(frame)


        if frame is not None:
            yield (b"--frame\r\n"
                b"Content-Type: image/jpeg\r\n\r\n" + frame.tobytes() + b"\r\n")
        else:
            print("frame is none")

@app.route("/video_feed")
def video_feed():
    return Response(gen(Camera()),
            mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=3000)