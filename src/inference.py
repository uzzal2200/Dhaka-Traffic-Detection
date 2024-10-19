import torch
from utils import load_model_weights

def run_inference(image_path):
    model = load_model_weights('saved_models/yolov5_weights.pt')
    results = model(image_path)
    results.print()  # Print results
    return results

if __name__ == "__main__":
    image_path = 'data/traffic_data/images/test.jpg'
    run_inference(image_path)
