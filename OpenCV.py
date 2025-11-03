import cv2

# 이미지 파일 이름 (같은 폴더 안에 있어야 함)
IMG_PATH = "/home/kimnayeon/Pictures/22.png"

img = cv2.imread(IMG_PATH)
if img is None:
    raise SystemExit("이미지를 불러올 수 없습니다. sample.jpg 파일이 같은 폴더에 있는지 확인하세요.")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_result.jpg", gray)


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = face_cascade.detectMultiScale(gray, 1.2, 5, minSize=(60, 60))
face_img = img.copy()
for (x, y, w, h) in faces:
    cv2.rectangle(face_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imwrite("face_detect_result.jpg", face_img)

blur = cv2.GaussianBlur(gray, (5, 5), 1.2)
edges = cv2.Canny(blur, 80, 160)
cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_img = img.copy()
cv2.drawContours(contour_img, cnts, -1, (0, 255, 0), 2)
cv2.imwrite("contour_result.jpg", contour_img)

print("결과 저장 완료:")
print("- gray_result.jpg")
print("- face_detect_result.jpg")
print("- contour_result.jpg")
