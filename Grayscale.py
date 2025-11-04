import cv2

# 이미지 파일 불러오기
img = cv2.imread("jang.jpeg")  # TOI 폴더 안 이미지 혹은 방금 저장된 우리 사 

# 컬러 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 결과 출력
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)

# 저장 (옵션)
cv2.imwrite("gray_result.jpg", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
