# gesture_picam2.py
import cv2
import mediapipe as mp
from picamera2 import Picamera2

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def get_finger_status(lm, handedness: str):
    TIPS = [4, 8, 12, 16, 20]
    PIPS = [3, 6, 10, 14, 18]
    ext = [False] * 5

    # 엄지
    tip = lm[TIPS[0]]
    ip  = lm[PIPS[0]]
    if handedness == "Right":
        ext[0] = tip.x < ip.x
    else:
        ext[0] = tip.x > ip.x

    # 검지 ~ 새끼
    for idx in range(1, 5):
        tip_y = lm[TIPS[idx]].y
        pip_y = lm[PIPS[idx]].y
        if tip_y < pip_y:
            ext[idx] = True

    return ext

def classify_gesture(ext):
    t, i, m, r, p = ext

    if all(ext):
        return "OPEN_PALM"   # 손바닥
    if not any(ext):
        return "FIST"        # 주먹
    if (not t and i and not m and not r and not p):
        return "POINT"       # 검지만
    if (not t and i and m and not r and not p):
        return "V_SIGN"      # V자
    return "UNKNOWN"

def main():
    picam2 = Picamera2()
    config = picam2.preview_configuration
    config.main.size = (640, 480)
    config.main.format = "RGB888"   # MediaPipe용 RGB
    picam2.configure("preview")
    picam2.start()

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.5
    ) as hands:
        while True:
            # 1) RGB 프레임 캡처
            frame_rgb = picam2.capture_array()
            frame_rgb = cv2.flip(frame_rgb, 1)

            # 2) MediaPipe 처리
            result = hands.process(frame_rgb)

            # 3) 출력용 BGR
            frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

            gesture_name = "NONE"

            if result.multi_hand_landmarks:
                for hand_lm, handed in zip(
                    result.multi_hand_landmarks,
                    result.multi_handedness
                ):
                    label = handed.classification[0].label  # Right/Left
                    ext = get_finger_status(hand_lm.landmark, label)
                    gesture_name = classify_gesture(ext)

                    mp_drawing.draw_landmarks(
                        frame_bgr, hand_lm, mp_hands.HAND_CONNECTIONS
                    )

            cv2.putText(frame_bgr, f"Gesture: {gesture_name}",
                        (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

            cv2.imshow("Gesture - PiCamera2", frame_bgr)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC
                break

    picam2.stop()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
