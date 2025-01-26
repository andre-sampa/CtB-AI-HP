from src.gradio_interface import demo

# Initialize the InferenceClient with the default model
#client = InferenceClient(models[0]["name"], token=api_token)

# Launch the Gradio app
demo.launch()