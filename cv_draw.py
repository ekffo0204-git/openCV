import cv2

points = []

def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"clicked:x={x}, y={y}")
        points.append((x,y))

cap = cv2.VideoCapture(0)

topLeft = (50,50)
bottomRight = (300,300)

cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", draw_circle)

while (cap.isOpened()):
    ret,frame = cap.read()

    cv2.line(frame,topLeft, bottomRight, (0,255,0), 5)

    cv2.rectangle(frame, [pt+30 for pt in topLeft], [pt-30 for pt in bottomRight], (0,0,255), 5)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'me', [pt+80 for pt in topLeft], font, 2, (0,255,255), 10)

    for x,y in points:
        cv2.circle(frame, (x,y), 20, (255,0,0), 5)
    cv2.imshow("Camera", frame)

    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
