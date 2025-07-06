import os
import yaml
import torch

def download_data(directory, url):
    os.system(f"gdown --id {url} -O {directory}")
    os.system(f"unzip {directory}/*.zip -d {directory}")

def load_model_config(path):
    with open(path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def load_data_config(path): # load the data
    with open(path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def load_model_weights(path):
    # Load the model using torch's load function
    model = torch.load(path, map_location=torch.device('cpu'))  # Use CPU if no GPU is available
    return model

