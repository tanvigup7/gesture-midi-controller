import cv2
from gesture import GestureDetector

# start video + gesture
cap = cv2.VideoCapture(0)
detector = GestureDetector()

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gesture, frame = detector.detect_gesture(frame)

        if gesture:
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

            cv2.putText(frame, gesture, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0),3)

        cv2.imshow("Gesture FX Looper", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
