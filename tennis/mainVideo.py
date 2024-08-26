import cv2
import numpy as np

from frameDetector import detector

input_video_path = 'input.mp4'

cap = cv2.VideoCapture(input_video_path)

frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MPEG-4 编码格式
output_video_path = 'output_video.mp4'
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

print(f"Processing, please wait ......")

i = 0
while True:
    ret, frame = cap.read()
    result = frame.copy()

    if not ret:
        break

    videoDetector = detector(frame, result)
    videoDetector.detection()

    out.write(result)

    i = i + 1
    num = i/frame_count
    percentage = round(num, 4) * 100
    print(f'{percentage}%')
    
cap.release()
out.release()

print(f"Processed video saved as {output_video_path}")
