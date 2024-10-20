# Dhaka Traffic Detection with YOLOv5 and Streamlit

This project is a traffic detection system built using YOLOv5, Streamlit, and PyTorch. The goal is to detect traffic objects in images using a trained YOLOv5 model and deploy the system via Streamlit Cloud.

## Project Structure

- `streamlit/`: Streamlit app to upload images and run inference.
- `src/`: Core Python scripts for data preparation, model training, and inference.
- `saved_models/`: Folder to store YOLOv5 trained model weights.
- `data/`: Dataset for training and evaluation.
- `uploads/`: Uploaded images for inference.

## How to Run

**Set up the Conda Environment:**
   ```bash
   conda env create -f environment.yml
   conda activate dhaka-traffic-detection
   ```

Run Streamlit App:

```bash
streamlit run streamlit/app.p
```

Deploy on Streamlit Cloud:

Push the project to GitHub.
Go to Streamlit Cloud and deploy the app.

**Dependencies**
- Python 3.9
- Streamlit
- PyTorch
- YOLOv5
- Pillow


---

### Running the Project Locally

1. **Activate your Conda environment**:

```bash
conda activate dhaka-traffic-detection
```

2. **Download the Dataset from Kaggle**
This project uses a dataset hosted on Kaggle. Follow these steps to download the dataset:

Install the Kaggle API (if not already installed):

```bash
pip install kaggle
```
Set up the Kaggle API credentials:

Download the kaggle.json file from your Kaggle account by navigating to the API section and creating a new API token.

Move the kaggle.json file to the appropriate location:

```bash
mkdir ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

Download the dataset:

Use the following command to download the YOLOv5 weights dataset into the saved_models/ folder:

```bash
kaggle datasets download -d aifahim/dhaka-ai-traffic-challenge-weights-yolov5 -p saved_models --unzip
```

This will download and unzip the trained YOLOv5 weights into the saved_models/ folder.

2. **Run the Streamlit app**:

    ```bash
    streamlit run streamlit/app.py
    ```

Your app will be available locally at `http://localhost:8501`.

### Deploying to Streamlit Cloud

1. Push your project to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and create a new app.
3. Link it to your GitHub repository and select `streamlit/app.py` as the main file.
4. Deploy your app to make it accessible online!

This setup will handle everything from model inference to deployment, all within **Strea