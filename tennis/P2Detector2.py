



import cv2
import numpy as np

class P2Detector():
    def __init__(self, image):
        self.image = image
    def detection(self):
        im = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        im[0:900,:] = 0
        im[1100:,:] = 0

        im[:,0:1400] = 0
        im[:,3000:] = 0

        # ykernel = np.zeros((3, 3), dtype=np.float32)
        # ykernel[:,0] = -1
        # ykernel[:,1] = 0
        # ykernel[:,2] = 1

        # convolved_imagey = cv2.filter2D(im, -1, ykernel)

        # xkernel = np.zeros((3, 3), dtype=np.float32)
        # xkernel[0,:] = -1
        # xkernel[1,:] = 0
        # xkernel[2,:] = 1

        # convolved_imagex = cv2.filter2D(im, -1, xkernel)

        # result = cv2.bitwise_or(convolved_imagey, convolved_imagex)


        hog = cv2.HOGDescriptor()
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        (rects, weights) = hog.detectMultiScale(im, winStride=(4, 4), padding=(8, 8), scale=1.02)
        print(rects, weights)
        return rects, weights
        # for i in range(len(weights)):
        #     if weights[i] > 0.3:
        #         (x, y, w, h) = rects[i]
        #         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # cv2.imwrite('P2.jpg', image)
if __name__ == "__main__":
    image = cv2.imread("frame.jpg")
    im = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    im[0:900,:] = 0
    im[1100:,:] = 0

    im[:,0:1200] = 0
    im[:,2500:] = 0

    ykernel = np.zeros((3, 3), dtype=np.float32)
    ykernel[:,0] = -1
    ykernel[:,1] = 0
    ykernel[:,2] = 1

    convolved_imagey = cv2.filter2D(im, -1, ykernel)

    xkernel = np.zeros((3, 3), dtype=np.float32)
    xkernel[0,:] = -1
    xkernel[1,:] = 0
    xkernel[2,:] = 1

    convolved_imagex = cv2.filter2D(im, -1, xkernel)

    result = cv2.bitwise_or(convolved_imagey, convolved_imagex)

    ret, binary = cv2.threshold(result, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 拟合每个轮廓的最小包围圆
    for contour in contours:
        # 获取最小包围圆的圆心和半径
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)

        cv2.circle(result, center, radius*5, (255, 0, 0), 2)

    cv2.imshow('Original Image', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()






