import cv2
from flask import Flask, render_template, Response, request, url_for, redirect

from camera import Camera
import os

app = Flask(__name__, static_folder='./templates/images')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream")
def stream():
    return render_template("stream.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # URLでhttp://127.0.0.1:5000/uploadを指定したときはGETリクエストとなるのでこっち
    if request.method == 'GET':
        return render_template('upload.html')
    # formでsubmitボタンが押されるとPOSTリクエストとなるのでこっち
    elif request.method == 'POST':
        file = request.files['example']
        file.save(os.path.join('templates/images', file.filename))
        return redirect(url_for('uploaded_file', filename=file.filename))


@app.route('/uploaded_file/<string:filename>')
def uploaded_file(filename):
    return render_template('uploaded_file.html', filename=filename)

# カメラからフレーム取得できる限り、画像を返す関数
def gen(camera):
    while True:
        frame = camera.get_frame()

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