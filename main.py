import cv2
import time
from gesture import GestureDetector
from midi import play_note

# Gesture → MIDI note mapping
GESTURE_TO_NOTE = {
    "1 finger": 58,
    "2 fingers": 56,
    "3 fingers": 54,
    "open_palm": 51,
    "fist": 48
}

# start video + gesture
cap = cv2.VideoCapture(0)
detector = GestureDetector()

last_gesture = None
last_note_time = 0
NOTE_COOLDOWN = 0.8  # seconds


try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gesture, frame = detector.detect_gesture(frame)
        current_time = time.time()

        if gesture and gesture in GESTURE_TO_NOTE:
            # prevent retrigger spam
            if gesture != last_gesture or (current_time - last_note_time) > NOTE_COOLDOWN:
                note = GESTURE_TO_NOTE[gesture]
                play_note(note)
                print(f"{gesture} → {note}")

                last_gesture = gesture
                last_note_time = current_time
                '''
                 if gesture == "1 finger":
                print("1 finger")
            elif gesture == "2 fingers":
                print("2 fingers")
            elif gesture == "fist":
                print("fist")
            elif gesture == "open_palm":
                print("palm")
            elif gesture == "3 fingers":
                print("3 fingers")
                '''
           

            cv2.putText(
                frame,
                gesture,
                (10,50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0,255,0),
                3
            )

        cv2.imshow("Gesture FX Looper", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
