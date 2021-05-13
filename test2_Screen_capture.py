import cv2
import pyautogui
import numpy as np

def captureimage():
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    while True:
        cap = pyautogui.screenshot()
        frame = np.array(cap)
        # ret,frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
        
captureimage()
# cap.release()
cv2.destroyAllWindows()
