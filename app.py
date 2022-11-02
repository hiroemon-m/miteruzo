import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2

st.title("My first Streamlit app")
st.write("Hello, world")

threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)
threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=200)


def callback(frame):
    img = frame.to_ndarray(format="bgr24")

    img = cv2.cvtColor(cv2.Canny(img, threshold1, threshold2), cv2.COLOR_GRAY2BGR)

    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(
    key="example",
    video_frame_callback=callback,
    rtc_configuration={  # Add this line
        "iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]
    }
)


# import cv2
# from flask import Flask, render_template, Response

# from camera import Camera

# app = Flask(__name__, static_folder='./templates/images')


# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/stream")
# def stream():
#     return render_template("stream.html")

# # カメラからフレーム取得できる限り、画像を返す関数
# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         print("カメラインスタンスからフレームを取得")
#         print(frame)


#         if frame is not None:
#             yield (b"--frame\r\n"
#                 b"Content-Type: image/jpeg\r\n\r\n" + frame.tobytes() + b"\r\n")
#         else:
#             print("frame is none")

# @app.route("/video_feed")
# def video_feed():
#     return Response(gen(Camera()),
#             mimetype="multipart/x-mixed-replace; boundary=frame")


# if __name__ == "__main__":
#     app.debug = True
#     app.run(host="0.0.0.0", port=3000)