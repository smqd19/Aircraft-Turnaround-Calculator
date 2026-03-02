import cv2

def draw_timestamp(frame, timestamp_ms):
    """Helper to draw current video time on the frame."""
    seconds = int((timestamp_ms / 1000) % 60)
    minutes = int((timestamp_ms / (1000 * 60)) % 60)
    time_str = f"Time: {minutes:02d}:{seconds:02d}"
    cv2.putText(frame, time_str, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame
