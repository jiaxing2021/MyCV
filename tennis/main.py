

import cv2
import numpy as np
from P1Detector import P1Detector
from P2Detector import P2Detector
from ballDetector import ballDetector


image = cv2.imread("frame.jpg")
result = cv2.imread("frame.jpg")
P1 = P1Detector(image)
center, radius = P1.detection()
try:
    print(center, radius)
    cv2.circle(result, center, radius*5, (255, 0, 0), 2)
except:
    pass


P2 = P2Detector(image)
rects, weights = P2.detection()
try:
    for i in range(len(weights)):
            if weights[i] > 0.3:
                (x, y, w, h) = rects[i]
                cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
except:
    pass


ball = ballDetector(image)
radius, center = ball.detection()
try:
    print(center, radius)
    cv2.circle(result, center, radius, (0, 0, 255), 2)
    cv2.imwrite('result.jpg', result)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
except:
    pass





