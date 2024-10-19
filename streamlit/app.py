import streamlit as st
import torch
from PIL import Image
from pathlib import Path
import os

# Load the YOLOv5 model once, when the app starts
@st.cache(allow_output_mutation=True)
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='saved_models/yolov5_weights.pt')
    return model

def run_inference(image_path, model):
    results = model(image_path)
    return results

def upload_and_predict():
    st.title("Dhaka Traffic Detection System")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Save uploaded image to disk
        img_path = os.path.join("uploads", uploaded_file.name)
        with open(img_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Display uploaded image
        image = Image.open(img_path)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Load YOLOv5 model
        model = load_model()

        # Predict when button is clicked
        if st.button("Predict"):
            results = run_inference(img_path, model)
            st.write("Predictions:")
            results.print()  # Print results to console
            st.table(results.pandas().xyxy[0])  # Display predictions as table

if __name__ == "__main__":
    upload_and_predict()
