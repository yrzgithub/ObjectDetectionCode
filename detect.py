from ultralytics import YOLO 
import cv2
from keyboard import is_pressed



model = YOLO("yolov8n.pt",task="predict",verbose=False)

video = cv2.VideoCapture(0)

while not is_pressed("esc"):
    _,img = video.read()
    results = model(img)

    for result in results:
        boxs = result.boxes
        # x1,y1,x2,y2 = map(int,boxs)

    cv2.imshow("frame",img)
    cv2.waitKey(100)

video.release()
cv2.destroyAllWindows()