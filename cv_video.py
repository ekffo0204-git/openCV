import numpy as np
import cv2

cap = cv2.VideoCapture("ronaldinho.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
if fps==0:
    fps = 30

delay = int(1000/fps)
count = 0
while cap.isOpened():
    ret, frame = cap.read()

    if ret is False:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
        print("Can not receive frame (stream end?). Exiting...")
        break

    cv2.imshow("Frame", frame)

    resized = cv2.resize(frame, (300,300))
    cv2.imshow("resized Frame", resized)

    # 키 입력 기다리는 시간
    key = cv2.waitKey(delay)
    if key & 0xFF == ord("q"):
        break
    elif key == ord("c"):
        filename = f"{count:03d}.jpg"
        cv2.imwrite(filename, frame)
        print("Successfully saved")
        count+=1


cap.release()
