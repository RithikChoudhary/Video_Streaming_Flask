# Abstraction of Base Class
from abc import ABC, abstractproperty

# Numpy for Image Array Storage
from numpy import array

# Opencv Modules
from cv2 import VideoCapture, imencode, cvtColor, COLOR_BGR2RGB

# Screen Capture Utility
import pyautogui

# Flask Modules
from flask import Response

# Annotation
from typing import Generator

class __shareable(ABC):
	'''
	A general abstract class for 
	all the classes which provide 
	different functionality and have 
	some shareable component example 
	webcam, screen etc.
	'''

	def encoded(self, frame) -> bytes:
		'''
		Encode the frame into bytes, 
		convert to jpg format and and 
		return the exact response to 
		render through flask
		'''
		frame = 							 			\
			b'--frame\r\n' +							\
			b'Content-Type: image/jpeg\r\n\r\n' +		\
			bytearray(imencode(".webp",frame)[1]) + 	\
			b'\r\n'										
		
		return frame

	@abstractproperty
	def feed() -> Generator[bytes, None, None]:
		'''
		The Video/Screen/Image/Audio sharing feed 
		that will be generally shared throught this class
		'''
		pass
	

class _webcam_sharing(__shareable):
	'''
	Inherited from the __shareable class, 
	it shares the live webcam 
	through the feed property.
	'''
	def __init__(self, stream_name = 0) -> None:
		self.cam = VideoCapture(stream_name)

	@property
	def feed(self) -> Generator[bytes, None, None]:
		'''
		Yields actual Video feed, 
		as captured by the camera, 
		in the form of a 
		byte-encoded response string
		'''
		while True:
			# self.cam.grab()

			frame = self.cam.read()[1]
			
			try:
				yield(self.encoded(frame))
			except Exception as e:
				print(e)
				self.cam.release()
				exit(1)

	def __del__(self) -> None:
		self.cam.release()


class _screen_sharing(__shareable):
	'''
	Inherited from the __shareable class, 
	it shares the live monitor screen 
	through the feed property.
	'''
	@property
	def feed(self) -> Generator[bytes, None, None]:
		'''
		Yields actual Screen Sharing as a 
		video feed in the form of a 
		byte-encoded response string.
		'''
		while True:
			frame = array(pyautogui.screenshot())
			frame = cvtColor(frame, COLOR_BGR2RGB)
			try:
				yield(self.encoded(frame))
			except Exception as e:
				print(e)
				exit(1)

my_webcam = _webcam_sharing()
my_screen = _screen_sharing()

def livestream_webcam_response() -> Response:
	'''
	Uses the byte-encoded feed 
	of the webcam's view
	and returns a robust
	Flask-Response object
	'''
	return Response(
		my_webcam.feed,
		mimetype='multipart/x-mixed-replace; boundary=frame'
	)


def livestream_screen_response() -> Response:
	'''
	Uses the byte-encoded feed 
	of the screen-shareing,
	and returns a robust
	Flask-Response object
	'''
	return Response(
		my_screen.feed,
		mimetype='multipart/x-mixed-replace; boundary=frame'
	)
