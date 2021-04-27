import numpy as np 
import cv2 as cv 

# cap = cv.VideoCapture('./resources/videos/spark_catalyst.mp4')
cap = cv.VideoCapture('./resources/videos/lecture.mkv')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('cant receive frame(stream end?)')
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()
