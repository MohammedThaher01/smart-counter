from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

# use your webcam — 0 is the built-in camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    annotated = results[0].plot()

    # count detected objects by class
    counts = {}
    for box in results[0].boxes:
        class_id = int(box.cls)
        class_name = model.names[class_id]
        counts[class_name] = counts.get(class_name, 0) + 1

    # draw counts on frame
    y = 30
    for name, count in counts.items():
        cv2.putText(annotated, f"{name}: {count}", (10, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        y += 30

    cv2.imshow("Smart Counter", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()