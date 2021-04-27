import numpy as np 
import cv2 as cv

cap = cv.VideoCapture('./resources/videos/layer.mp4')

# define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVDI')
out = cv.VideoWriter('layer.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('can\'t receive frame (stream end)')
        break 
    frame = cv.flip(frame, 0)
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break 

cap.release()
out.release()
cv.destroyAllWindows()

