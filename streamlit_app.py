import streamlit as st
from PIL import Image
from pathlib import Path
import os
from src.inference import YOLOv5Inference  # Importing the class from inference.py

class TrafficDetectionApp:
    def __init__(self):
        self.model_path = 'saved_models/Best_Accuracy_Dhaka_AI_Yolov5l_By_Autobot_BS_8.pt'  # Path to model
        self.inference_engine = YOLOv5Inference(self.model_path)  # Initialize YOLOv5Inference

    def run(self):
        st.title("Dhaka Traffic Detection System")

        # File uploader
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            # Save uploaded image to disk
            img_path = os.path.join("uploads", uploaded_file.name)
            with open(img_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Display uploaded image
            image = Image.open(img_path)
            st.image(image, caption='Uploaded Image', use_column_width=True)

            # Predict when button is clicked
            if st.button("Predict"):
                # Run inference
                results = self.inference_engine.run_inference(img_path)

                # Display predictions
                st.write("Predictions:")
                results.print()  # Print results to console
                st.table(results.pandas().xyxy[0])  # Display predictions as a table

                # Display image with bounding boxes
                results_img = Image.fromarray(results.render()[0])  # Render and get image with bounding boxes
                st.image(results_img, caption='Detected Traffic Objects', use_column_width=True)


if __name__ == "__main__":
    app = TrafficDetectionApp()
    app.run()
