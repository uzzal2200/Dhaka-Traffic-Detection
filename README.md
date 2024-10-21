# Dhaka Traffic Detection with YOLOv5, Streamlit, and FastAPI

This project is a traffic detection system built using YOLOv5, Streamlit, FastAPI, and PyTorch. The goal is to detect traffic objects in images using a trained YOLOv5 model, with options to deploy via Streamlit or FastAPI.

## Project Structure

* `streamlit/`: Streamlit app to upload images and run inference.
* `src/`: Core Python scripts for data preparation, model training, and inference.
* `saved_models/`: Folder to store YOLOv5 trained model weights.
* `data/`: Dataset for training and evaluation.
* `uploads/`: Uploaded images for inference.
* `templates/`: HTML templates for the FastAPI frontend.
* `static/`: Static files (e.g., images) for the FastAPI frontend.

## How to Run

### Set up the Conda Environment:

```bash
conda env create -f environment.yml
conda activate dhaka-traffic-detection
```

### Running the Streamlit App:

To run the Streamlit app locally:

```bash
streamlit run streamlit/app.py
```

Your app will be available locally at `http://localhost:8501`.

### Running the FastAPI App:

To run the FastAPI app locally:

```bash
uvicorn main:app --reload --port 8080
```

This will start the FastAPI server locally at `http://127.0.0.1:8080`.

## FastAPI Endpoints

* **GET /**: Renders the HTML page to upload an image for traffic detection.
* **POST /upload/**: Uploads an image and returns the processed image with detected objects.

Example to upload an image using `curl`:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8080/upload/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@your_image.jpg;type=image/jpeg'
```

## Deploy on Streamlit Cloud

Push the project to GitHub and deploy it to Streamlit Cloud using the following steps:

1. Push your project to GitHub.
2. Go to Streamlit Cloud and create a new app.
3. Link it to your GitHub repository and select `streamlit/app.py` as the main file.
4. Deploy your app to make it accessible online.

## Dependencies

* Python 3.9
* Streamlit
* FastAPI
* Uvicorn
* PyTorch
* YOLOv5
* Pillow

## Running the Project Locally

1. **Activate your Conda environment**:

```bash
conda activate dhaka-traffic-detection
```

2. **Download the Dataset from Kaggle:**

This project uses a dataset hosted on Kaggle. Follow these steps to download the dataset:

* Install the Kaggle API (if not already installed):

```bash
pip install kaggle
```

* Set up the Kaggle API credentials:
  - Download the `kaggle.json` file from your Kaggle account by navigating to the API section and creating a new API token.
  - Move the `kaggle.json` file to the appropriate location:

```bash
mkdir ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

* Download the dataset:
  Use the following command to download the YOLOv5 weights dataset into the `saved_models/` folder:

```bash
kaggle datasets download -d aifahim/dhaka-ai-traffic-challenge-weights-yolov5 -p saved_models --unzip
```

This will download and unzip the trained YOLOv5 weights into the `saved_models/` folder.

## Deploying to Streamlit Cloud

1. Push your project to a GitHub repository.
2. Go to Streamlit Cloud and create a new app.
3. Link it to your GitHub repository and select `streamlit/app.py` as the main file.
4. Deploy your app to make it accessible online!

## Additional Notes

* For FastAPI, ensure that you have installed `uvicorn`, and run the app using the command provided in the "Running the FastAPI App" section.
* This setup will handle everything from model inference to deployment, both using Streamlit and FastAPI.
