


import cv2
import numpy as np
from P1Detector import P1Detector
from P2Detector import P2Detector
from ballDetector import ballDetector


class detector():
    def __init__(self, image, result):
        self.image = image
        self.result = result
    def detection(self):

        try:
            P1 = P1Detector(self.image)
            center, radius = P1.detection()
            # print(center, radius)
            P1text = "P1"
            cv2.putText(self.result, P1text, center, cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 3)
            # cv2.circle(self.result, center, radius*5, (255, 0, 0), 2)
        except:
            pass


        try:
            P2 = P2Detector(self.image)
            rect, weight = P2.detection()
        
            (x, y, w, h) = rect
            P2text = "P2"
            center = (int(x + w/2), int(y + h/2))
            cv2.putText(self.result, P2text, center, cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 3)
            cv2.rectangle(self.result, (x, y), (x + w, y + h), (0, 255, 0), 2)
        except:
            pass

        try:
            ball = ballDetector(self.image)
            radius, center = ball.detection()
            # print(center, radius)
            # balltext = "ball"
            # cv2.putText(self.result, balltext, center, cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 3)
            cv2.circle(self.result, center, radius, (0, 0, 255), 2)
            # cv2.imwrite('result.jpg', self.result)
        except:
            pass
