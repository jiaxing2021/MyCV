import cv2
import os


video_path = 'input.mp4'
output_folder = 'frames'
frame_interval = 30  

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Frames per second: {fps}")

frame_number = 0

while True:

    ret, frame = cap.read()
    if not ret:
        break

   

    if frame_number % frame_interval == 0:
        image_path = os.path.join(output_folder, f'frame_{frame_number}.jpg')
        cv2.imwrite(image_path, frame)
        print(f"Image saved as {image_path}")
    
    frame_number = frame_number + 1

    


cap.release()
print("Video processing complete.")
