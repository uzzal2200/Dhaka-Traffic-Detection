import os

def download_data_from_kaggle(dataset, download_path):
    """
    Download dataset from Kaggle using the Kaggle API.
    
    Args:
        dataset (str): The dataset identifier (e.g., "aifahim/dhaka-ai-traffic-challenge-weights-yolov5").
        download_path (str): The path where the dataset should be downloaded.
    """
    # Ensure the download path exists
    os.makedirs(download_path, exist_ok=True)

    # Run the Kaggle API command to download and unzip the dataset
    kaggle_command = f'kaggle datasets download -d {dataset} -p {download_path} --unzip'
    os.system(kaggle_command)

def prepare_data():
    """
    Prepare data by downloading the dataset from Kaggle.
    """
    dataset = "aifahim/dhaka-ai-traffic-challenge-weights-yolov5"
    download_path = "saved_models/"  # Set the target download folder to saved_models
    
    print("Downloading dataset from Kaggle...")
    download_data_from_kaggle(dataset, download_path)
    print(f"Download complete! Files saved in {download_path}")

if __name__ == "__main__":
    prepare_data()
