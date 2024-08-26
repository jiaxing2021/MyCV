

import cv2
import numpy as np

class P1Detector():
    def __init__(self, image):
        self.image = image
    def detection(self):

        # conver to HSV color space
        hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])

        mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

        yellow_segment = cv2.bitwise_and(self.image, self.image, mask=mask)

        im = cv2.cvtColor(yellow_segment, cv2.COLOR_RGB2GRAY)

        ret, binary = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 拟合每个轮廓的最小包围圆
        for contour in contours:
            # 获取最小包围圆的圆心和半径
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)

            if radius > 0:
                return center, radius
            
            # # 绘制轮廓
            # cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
            
            # 绘制拟合的圆
            # cv2.circle(image, center, radius*5, (255, 0, 0), 2)

        # cv2.imwrite('P1.jpg', image)


if __name__ == "__main__":
    image = cv2.imread("frame.jpg")
    P1 = P1Detector(image)
    # P1.detection()
    center, radius = P1.detection()
    print(center, radius)

    text = "P1"

    cv2.putText(image, text, center, cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 0, 0), 3)
    # cv2.circle(image, center, radius*5, (255, 0, 0), 2)
    cv2.imwrite('P1.jpg', image)


