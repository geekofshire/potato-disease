import streamlit as st
import tensorflow as tf
import numpy as np
from io import BytesIO
from PIL import Image
import pandas as pd

import os
import random

dir = 'training/test'
filename = random.choice(os.listdir(dir))
path = os.path.join(dir, filename)
    

st.write("Potato Leaf Disease Prediction Model")
st.file_uploader("Upload the image",type=['png','jpg','jpeg'])



