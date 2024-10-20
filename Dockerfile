# Base image
FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8501
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "streamlit_app.py"]
