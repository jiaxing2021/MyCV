import os
import cv2



class imageReader():
    def __init__(self, path):
        self.path = path
    def Imageread(self):
        file_names = os.listdir(self.path)
        images = []

        for file_name in file_names:
            file_path = os.path.join(self.path, file_name)
            if file_name.endswith(('.jpg', '.jpeg', '.png')):
                image = cv2.imread(file_path)
                if image is not None:
                    images.append(image)
                else:
                    print(f"Failed to load image: {file_path}")

        return images


if __name__ == "__main__":
    folder_path = './path'
    reader = imageReader(folder_path)
    imageSet = reader.Imageread()
    print(f"Total images loaded: {len(imageSet)}")


