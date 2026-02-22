import cv2
import time
import numpy as np
from ultralytics import YOLO

# 1. Load the Medium Model (Better accuracy than Nano, faster than Large)
# This will auto-download 'yolo11m.pt' on first run
model = YOLO("yolo11m.pt") 

# 2. Setup Webcam with High-Def capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# 3. Optimization: Fixed Color Palette for 80 Objects
np.random.seed(42)
colors = np.random.randint(0, 255, size=(80, 3), dtype=np.uint8)

while cap.isOpened():
    start_time = time.time()
    success, frame = cap.read()
    if not success: break

    # --- STEP 1: PRECISE TRACKING ENGINE ---
    # imgsz=640: Optimization! AI 'thinks' at 640px while we 'see' at 720p. 
    # This keeps FPS high without losing detection quality.
    results = model.track(frame, persist=True, conf=0.5, iou=0.6, 
                          imgsz=640, tracker="bytetrack.yaml", verbose=False)[0]

    # --- STEP 2: PROFESSIONAL UI PANEL ---
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, 0), (300, 720), (10, 10, 10), -1)
    cv2.addWeighted(overlay, 0.75, frame, 0.25, 0, frame)
    
    cv2.putText(frame, "ULTIMATE VISION ENGINE", (20, 40), 0, 0.7, (0, 255, 0), 2)
    cv2.line(frame, (20, 55), (260, 55), (255, 255, 255), 1)

    summary = {}

    # --- STEP 3: RENDERING DETECTIONS ---
    if results.boxes.id is not None:
        boxes = results.boxes.xyxy.int().cpu().tolist()
        ids = results.boxes.id.int().cpu().tolist()
        clss = results.boxes.cls.int().cpu().tolist()

        for box, obj_id, cls in zip(boxes, ids, clss):
            x1, y1, x2, y2 = box
            name = model.names[cls].upper()
            summary[name] = summary.get(name, 0) + 1
            color = [int(c) for c in colors[cls]]

            # Dynamic Box corners (High-Tech Design)
            length = 25
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 1) 
            # Drawing the 4 corners thicker for a 'Scanner' effect
            corners = [(x1,y1), (x2,y1), (x1,y2), (x2,y2)]
            for i, (cx, cy) in enumerate(corners):
                # Logic to draw lines extending from corners
                dx = length if i % 2 == 0 else -length
                dy = length if i < 2 else -length
                cv2.line(frame, (cx, cy), (cx + dx, cy), color, 4)
                cv2.line(frame, (cx, cy), (cx, cy + dy), color, 4)

            cv2.putText(frame, f"{name} ID:{obj_id}", (x1, y1 - 10), 0, 0.6, color, 2)

    # --- STEP 4: ANALYTICS DASHBOARD ---
    fps = 1 / (time.time() - start_time)
    cv2.putText(frame, f"INFERENCE: {int(fps)} FPS", (20, 85), 0, 0.5, (200, 200, 200), 1)
    
    y_pos = 140
    cv2.putText(frame, "LIVE SCAN RESULTS:", (20, 120), 0, 0.5, (0, 255, 255), 1)
    for name, count in summary.items():
        cv2.putText(frame, f"> {name}: {count}", (30, y_pos), 0, 0.6, (255, 255, 255), 1)
        y_pos += 30

    cv2.imshow("Professional Object Detection & Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()