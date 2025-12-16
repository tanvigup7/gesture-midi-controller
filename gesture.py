import cv2
import mediapipe as mp

class GestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7,
                                         min_tracking_confidence=0.7,
                                         max_num_hands=2)
        self.mp_draw = mp.solutions.drawing_utils
        self.prev_gesture = None
        self.cooldown = 0

    def detect_gesture(self, frame):
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)

        gesture = None
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                # simple open palm / fist / finger count logic
                fingers = []
                tip_ids = [8, 12, 16, 20]
                mid_ids = [6, 10, 14, 18]
                for i in range(4):
                    tip_y = hand_landmarks.landmark[tip_ids[i]].y
                    mid_y = hand_landmarks.landmark[mid_ids[i]].y
                    fingers.append(1 if tip_y < mid_y else 0)
                if fingers == [0,0,0,0]:
                    gesture = "fist"
                elif fingers == [1,1,1,1]:
                    gesture = "open_palm"
                elif fingers == [1,0,0,0]:
                    gesture = "1 finger"
                elif fingers == [1,1,0,0]:
                    gesture = "2 fingers"
                elif fingers == [1,1,1,0]:
                    gesture = "3 fingers"

        return gesture, frame
