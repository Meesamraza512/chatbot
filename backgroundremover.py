'''from rembg import remove
from PIL import Image


def remove_background(input_path, output_path):
    # Open the image file
    input_image = Image.open(input_path)

    # Remove the background
    output_image = remove(input_image)

    # Save the result
    output_image.save(output_path)

    print(f"Background removed and saved to {output_path}")


# Run the function
remove_background('meesam.jpg', 'output_image.png')

'''







import streamlit as st
from rembg import remove
from PIL import Image
import io

def main():
    st.title("Background Remover")

    # Upload image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load the uploaded image
        image = Image.open(uploaded_file)

        # Remove background
        image_no_bg = remove(image)

        # Display the image with background removed
        st.image(image_no_bg, use_column_width=True)

        # Convert image to bytes for download
        buffer = io.BytesIO()
        image_no_bg.save(buffer, format="PNG")
        buffer.seek(0)

        # Download button
        st.download_button(
            label="Download Image Without Background",
            data=buffer,
            file_name="no_background_image.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()








