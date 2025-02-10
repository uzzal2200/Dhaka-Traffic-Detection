from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PIL import Image
import os
import io
from src.inference import YOLOv5Inference

# Initialize FastAPI app
app = FastAPI()

# Create necessary directories
os.makedirs('static', exist_ok=True)
os.makedirs('uploads', exist_ok=True)

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize YOLOv5 inference engine
inference_engine = YOLOv5Inference('./saved_models/Best_Accuracy_Dhaka_AI_Yolov5l_By_Autobot_BS_8.pt')


@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "show_result": False
    })


@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # Read uploaded file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        # Save uploaded image
        img_path = "uploads/uploaded_image.jpg"
        image.save(img_path)

        # Run YOLOv5 inference
        results = inference_engine.run_inference(img_path)
        results.render()  # Render the bounding boxes

        # Save the result image
        results_img = Image.fromarray(results.ims[0])
        results_img_path = "static/results.jpg"
        results_img.save(results_img_path)

        return {"success": True}

    except Exception as e:
        print(f"Error processing image: {str(e)}")
        return {"success": False, "error": str(e)}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)