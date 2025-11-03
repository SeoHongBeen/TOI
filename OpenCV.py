import cv2

# ① 이미지 읽기
img = cv2.imread("jang.jpeg")              # 네 이미지 파일명
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ② 노이즈 완화
blur = cv2.GaussianBlur(gray, (5,5), 1.2)

# ③ 엣지(Canny)
edges = cv2.Canny(blur, 80, 160)            # (low, high) 임계값. 환경에 맞게 조절

# ④ 컨투어 추출
cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# ⑤ 컨투어 그리기
out = img.copy()
cv2.drawContours(out, cnts, -1, (0,255,0), 2)

# ⑥ 결과 보기/저장
cv2.imshow("edges", edges)
cv2.imshow("contours", out)
cv2.imwrite("edges.png", edges)
cv2.imwrite("contours.png", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
