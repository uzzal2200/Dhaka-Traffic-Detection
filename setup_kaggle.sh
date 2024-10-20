#!/bin/bash

# Check if kaggle.json exists in the Downloads directory
if [ ! -f ~/Downloads/kaggle.json ]; then
    echo "Error: kaggle.json not found in the Downloads folder."
    echo "Please download it from your Kaggle account first."
    exit 1
fi

# Create the .kaggle directory if it doesn't exist
if [ ! -d ~/.kaggle ]; then
    echo "Creating .kaggle directory..."
    mkdir ~/.kaggle
fi

# Move the kaggle.json file to the .kaggle directory
echo "Moving kaggle.json to .kaggle directory..."
mv ~/Downloads/kaggle.json ~/.kaggle/

# Set correct permissions on kaggle.json
echo "Setting permissions for kaggle.json..."
chmod 600 ~/.kaggle/kaggle.json

# Verify the Kaggle setup
echo "Verifying Kaggle API setup..."
kaggle datasets list

if [ $? -eq 0 ]; then
    echo "Kaggle API setup successfully!"
else
    echo "There was an issue with the Kaggle API setup. Please check the installation and try again."
fi
