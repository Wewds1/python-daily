import cv2
import mediapipe as mp
import numpy as np


# === HAND TRACKING SETUP ===
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils


def detect_hands(frame, hands):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return hands.process(rgb_frame)


def fingers_up(hand_landmarks):
    tip_ids = [4, 8, 12, 16, 20]  
    fingers = []

    if hand_landmarks.landmark[tip_ids[1]].y < hand_landmarks.landmark[tip_ids[1] - 2].y:
        fingers.append(1)
    else:
        fingers.append(0)

    if hand_landmarks.landmark[tip_ids[2]].y < hand_landmarks.landmark[tip_ids[2] - 2].y:
        fingers.append(1)
    else:
        fingers.append(0)

    if hand_landmarks.landmark[tip_ids[3]].y < hand_landmarks.landmark[tip_ids[3] - 2].y:
        fingers.append(1)
    else:
        fingers.append(0)

    if hand_landmarks.landmark[tip_ids[4]].y < hand_landmarks.landmark[tip_ids[4] - 2].y:
        fingers.append(1)
    else:
        fingers.append(0)

    return fingers  


def process_frame(frame, hands, canvas):
    """Process frame, draw or erase depending on gesture."""
    frame = cv2.flip(frame, 1)
    result = detect_hands(frame, hands)
    h, w, _ = frame.shape

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers = fingers_up(hand_landmarks)

            cx, cy = int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h)

            if fingers == [1, 0, 0, 0]:
                cv2.circle(frame, (cx, cy), 2, (0, 0, 255), 1)
                cv2.circle(canvas, (cx, cy), 2, (0, 0, 255), 1)

            elif fingers == [0, 0, 0, 0]:
                cv2.circle(frame, (cx, cy), 40, (0, 255, 0), 2)
                cv2.circle(canvas, (cx, cy), 40, (0, 0, 0), -1) 

    gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, inv = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY_INV)
    inv = cv2.cvtColor(inv, cv2.COLOR_GRAY2BGR)
    frame = cv2.bitwise_and(frame, inv)
    frame = cv2.bitwise_or(frame, canvas)

    return frame, canvas


def main():
    cap = cv2.VideoCapture(0)
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)
    canvas = np.zeros((480, 640, 3), np.uint8)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame, canvas = process_frame(frame, hands, canvas)
        cv2.imshow("Finger Painter", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
