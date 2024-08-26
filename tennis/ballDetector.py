

import cv2
import numpy as np

class ballDetector():
    def __init__(self, image):
        self.image = image
    def detection(self):
        
        self.image[0:950,:,:] = 0
        self.image[:,0:500,:] = 0
        self.image[:,2600:,:] = 0

        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([35, 50, 50])
        upper_yellow = np.array([50, 255, 255])
        mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
        yellow_segment = cv2.bitwise_and(self.image, self.image, mask=mask)

        im = cv2.cvtColor(yellow_segment, cv2.COLOR_RGB2GRAY)

        ret, binary = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:

            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            # print(radius, center)

            if radius <= 2:
                return radius+15, center
        #         cv2.circle(self.image, center, radius*5, (255, 0, 0), 2)

        # cv2.imshow('Detected Circles', image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


if __name__ == "__main__":
    image = cv2.imread("frame.jpg")
    ball = ballDetector(image)
    radius, center = ball.detection()
    try:
        print(center, radius)
        cv2.circle(image, center, radius, (255, 0, 0), 2)
        cv2.imshow('Detected Circles', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        pass
    

   