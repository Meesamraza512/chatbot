'''import moviepy.editor
from tkinter.filedialog import *
vid = askopenfilename()
video= moviepy.editor.VideoFileClip(vid)

aud=video.audio
aud.write_audiofile("demo1.mp3")
print("end")'''

'''
import streamlit as st
import moviepy.editor as mp

# Streamlit app title
st.title("Video to Audio Converter")

# Upload video file using Streamlit's file uploader
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Display a message indicating the upload is in progress
    st.info("Processing the video...")

    # Save the uploaded file temporarily
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.read())

    # Load the video file using MoviePy
    video = mp.VideoFileClip("temp_video.mp4")

    # Extract audio from the video
    audio = video.audio

    # Save the audio as an MP3 file
    audio.write_audiofile("demo1.mp3")

    # Provide a download link for the audio file
    st.success("Audio extraction complete!")
    st.audio("demo1.mp3", format="audio/mp3")
    st.download_button(label="Download Audio", data=open("demo1.mp3", "rb"), file_name="demo1.mp3", mime="audio/mp3")
    st.write("End")



from urllib.parse import quote as url_quote

import streamlit as st
import pywhatkit as pyw

# Streamlit app title
st.title("Send WhatsApp Message via Python")

# Input fields for phone number, message, and time
phone_number = st.text_input("Enter phone number (with country code)", "+92")
message = st.text_input("Enter your message", " ")
hour = st.number_input("Hour (24-hour format)", min_value=0, max_value=23, value=12)
minute = st.number_input("Minute", min_value=0, max_value=59, value=52)

# Button to send the message
if st.button("Send Message"):
    if phone_number and message:
        try:
            # Send the WhatsApp message using pywhatkit
            pyw.sendwhatmsg(phone_number, message, hour, minute)
            st.success("Message sent successfully!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please provide a valid phone number and message.")

'''

import streamlit as st
import moviepy.editor as mp
import pywhatkit as pyw
from urllib.parse import quote as url_quote

# Streamlit app title
st.title("Utility App")

# Create tabs
tab1, tab2 = st.tabs(["Video to Audio Converter", "Send WhatsApp Message"])

# Video to Audio Converter tab
with tab1:
    st.header("Video to Audio Converter")

    # Upload video file using Streamlit's file uploader
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:
        # Display a message indicating the upload is in progress
        st.info("Processing the video...")

        # Save the uploaded file temporarily
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.read())

        # Load the video file using MoviePy
        video = mp.VideoFileClip("temp_video.mp4")

        # Extract audio from the video
        audio = video.audio

        # Save the audio as an MP3 file
        audio.write_audiofile("demo1.mp3")

        # Provide a download link for the audio file
        st.success("Audio extraction complete!")
        st.audio("demo1.mp3", format="audio/mp3")
        st.download_button(label="Download Audio", data=open("demo1.mp3", "rb"), file_name="demo1.mp3",
                           mime="audio/mp3")
        st.write("End")

# Send WhatsApp Message tab
with tab2:
    st.header("Send WhatsApp Message")

    # Input fields for phone number, message, and time
    phone_number = st.text_input("Enter phone number (with country code)", "+92")
    message = st.text_input("Enter your message", " ")
    hour = st.number_input("Hour (24-hour format)", min_value=0, max_value=23, value=12)
    minute = st.number_input("Minute", min_value=0, max_value=59, value=30)

    # Button to send the message
    if st.button("Send Message"):
        if phone_number and message:
            try:
                # Send the WhatsApp message using pywhatkit
                pyw.sendwhatmsg(phone_number, message, hour, minute)
                st.success("Message sent successfully!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please provide a valid phone number and message.")
