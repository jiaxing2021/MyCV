



import cv2
import numpy as np

class P2Detector():
    def __init__(self, image):
        self.image = image
    def detection(self):
        im = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        im[0:900,:] = 0
        im[1050:,:] = 0

        im[:,0:1400] = 0
        im[:,2500:] = 0
        cv2.imwrite('im.jpg', im)

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
        # print(rects, weights)

        maxWeight = 0

        # try:
        for i in range(weights.shape[0]):
            if maxWeight < weights[i]:
                maxWeight = weights[i]
                rect = rects[i]

        return rect, maxWeight
        # except:
        #     return rects, weights
        # for i in range(len(weights)):
        #     if weights[i] > 0.3:
        #         (x, y, w, h) = rects[i]
        #         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # cv2.imwrite('P2.jpg', image)
if __name__ == "__main__":
    image = cv2.imread("frame.jpg")

    P2 = P2Detector(image)
    rect, weight = P2.detection()
    # for i in range(len(weights)):
    #         if weights[i] > 0.3:
    (x, y, w, h) = rect
    P2text = "P2"
    center = (int(x + w/2), int(y + h/2))
    cv2.putText(image, P2text, center, cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 255, 0), 3)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imwrite('P2.jpg', image)


