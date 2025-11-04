### 사진 캡처
import cv2

# 카메라 객체 생성
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise SystemExit("카메라를 열 수 없습니다.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)
    if key == ord('c'):  # 'c' 키로 사진 저장
        cv2.imwrite("capture.jpg", frame)
        print("사진 저장 완료!")
    elif key == ord('q'):  # 'q' 키로 종료
        break

cap.release()
cv2.destroyAllWindows()
