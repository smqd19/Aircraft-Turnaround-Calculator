import cv2
from detector import TATDetector
from tracker import EventTracker
from utils import draw_annotations

def run_pipeline(video_path):
    cap = cv2.VideoCapture(video_path)
    detector = TATDetector()
    tracker = EventTracker()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret: break

        timestamp = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
        
        # 1. Detection
        plane_box = detector.detect_aircraft(frame)
        equip_boxes = detector.detect_ground_equipment(frame)

        # 2. Tracking & Logic
        tracker.update(plane_box, equip_boxes, timestamp)

        # 3. Visualization (Optional)
        # annotated_frame = draw_annotations(frame, plane_box, equip_boxes)
        # cv2.imshow('TAT Analysis', annotated_frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): break

    cap.release()
    print("Processing Complete. Generating Report...")
    print(tracker.get_summary())

if __name__ == "__main__":
    run_pipeline("data/Airplane_Video.mp4")
