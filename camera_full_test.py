import cv2

# 얼굴 인식용 분류기 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# 카메라 연결
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise SystemExit("카메라를 열 수 없습니다.")

print("✅ 카메라 실행 중... (c: 캡처, q: 종료)")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # 얼굴 감지
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    # 얼굴 영역에 사각형 표시
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # 화면 출력
    cv2.imshow("Camera (Press 'c' to capture, 'q' to quit)", frame)

    key = cv2.waitKey(1)
    if key == ord('c'):
        cv2.imwrite("capture.jpg", frame)
        print("📸 capture.jpg 저장 완료")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
