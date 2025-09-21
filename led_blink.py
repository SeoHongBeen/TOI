import RPi.GPIO as GPIO //센서 제어용 GPIO 모듈/대기시간 용 tiome 모듈 로드
import time //반복문으로 gpio 18번 핀에 false 데이터 출력 후 2초 대기

GPIO.setmode(GPIO.BCM) //핀 번호를 BCM 번호로 참조
GPIO.setup(18, GPIO.OUT) //18번 핀을 출력으로 설정

while True:
    try:
        GPIO.output(18, False) //GPIO로 FALSE를 18번 핀에 출력
        print("OFF") //LED의 상태를 표기(OFF)
        time.sleep(2) //2초동안 중지되도록 구성
	
	 GPIO.output(18, True)    # LED 켜기
        print("ON") //LED 상태 ON 으로 표기
        time.sleep(2)

    except KeyboardInterrupt: //키보드 인터럽트 발생 시 (컨트롤+C)
        pass //모든 코드 패스
        print("Exit with ^C. Goodbye!") //코드 중지됨을 선언
        GPIO.cleanup()           # 모든 GPIO 핀 초기화
        exit() #코드 종료
