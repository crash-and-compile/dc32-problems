#!/usr/bin/env python3

import cv2
import numpy as np
import base64
from PIL import Image
import io
import sys
import string

def load_images(image_dir):
    templates = {}
    for char in string.ascii_uppercase:  # Loads images for characters A to Z
        image_path = f"{image_dir}/{char}.png"
        img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
        templates[char] = img
    return templates

def match_template(image, templates):
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    matched_chars = ""
    char_width = 16
    char_height = 16

    # Divide the image into 16x16 blocks and match each block
    for i in range(0, image.shape[1], char_width):
        char_img = img_gray[:, i:i + char_width]
        max_val = -1
        best_match = '?'

        for char, template in templates.items():
            template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
            res = cv2.matchTemplate(char_img, template_gray, cv2.TM_CCOEFF_NORMED)
            _, local_max_val, _, _ = cv2.minMaxLoc(res)
            if local_max_val > max_val:
                max_val = local_max_val
                best_match = char

        matched_chars += best_match

    return matched_chars

def decode_image(base64_string, templates):
    img_data = base64.b64decode(base64_string)
    image = np.array(Image.open(io.BytesIO(img_data)))
    matched_chars = match_template(image, templates)
    return matched_chars

def main(base64_input_file, plaintext_output_file):
    templates = load_images(".")
    with open(base64_input_file, 'r') as b64_in, open(plaintext_output_file, 'w') as text_out:
        for line in b64_in:
            base64_string = line.strip()
            decoded_string = decode_image(base64_string, templates)
            text_out.write(f'{decoded_string}\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: script.py <base64_input_file> <plaintext_output_file>")
    else:
        main(sys.argv[1], sys.argv[2])

