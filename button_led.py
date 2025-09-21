import board
import digitalio

# LED를 GP15 핀에 연결 → 출력 모드로 설정
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

# 버튼을 GP14 핀에 연결 → 입력 모드로 설정
button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN   # 풀다운 적용 (기본값 0)

# 무한 루프: 버튼 값 = LED 값
while True:
    led.value = button.value
