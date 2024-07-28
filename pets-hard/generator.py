#!/usr/bin/env python3

#WARNING:
#pip install Pillow
#or this won't work

import os
import random
import string
import base64
from PIL import Image
from io import BytesIO

# Global Configuration Variables
RANDOM_STRING_LENGTH = 10
NUMBER_STRINGS = 50
CHAR_WIDTH = 16
CHAR_HEIGHT = 16

# Function to generate random strings
def generate_random_strings(length, number):
    return [''.join(random.choices(string.ascii_uppercase, k=length)) for _ in range(number)]

# Function to create an image from a string
def create_image_from_string(s, char_images):
    width = len(s) * CHAR_WIDTH
    img = Image.new('RGB', (width, CHAR_HEIGHT), color=(0, 0, 0))
    for i, char in enumerate(s):
        char_img = char_images[char]
        img.paste(char_img, (i * CHAR_WIDTH, 0))
    return img

# Main function
def main(base64_output_file, plaintext_output_file):
    # Load character images
    char_images = {char: Image.open(f'{char}.png') for char in string.ascii_uppercase}

    # Generate random strings
    random_strings = generate_random_strings(RANDOM_STRING_LENGTH, NUMBER_STRINGS)

    # Open output files
    with open(base64_output_file, 'w') as b64_out, open(plaintext_output_file, 'w') as text_out:
        for s in random_strings:
            # Create image
            img = create_image_from_string(s, char_images)

            # Save image to a bytes buffer
            buffered = BytesIO()
            img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

            # Write to output files
            b64_out.write(f'{img_str}\n')
            text_out.write(f'{s}\n')

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: script.py <base64_output_file> <plaintext_output_file>")
    else:
        main(sys.argv[1], sys.argv[2])

