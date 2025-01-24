import os
import random
from huggingface_hub import InferenceClient
from PIL import Image
from datetime import datetime
import gradio as gr

# Retrieve the Hugging Face token from environment variables
api_token = os.getenv("HF_TOKEN")

# List of models with aliases
models = [
    {
        "alias": "FLUX.1-dev",
        "name": "black-forest-labs/FLUX.1-dev"
    }
]

# Initialize the InferenceClient with the default model
client = InferenceClient(models[0]["name"], token=api_token)

# Function to generate castle descriptions based on HP
def generate_castle_description(hp, color):
    if hp == 100:
        return f"a {color} flag, perfectly intact, with lush vegetation surrounding it, birds flying in the sky, and a peaceful atmosphere"
    elif hp >= 80:
        return f"a {color} flag, slightly damaged, with small red fires and smoke visible, cracks starting to appear on the walls, and a tense atmosphere"
    elif hp >= 50:
        return f"a {color} flag, moderately damaged, with larger red fires, smoke billowing from the towers, cracks spreading across the walls, and some structures partially collapsed"
    elif hp >= 30:
        return f"a {color} flag, severely damaged, with heavy red fires, thick smoke, walls crumbling, and significant structural collapse"
    elif hp >= 15:
        return f"a {color} flag, critically damaged, with most structures in ruins, intense red fire and smoke, and only a few recognizable parts of the castle remaining"
    elif hp >= 5:
        return f"a {color} flag, almost destroyed, with only a few recognizable structures still standing, engulfed in red flames, and the castle on the verge of collapse"
    else:
        return f"a {color} flag, completely ruined, with no signs of life, intense red fire and smoke, and the castle reduced to rubble"

# Function to generate the prompt
def generate_prompt(left_hp, right_hp):
    left_desc = generate_castle_description(left_hp, "blue")
    right_desc = generate_castle_description(right_hp, "red")
    return f"A wide fantasy landscape showing two castles. On the left, a castle with {left_desc}, adorned exclusively with large and prominent blue flags flying proudly. On the right, a castle with {right_desc}, adorned exclusively with large and prominent red flags flying proudly. The scene is highly detailed, with a clear contrast between the two castles. The left castle is visibly more damaged than the right castle, with significantly more red fire, smoke, and destruction. The blue flags on the left castle and the red flags on the right castle are clearly visible and distinct, ensuring no overlap in team colors. The fire is always red, regardless of the castle's team."

# Function to generate images based on the HP values
def generate_image(left_hp, right_hp, height, width, num_inference_steps, guidance_scale, seed, randomize_seed):
    # Generate the prompt
    prompt = generate_prompt(left_hp, right_hp)

    try:
        # Randomize the seed if the checkbox is checked
        if randomize_seed:
            seed = random.randint(0, 1000000)

        print(f"Using seed: {seed}")

        # Debug: Indicate that the image is being generated
        print("Generating image... Please wait.")

        # Initialize the InferenceClient with the selected model
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
        return image
    except Exception as e:
        return f"An error occurred: {e}"

# Gradio Interface
def generate_interface(left_hp, right_hp, height, width, num_inference_steps, guidance_scale, seed, randomize_seed):
    # Generate the image
    image = generate_image(left_hp, right_hp, height, width, num_inference_steps, guidance_scale, seed, randomize_seed)

    if isinstance(image, str):
        return image  # Return error message
    else:
        # Save the image with a timestamped filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{timestamp}_left_{left_hp}_right_{right_hp}.png"
        image.save(output_filename)
        return output_filename

# Gradio UI Components
with gr.Blocks() as demo:
    gr.Markdown("# Castle Image Generator")
    with gr.Row():
        left_hp = gr.Slider(0, 100, value=100, label="Left Castle HP")
        right_hp = gr.Slider(0, 100, value=100, label="Right Castle HP")
    with gr.Row():
        height = gr.Number(value=512, label="Height")
        width = gr.Number(value=1024, label="Width")
    with gr.Row():
        num_inference_steps = gr.Slider(10, 100, value=20, label="Inference Steps")
        guidance_scale = gr.Slider(1.0, 20.0, value=2.0, label="Guidance Scale")
    with gr.Row():
        seed = gr.Number(value=random.randint(0, 1000000), label="Seed")
        randomize_seed = gr.Checkbox(value=True, label="Randomize Seed")
    generate_button = gr.Button("Generate Image")
    output_image = gr.Image(label="Generated Image")

    # Link the button to the function
    generate_button.click(
        generate_interface,
        inputs=[left_hp, right_hp, height, width, num_inference_steps, guidance_scale, seed, randomize_seed],
        outputs=output_image
    )

# Launch the Gradio app
demo.launch()