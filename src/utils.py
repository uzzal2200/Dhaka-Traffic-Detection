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

def load_data_config(path):
    with open(path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def load_model_weights(path):
    model = torch.load(path)
    return model
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

def load_data_config(path):
    with open(path, 'r') as f:
        config = yaml.safe_load(f)
    return config

def load_model_weights(path):
    model = torch.load(path)
    return model
