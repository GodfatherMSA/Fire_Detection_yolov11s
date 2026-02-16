from ultralytics import YOLO
import cv2

MODEL_PATH = 'yolo11s.pt'     
CONFIDENCE_THRESHOLD = 0.35   
IMG_SIZE = 640  
SOURCE = "fire.mp4"

model = YOLO(MODEL_PATH)

cap = cv2.VideoCapture(SOURCE)

print("Press 'q' to exit.")

while cap.isOpened():
    ret, frame = cap.read() 
    
    if not ret:
        break

    results = model.predict(
        source=frame, 
        imgsz=IMG_SIZE, 
        conf=CONFIDENCE_THRESHOLD, 
        verbose=False
    )

    results[0].names[0] = 'smoke'   
    results[0].names[1] = 'fire'

    annotated_frame = results[0].plot() 
    cv2.imshow('Fire Detect System', annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()