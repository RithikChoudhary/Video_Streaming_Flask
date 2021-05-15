# Flask Modules 
from flask import Flask, render_template

# Our Core Live Stream Function
from flaskvideostream import livestream_webcam_response, livestream_screen_response

server = Flask(__name__)

@server.route('/')
def index_page():
    return render_template('index.html')

@server.route('/webcam')
def webcam():
    return livestream_webcam_response()


@server.route('/screen')
def screen():
    return livestream_screen_response()


if __name__ == '__main__':
    try:
        server.run()
    except Exception as e:
        print(e)
