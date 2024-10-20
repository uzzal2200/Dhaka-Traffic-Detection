import streamlit as st
import torch
from PIL import Image
from pathlib import Path
import os

# Load the YOLOv5 model once, when the app starts
@st.cache_resource
def load_model():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='saved_models/Best_Accuracy_Dhaka_AI_Yolov5l_By_Autobot_BS_8.pt')
    return model

def run_inference(image_path, model):
    results = model(image_path)
    return results

def upload_and_predict():
    st.title("Dhaka Traffic Detection System")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

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

            # Display image with bounding boxes
            results_img = Image.fromarray(results.render()[0])  # Render and get image with bounding boxes
            st.image(results_img, caption='Detected Traffic Objects', use_column_width=True)

if __name__ == "__main__":
    upload_and_predict()
