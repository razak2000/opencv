import cv2
from cv2 import *
import sys
from movienet.tools import FaceDetector

img = cv2.imread('/home/abdul/github/movienet-tools/tests/data/still01.jpg')
# img = cv2.imread('./resources/images/car.jpg', IMREAD_GRAYSCALE)

if img is None:
    sys.exit('Could not read the image')

cv2.imshow("Display window", img)

k = cv2.waitKey(0)

if k == ord("s"):
    cv2.imwrite('car.png', img)
