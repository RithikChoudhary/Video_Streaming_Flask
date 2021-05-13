#!/usr/bin/env python
import cv2
from flask import Flask, render_template, Response,url_for
# from camera import Camera
from imutils.video import VideoStream
import imutils


app = Flask(__name__,template_folder='template')
# videostream = VideoStream(src=0).start()
cap = cv2.VideoCapture(0)
def captureimage():
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    while True:
        ret,frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

@app.route('/')
def index():
    return render_template('index.html')
def gen():
    while True:
        ret,frame = cap.read()
        frame = imutils.resize(frame,width=600)
        (flag,encodeImage) = cv2.imencode(".jpg",frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodeImage) + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run( debug=True)