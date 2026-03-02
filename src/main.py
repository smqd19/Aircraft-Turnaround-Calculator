import cv2
from detector import TATDetector
from tracker import EventTracker

def main():
    video_path = "data/Airplane_Video.mp4"
    cap = cv2.VideoCapture(video_path)
    
    detector = TATDetector()
    tracker = EventTracker()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
            
        # Implement logic here
        detections = detector.detect(frame)
        events = tracker.update(detections, cap.get(cv2.CAP_PROP_POS_MSEC))

    # Print final report
    tracker.generate_report()

if __name__ == "__main__":
    main()
