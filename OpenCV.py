# file: cv_image_lab.py
import cv2

IMG = "jang.jpeg"  # 네 이미지 파일

img  = cv2.imread(IMG)
if img is None:
    raise SystemExit(f"이미지 못 찾음: {IMG}")

# 1) 그레이스케일
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("out_gray.jpg", gray)

# 2) 얼굴 감지 + 사각형
face = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
faces = face.detectMultiScale(gray, 1.2, 6, minSize=(60,60))
vis = img.copy()
for (x,y,w,h) in faces:
    cv2.rectangle(vis, (x,y), (x+w,y+h), (0,255,0), 2)
cv2.imwrite("out_face.jpg", vis)

# 3) 외곽선(엣지+컨투어)
blur  = cv2.GaussianBlur(gray, (5,5), 1.2)
edges = cv2.Canny(blur, 80, 160)
cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cont = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
cv2.drawContours(cont, cnts, -1, (0,255,0), 2)
cv2.imwrite("out_edges.jpg", edges)
cv2.imwrite("out_contours.jpg", cont)

print("저장: out_gray.jpg, out_face.jpg, out_edges.jpg, out_contours.jpg")
