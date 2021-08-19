import cv2
from flask import Flask
import time

app = Flask(__name__)
capture = cv2.VideoCapture(0)

@app.route('/')
def index():
    return "hello world"

@app.route('/hi')
def get_frame():
    start_time = time.time()
    ret, frame = capture.read()
    if ret:
        frame_byte = cv2.imencode('*.jpg', frame)[1].tobytes()
        return frame_byte


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7079, debug=True)