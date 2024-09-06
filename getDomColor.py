import cv2
import numpy as np

# get dominant color histogram
def getDomColor(image):
    image = image[40:80,40:80,:]
    hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    dominant_color = np.unravel_index(np.argmax(hist), hist.shape)
    dominant_color = [int(c * 32) for c in dominant_color]
    return dominant_color


if __name__ == "__main__":
    image = cv2.imread('image.png')

    dominant_color = getDomColor(image)
    print(f'Dominant Color: {dominant_color}')

