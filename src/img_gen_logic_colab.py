# src/img_gen_logic_colab.py
from huggingface_hub import InferenceClient
from PIL import Image
import random
from datetime import datetime

def generate_image(left_hp, right_hp, height, width, num_inference_steps, guidance_scale, seed, models, api_token, randomize_seed_checkbox, seed_input):
    """
    Generate an image using the Hugging Face Inference API.
    """
    # Generate the prompt
    prompt = generate_prompt(left_hp, right_hp)

    try:
        # Randomize the seed if the checkbox is checked
        if randomize_seed_checkbox.value:
            seed = random.randint(0, 1000000)
            seed_input.value = seed  # Update the seed input box

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

def on_generate_button_clicked(b, output, left_hp_input, right_hp_input, height_input, width_input, num_inference_steps_input, guidance_scale_input, seed_input, randomize_seed_checkbox, models, api_token):
    """
    Handle the button click event.
    """
    with output:
        clear_output(wait=True)  # Clear previous output
        left_hp = left_hp_input.value
        right_hp = right_hp_input.value
        height = height_input.value
        width = width_input.value
        num_inference_steps = num_inference_steps_input.value
        guidance_scale = guidance_scale_input.value
        seed = seed_input.value

        # Debug: Show selected parameters
        print(f"Left Castle HP: {left_hp}")
        print(f"Right Castle HP: {right_hp}")
        print(f"Height: {height}")
        print(f"Width: {width}")
        print(f"Inference Steps: {num_inference_steps}")
        print(f"Guidance Scale: {guidance_scale}")
        print(f"Seed: {seed}")

        # Generate the image
        image = generate_image(left_hp, right_hp, height, width, num_inference_steps, guidance_scale, seed, models, api_token, randomize_seed_checkbox, seed_input)

        if isinstance(image, str):
            print(image)
        else:
            # Debug: Indicate that the image is being displayed and saved
            print("Image generated successfully!")
            print("Displaying image...")

            # Display the image in the notebook
            display(image)

            # Save the image with a timestamped filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"{timestamp}_left_{left_hp}_right_{right_hp}.png"
            print(f"Saving image as {output_filename}...")
            image.save(output_filename)
            print(f"Image saved as {output_filename}")