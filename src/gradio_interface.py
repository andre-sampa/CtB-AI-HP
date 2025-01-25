import gradio as gr
from datetime import datetime
from src.img_gen_logic import generate_image


# Gradio Interface
def generate_interface(left_hp, right_hp):
    # Generate the image
    image = generate_image(left_hp, right_hp)

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
        #right_hp = gr.Slider(0, 100, value=100, label="Right Castle HP")
    generate_button = gr.Button("Generate Image")
    output_image = gr.Image(label="Generated Image")
    with gr.Row():
        status_text = gr.Textbox(label="Status", placeholder="Waiting for input...", interactive=False)


    # Link the button to the function
    generate_button.click(
        generate_interface,
        inputs=[left_hp, right_hp],
        outputs=[output_image, status_text]
    )