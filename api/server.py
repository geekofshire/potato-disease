import streamlit as st
import tensorflow as tf
import numpy as np
from io import BytesIO
from PIL import Image
import pandas as pd
from io import BytesIO
import imageio

import os
import random

dir = 'training/test'
filename = random.choice(os.listdir(dir))
path = os.path.join(dir, filename)
image=Image.open(path)

MODEL= tf.keras.models.load_model("../potato-disease/api/model")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def read_file_as_image(data)-> np.ndarray:
    return np.array(Image.open(BytesIO(data)))


def predict(image):
    image=read_file_as_image(imageio.read())
    img_batch=np.expand_dims(image,0)
    predictions= MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return predicted_class,confidence


st.write("Potato Leaf Disease Prediction Model")
upload=st.file_uploader("Upload the image",type=['png','jpg','jpeg'])

class_name,confidence=predict(upload)

st.write(class_name,"",confidence)
# st.sidebar.write("Download randomly selected photos for using the model")
# st.sidebar.download_button("Download",data=image)



