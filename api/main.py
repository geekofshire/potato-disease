
from fastapi import FastAPI,File,UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf


def read_file_as_image(data)-> np.ndarray:
    return np.array(Image.open(BytesIO(data)))

app=FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5500",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL= tf.keras.models.load_model("../potato-disease/api/model")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

@app.get("/ping")
async def ping():
    return "Hello"


@app.post('/predict')
async def predict(
    file : UploadFile=File(...)
):
    image=read_file_as_image(await file.read())
    img_batch=np.expand_dims(image,0)
    predictions= MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }

if __name__=="__main__":
    uvicorn.run(app,host='localhost',port=8080)