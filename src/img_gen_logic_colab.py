# src/img_gen_logic_colab.py
import random
import ipywidgets as widgets
from datetime import datetime
from config.config_colab import models, api_token
from huggingface_hub import InferenceClient


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


