import cv2
import os
import numpy as np
import streamlit as st
import openai
from config import OPENAI_API_KEY

# Set your OpenAI API key
openai.api_key = OPENAI_API_KEY

if openai.api_key is None:
    st.error("OpenAI API key is missing. Set the OPENAI_API_KEY environment variable.")
    st.stop()
# Define criteria weights
criteria_weights = {
    'Composition': 0.1,
    'Lighting': 0.1,
    'Focus': 0.1,
    'Color': 0.1,
    'Tone': 0.1,
    'Timing': 0.1,
    'Perspective': 0.1,
    'Storytelling': 0.1,
    'Technical_Quality': 0.1,
    'Originality': 0.1,
    'Post_Processing': 0.1,
}


def calculate_score(img):
    # Extract features (for demonstration purposes, using average color intensity)
    average_intensity = np.mean(img)

    

    # Calculate the score based on the features and weights
    score = (
        criteria_weights['Composition'] * average_intensity +
        criteria_weights['Lighting'] * average_intensity +
        criteria_weights['Focus'] * average_intensity +
        criteria_weights['Color'] * average_intensity +
        criteria_weights['Tone'] * average_intensity +
        criteria_weights['Timing'] * average_intensity +
        criteria_weights['Perspective'] * average_intensity +
        criteria_weights['Storytelling'] * average_intensity +
        criteria_weights['Technical_Quality'] * average_intensity +
        criteria_weights['Originality'] * average_intensity +
        criteria_weights['Post_Processing'] * average_intensity
    )

    return score

def generate_text(image_name, criterion, score):
    prompt = f"Image '{image_name}' received a score of {score:.2f} for '{criterion}' based on the image quality criteria. Provide a description:"

    # Call OpenAI GPT to generate text
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )

    return response.choices[0].text.strip()

def select_best_image(images, image_names):
    # Calculate scores for each image
    scores = {}
    for idx, (img, name) in enumerate(zip(images, image_names)):
        scores[name] = calculate_score(img)

    # Select the image with the highest score
    best_image = max(scores, key=scores.get)
    best_score = scores[best_image]

    # Display the best image with a styled success box
    st.success(f"🏆 The best image is {best_image} with a score of {best_score:.2f}")

    # Generate text descriptions for each criterion and display below the image previews
    st.subheader("Criterion Descriptions:")
    for criterion in criteria_weights.keys():
        description = generate_text(best_image, criterion, scores[best_image])
        st.write(f"**{criterion}:** {description}")

# Streamlit UI
def main():
    st.title("Image Quality Assessment")

    uploaded_files = st.file_uploader("Upload multiple images", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if not uploaded_files or len(uploaded_files) < 2:
        st.warning("Please upload at least two images for assessment.")
        st.stop()

    # Read and process uploaded images
    images = [cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR) for file in uploaded_files]
    image_names = [file.name for file in uploaded_files]

    # Display uploaded images with styled columns
    st.subheader("Uploaded Images:")
    columns = st.columns(2)
    for i in range(0, len(images), 2):
        with columns[0]:
            st.image(images[i], caption=image_names[i], use_column_width=True)
        if i + 1 < len(images):
            with columns[1]:
                st.image(images[i + 1], caption=image_names[i + 1], use_column_width=True)

    # Assess image quality with a styled button
    if st.button("🚀 Assess Image Quality", key="assessment_button"):
        st.spinner("Assessing image quality...")  # Show a spinner while assessing
        select_best_image(images, image_names)

if __name__ == "__main__":
    main()