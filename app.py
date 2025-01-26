import random
from huggingface_hub import InferenceClient
from datetime import datetime
import gradio as gr
from config.config import api_token
from config.models import models
from src.gradio_interface import demo

# Initialize the InferenceClient with the default model
#client = InferenceClient(models[0]["name"], token=api_token)

# Launch the Gradio app
demo.launch()