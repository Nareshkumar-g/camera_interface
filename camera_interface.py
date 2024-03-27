import cv2

def capture_and_display():
    cap = cv2.VideoCapture(2)
    if not cap.isOpened():
        print("Error : Failed to open camera")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to receive frame")
            break
        cv2.imshow('Camera', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    capture_and_display()
