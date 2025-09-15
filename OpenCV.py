#카메라 모듈(라즈베리파이 전용 카메라 or USB 웹캠) -> 트랙상  11.05 - 11.12 예정

import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
