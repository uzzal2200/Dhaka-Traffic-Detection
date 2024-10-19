import os
from utils import download_data

def prepare_data():
    # Create necessary directories
    os.makedirs('data/traffic_data', exist_ok=True)

    # Download data and unzip it
    download_data('data/traffic_data/', 'https://drive.google.com/file/d/1LR1VnpEg2jN75K_Vkd6zFq3P0mzvQY7p/view?usp=sharing')
    print("Data prepared!")

if __name__ == "__main__":
    prepare_data()
