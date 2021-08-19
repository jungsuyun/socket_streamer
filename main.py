from queue import Queue
from typing import Any
import numpy as np

from flask import Flask, render_template, Response, jsonify
import cv2
import threading
import queue

global te
te = []


class VideoThread:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.frame = None
        self.my_thread = threading.Thread(target=self.capture_thread)
        self.my_thread.start()
        self.lock = threading.Lock()

    def capture_thread(self):
        if self.capture.isOpened():
            while True:
                global te
                ret, frame = self.capture.read()
                if ret:
                    te.append(frame)
                    print(len(te))
                    # q.put(frame)
                    # print(type(frame), q.qsize())

    def get_frame(self):
        if self.frame is not None:
            return self.frame
        else:
            print("NONE!!")


q = queue.Queue()
video = VideoThread()

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route('/test')
def get_camera():
    capture = cv2.VideoCapture(0)
    ret, buffer = capture.read()
    if ret:
        frame = cv2.imencode('.jpg', buffer)[1].tobytes()
        print(buffer.shape)
        return frame


@app.route('/test2')
def get_camera2():
    global te
    video.lock.acquire()
    print(len(te), type(te))
    video.lock.release()
    return str(len(te))


#     print(type(video.get_frame()))
#     return str(video.get_frame())


@app.route('/hi')
def speed_test():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.30', threaded=True)
