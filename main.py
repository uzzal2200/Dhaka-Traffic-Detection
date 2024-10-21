from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image
import os
import io
from src.inference import YOLOv5Inference

# Initialize FastAPI app
app = FastAPI()

# Serve static files (e.g., images) and templates (HTML)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize the YOLOv5 inference engine
inference_engine = YOLOv5Inference('./saved_models/Best_Accuracy_Dhaka_AI_Yolov5l_By_Autobot_BS_8.pt')

# Ensure 'uploads' directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.get("/", response_class=HTMLResponse)
async def get_home():
    # Display the HTML page for image upload
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    # Read uploaded file and run YOLOv5 inference
    contents = await file.read()

    # Decode the base64 image and open it with PIL
    image = Image.open(io.BytesIO(contents))

    # Save the image temporarily
    img_path = "uploads/uploaded_image.jpg"
    image.save(img_path)

    # Run YOLOv5 inference
    results = inference_engine.run_inference(img_path)

    # Save the result image with bounding boxes
    results.render()  # Render the bounding boxes
    results_img = Image.fromarray(results.ims[0])  # Convert to PIL Image (using 'ims')
    results_img_path = "uploads/results.jpg"
    results_img.save(results_img_path)

    # Send the image with bounding boxes as the response
    return FileResponse(results_img_path, media_type="image/jpeg")
