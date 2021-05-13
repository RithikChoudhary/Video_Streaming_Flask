import cv2


cap = cv2.VideoCapture(0)
def captureimage():
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')
    while True:
        ret,frame = cap.read()
    
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
captureimage()
cap.release()
cv2.destroyAllWindows()