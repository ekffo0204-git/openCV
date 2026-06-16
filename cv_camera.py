import cv2

cap = cv2.VideoCapture(0)

w = 640
h = 480

cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter("output.mp4", fourcc, 30.0, (w,h))

while (cap.isOpened):
    ret, frame = cap.read()
    if ret is False:
        print("Can not receive frame (stream end?). Exiting ...")
        break

    cv2.imshow("Camera", frame)
    writer.write(frame)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break

writer.release()

cap.release()
cv2.destroyAllWindows()
