import cv2
import numpy as np

#720p 해상도의 빈 스케치북 (검정 바탕)
height, width = 720, 1280
sketchbook = np.zeros((height, width, 3), dtype=np.uint8) # 초기값은 모두 0, 즉 검정색

window_name = "스케치북" # 윈도우 이름 설정
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL) # OpenCV 창 생성

draw_points = []
def draw_circle(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"clicked:x={x}, y={y}")
        draw_points.append((x,y))


# points = np.array([
#     [250, 50],   # 위
#     [300, 180],
#     [450, 180],
#     [330, 280],
#     [380, 430],
#     [250, 340],
#     [120, 430],
#     [170, 280],
#     [50, 180],
#     [200, 180]
# ], dtype=np.int32)


# points = points.reshape((-1, 1, 2))

cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", draw_circle)
#검정색으로 화면 보여주기
while True:
    cv2.setWindowTitle(window_name, "검정색 스케치북")
    cv2.imshow(window_name, sketchbook)

    #cv2.polylines(sketchbook, [points], isClosed=True, color=(255, 0, 0), thickness=5)
    
    key = cv2.waitKey(1)
    if key & 0xFF == ord("q"):
        break

# #흰색으로 화면 전체 칠하기
# sketchbook[:] = (255, 255, 255) # BGR 순서
# cv2.imshow(window_name, sketchbook)
# cv2.setWindowTitle(window_name, "흰색 스케치북")
# cv2.waitKey(1000) # 1초 대기

# #빨간색으로 화면 전체 칠하기
# sketchbook[:] = (0, 0, 255) # 빨간색 (OpenCV는 BGR)
# cv2.imshow(window_name, sketchbook)
# cv2.setWindowTitle(window_name, "빨간색 스케치북")
# cv2.waitKey(1000)

#종료
cv2.destroyAllWindows()