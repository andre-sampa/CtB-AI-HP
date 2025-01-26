import random
from config.prompts import generate_prompt
from huggingface_hub import InferenceClient
from config.models import models
from config.config import api_token

# Function to generate images based on the HP values
def generate_image(left_hp, right_hp):
    # Hardcoded parameters
    height = 512  # Fixed height
    width = 1024  # Fixed width
    num_inference_steps = 20  # Fixed inference steps
    guidance_scale = 2.0  # Fixed guidance scale
    seed = random.randint(0, 1000000)  # Random seed

    # Generate the prompt
    prompt = generate_prompt(left_hp, right_hp)

    try:
        print(f"Using seed: {seed}")

        # Debug: Indicate that the image is being generated
        print("Generating image... Please wait.")

        # Initialize the InferenceClient with the selected model
            # Debugging: Check if the Hugging Face token is available
        if not api_token:
             print("ERROR2: Hugging Face token (HF_CTB_TOKEN) is missing. Please set it as an environment variable or in Colab secrets.")
        else:
             print("Hugging Face token loaded successfully.")

        client = InferenceClient(models[0]["name"], token=api_token)

        # Generate the image using the Inference API with parameters
        image = client.text_to_image(
            prompt,
            guidance_scale=guidance_scale,  # Guidance scale
            num_inference_steps=num_inference_steps,  # Number of inference steps
            width=width,  # Width
            height=height,  # Height
            seed=seed  # Random seed
        )

        # Debug: Show selected parameters
        print(f"Left Castle HP: {left_hp}")
        print(f"Right Castle HP: {right_hp}")
        print(f"Height: {height}")
        print(f"Width: {width}")
        print(f"Inference Steps: {num_inference_steps}")
        print(f"Guidance Scale: {guidance_scale}")
        print(f"Seed: {seed}")
        
        return image
    except Exception as e:
        return f"An error occurred: {e}"
