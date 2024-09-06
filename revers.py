import streamlit as st
import cv2
import tempfile
import os


# Function to reverse the video
def reverse_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        st.error("Error opening video file")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    frames = []

    # Read and store each frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    # Write frames in reverse order to output video
    for frame in reversed(frames):
        out.write(frame)

    out.release()


# Streamlit app interface
st.title("Video Reverser App")
st.write("Upload a video and reverse it!")

# Video file upload
uploaded_file = st.file_uploader("Choose a video...", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Save the uploaded video to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    temp_file.write(uploaded_file.read())
    input_video_path = temp_file.name

    st.video(input_video_path)  # Display the uploaded video

    # Button to reverse the video
    if st.button("Reverse Video"):
        output_video_path = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4').name

        # Call the reverse_video function
        reverse_video(input_video_path, output_video_path)

        # Show the reversed video
        st.write("Reversed video:")
        st.video(output_video_path)

        # Provide a download link for the reversed video
        with open(output_video_path, "rb") as file:
            btn = st.download_button(
                label="Download Reversed Video",
                data=file,
                file_name="reversed_video.mp4",
                mime="video/mp4"
            )
