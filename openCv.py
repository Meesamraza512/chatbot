'''import cv2

# Initialize the webcam
cap = cv2.VideoCapture(1)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Loop to continuously get frames
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly, ret is True
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting...")
        break

    # Display the resulting frame
    cv2.imshow('Webcam Feed', frame)

    # Press 'q' on the keyboard to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
'''








import cv2
from fer import FER

cap = cv2.VideoCapture(1)
face_detector = FER()

colors = {'happy': (0, 255, 0), 'sad': (0, 0, 255), 'neutral': (255, 255, 255)}

while True:
    ret, frame = cap.read()
    if not ret: break
    result = face_detector.detect_emotions(frame)
    if result:
        for face in result:
            emotions = face['emotions']
            emotion = max(emotions, key=emotions.get)
            color = colors.get(emotion, (255, 255, 255))
            x, y, w, h = face['box']
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, emotion.capitalize(), (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    cv2.imshow('Emotion Detection', frame)
    if cv2.waitKey(1) == 27: break

cap.release()
cv2.destroyAllWindows()
