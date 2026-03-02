import cv2
import matplotlib.pyplot as plt

# Load the video
video_path = "../data/Airplane_Video.mp4"
cap = cv2.VideoCapture(video_path)

# Get Metadata
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
duration_sec = total_frames / fps

print(f"FPS: {fps}")
print(f"Total Duration: {duration_sec:.2f} seconds")

# Grab one frame at the 5-second mark
cap.set(cv2.CAP_PROP_POS_MSEC, 5000) 
ret, frame = cap.read()

if ret:
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(frame_rgb)
    plt.title("Snapshot at 00:05")
    plt.show()

cap.release()
