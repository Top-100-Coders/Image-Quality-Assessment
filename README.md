# Image-Quality-Assessment


This project is a Streamlit web application for assessing and ranking the quality of uploaded images based on predefined criteria. The app utilizes OpenAI's GPT (Generative Pre-trained Transformer) to generate text descriptions for each image criterion, providing detailed insights into the strengths and weaknesses of the images.

try it out: https://image-quality-assessment1.onrender.com

## Features

* Multi-Image Upload: Users can upload multiple images in common formats (jpg, jpeg, png) for simultaneous assessment.
* Image Display: Uploaded images are displayed in a visually appealing layout with image names and captions.
* Quality Assessment: The app calculates image quality scores based on predefined criteria and weights.
* Best Image Selection: The app identifies and displays the image with the highest quality score, along with a styled success box.
* Criterion Descriptions: For transparency, the app generates text descriptions for each criterion of the best image using OpenAI GPT.
* Dynamic Weighting: Users can dynamically adjust weights for each criterion to customize the assessment.

## Installation

* Clone the repository.
* Install dependencies: pip install -r requirements.txt
* Set up your OpenAI API key in the environment variables or directly in the script.
* Run the app: streamlit run app.py

## Usage

* Upload at least two images.
* Click the "Assess Image Quality" button to view the best image and detailed criterion descriptions.
* Customize the assessment by adjusting criterion weights.

## Technologies Used

* Python
* OpenAI GPT
* Streamlit
* OpenCV

## Contributors

* [AshinSMathew](https://github.com/AshinSMathew)
* [abinrd](https://github.com/abinrd)
