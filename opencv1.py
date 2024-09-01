import streamlit as st
import cv2
from fer import FER


def main():
    st.title("Real-Time Emotion Detection")

    # Create a placeholder for the camera feed
    frame_placeholder = st.empty()

    # Button to open the camera
    if st.button("Open Camera", key="open_camera"):
        cap = cv2.VideoCapture(1)
        face_detector = FER()
        colors = {'happy': (0, 255, 0), 'sad': (0, 0, 255), 'neutral': (255, 255, 255)}

        # Create a stop button
        stop_button = st.button("Stop Camera", key="stop_camera")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                st.write("Failed to capture image")
                break

            result = face_detector.detect_emotions(frame)
            if result:
                for face in result:
                    emotions = face['emotions']
                    emotion = max(emotions, key=emotions.get)
                    color = colors.get(emotion, (255, 255, 255))
                    x, y, w, h = face['box']
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
                    cv2.putText(frame, emotion.capitalize(), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

            # Convert the frame to RGB (Streamlit expects RGB images)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Update the placeholder with the current frame
            frame_placeholder.image(frame_rgb, channels="RGB", use_column_width=True)

            # Check if the "Stop Camera" button is pressed
            if stop_button:
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()



