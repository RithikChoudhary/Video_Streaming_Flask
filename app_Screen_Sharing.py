#!/usr/bin/env python
from types import FrameType
import cv2
from flask import Flask, render_template, Response,url_for
import imutils
import numpy as np
import pyautogui
app = Flask(__name__,template_folder='template')
@app.route('/')
def index():
    return render_template('index.html')
def gen():
    while True:
        cap = pyautogui.screenshot()
        # ret,frame = cap.read()
        frame= np.array(cap)
        (flag,encodeImage) = cv2.imencode(".jpg",frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodeImage) )
@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run( debug=True)
