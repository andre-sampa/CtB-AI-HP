# config_colab.py
from google.colab import userdata
from src.prompts import prompts  # Import prompts from prompts.py

# Retrieve the Hugging Face token from Colab secrets
api_token = userdata.get("HF_CTB_TOKEN")

# Debugging: Check if the Hugging Face token is available
if not api_token:
    print("=== Debug: Error ===")
    print("ERROR: Hugging Face token (HF_CTB_TOKEN) is missing. Please set it in Colab secrets.")
else:
    print("=== Debug: Success ===")
    print("Hugging Face token loaded successfully.")

# List of models with aliases
models = [
    {"alias": "FLUX.1-dev", "name": "black-forest-labs/FLUX.1-dev"},
]

# Debugging: Print prompt and model options
print("Model Options:", [m["alias"] for m in models])

