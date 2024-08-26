

import cv2
import numpy as np

class ballDetector():
    def __init__(self, image):
        self.image = image
    def detection(self):
        
        # covert to YUV color space
        yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
        yuv_image[:,:,0] = cv2.equalizeHist(yuv_image[:,:,0])
        equalized_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)

        # conver to HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        lower_yellow = np.array([30, 90, 90])
        upper_yellow = np.array([45, 255, 255])
        mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
        yellow_segment_1 = cv2.bitwise_and(image, image, mask=mask)

        lower_yellow = np.array([30, 50, 50])
        upper_yellow = np.array([45, 255, 255])
        mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
        yellow_segment_2 = cv2.bitwise_and(image, image, mask=mask)

        # yellow_segment = yellow_segment_1 - yellow_segment_2

        # # blur
        # kernel_size = (2, 2)  
        # smoothed_image = cv2.blur(yellow_segment_2, kernel_size)
        im = cv2.cvtColor(yellow_segment_2, cv2.COLOR_RGB2GRAY)
        ret, binary = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # 拟合每个轮廓的最小包围圆
        for contour in contours:
            # 获取最小包围圆的圆心和半径
            (x, y), radius = cv2.minEnclosingCircle(contour)
            center = (int(x), int(y))
            radius = int(radius)
            
            # 绘制轮廓
            cv2.drawContours(im, [contour], -1, (0, 255, 0), 2)
            
            # 绘制拟合的圆
            cv2.circle(im, center, radius, (255, 0, 0), 2)

        cv2.imwrite('ball.jpg', im)

       

if __name__ == "__main__":
    image = cv2.imread("frame.jpg")

    image[0:950,:,:] = 0

    image[:,0:500,:] = 0
    image[:,2600:,:] = 0

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_yellow = np.array([35, 50, 50])
    upper_yellow = np.array([50, 255, 255])
    mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    yellow_segment = cv2.bitwise_and(image, image, mask=mask)

    im = cv2.cvtColor(yellow_segment, cv2.COLOR_RGB2GRAY)

    ret, binary = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:

        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        print(radius, center)

        if radius <= 2:
            cv2.circle(image, center, radius*5, (255, 0, 0), 2)

    


