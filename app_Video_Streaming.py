#!/usr/bin/env python
import cv2
from flask import Flask, render_template, Response

app = Flask(__name__,template_folder='template')
cap = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')


def gen():
    while True:
        ret,frame = cap.read()
        
        (flag,encodeImage) = cv2.imencode(".jpg",frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodeImage) + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run( debug=True)
