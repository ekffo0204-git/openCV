import cv2


frame = None
cap = cv2.VideoCapture(0)
count = 0

def capture_screen(event, x, y, flags, param):
    global frame, count
    filename = f"{count:03d}.jpg"
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.imwrite(filename, frame)

    count+=1

cv2.namedWindow("Capture")
cv2.setMouseCallback("Capture", capture_screen)


while cap.isOpened():
    ret, frame = cap.read()

    if ret is False:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue
        print("Can not receive frame (stream end?). Exiting...")
        break

    cv2.imshow("Capture", frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break

cap.release()