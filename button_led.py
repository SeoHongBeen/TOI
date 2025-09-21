import board
import digitalio
import time

# LED: GP15
led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

# 버튼: GP14 (풀다운)
button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

while True:
    if button.value:   # 버튼 눌렸을 때 (HIGH)
        led.value = True
        print("Button Pressed! → LED ON")
    else:              # 버튼 안 눌렸을 때 (LOW)
        led.value = False
        print("Button Released → LED OFF")
    
    time.sleep(0.2)  # 너무 빠른 출력 방지
