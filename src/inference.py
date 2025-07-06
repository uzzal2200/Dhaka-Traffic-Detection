import torch

class YOLOv5Inference:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = self.load_model()

    def load_model(self):
        # Load the YOLOv5 model from the Ultralytics repository using torch.hub
        return torch.hub.load('ultralytics/yolov5', 'custom', path=self.model_path, force_reload=True)

    def run_inference(self, image_path):
        # Run inference on the provided image path
        results = self.model(image_path)
        results.print()  # Print results
        return results


# src file included