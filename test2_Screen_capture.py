import cv2
import pyautogui
import numpy as np

def captureimage():

    while True:
        cap = pyautogui.screenshot()
        frame = np.array(cap)
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
        
captureimage()

cv2.destroyAllWindows()
