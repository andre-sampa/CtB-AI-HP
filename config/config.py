import os

# Retrieve the Hugging Face token from environment variables
api_token = os.getenv("HF_TOKEN")
# Debugging: Check if the Hugging Face token is available
if not api_token:
    print("ERROR1: Hugging Face token (HF_CTB_TOKEN) is missing. Please set it as an environment variable or in Colab secrets.")
else:
    print("Hugging Face token loaded successfully.")
