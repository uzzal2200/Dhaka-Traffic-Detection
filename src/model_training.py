import torch
from utils import load_model_config, load_data_config
from yolov5 import train

def train_model():
    # Load model and data configurations
    model_config = load_model_config('models/yolov5l.yaml')
    data_config = load_data_config('data/traffic.yaml')

    # Train the model using the loaded configurations
    train.run(data=data_config, cfg=model_config, epochs=100, batch_size=8, img_size=1024)
    print("Model trained!")

if __name__ == "__main__":
    train_model()
