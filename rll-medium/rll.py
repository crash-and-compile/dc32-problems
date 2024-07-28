#!/usr/bin/env python3
import random
import string
import sys

# Configuration for the number of keys
NUM_KEYS = 50

# Define the encoding table for RLL (2,7)
RLL_ENCODING_TABLE = {
    '11': '1000',
    '10': '0100',
    '000': '100100',
    '010': '000100',
    '011': '001000',
    '0011': '00001000',
    '0010': '00100100'
}

# Create the decoding table by reversing the encoding table
RLL_DECODING_TABLE = {v: k for k, v in RLL_ENCODING_TABLE.items()}

def ascii_to_binary(data):
    """Convert ASCII data to binary."""
    return ''.join(f'{ord(c):08b}' for c in data)

def binary_to_ascii(data):
    """Convert binary data to ASCII."""
    chars = [data[i:i+8] for i in range(0, len(data), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

def rll_encode(data):
    """Encode data using RLL encoding."""
    i = 0
    encoded_data = ''
    while i < len(data):
        matched = False
        for length in sorted(RLL_ENCODING_TABLE.keys(), key=len, reverse=True):
            if data[i:i+len(length)] == length:
                encoded_data += RLL_ENCODING_TABLE[length]
                i += len(length)
                matched = True
                break
        if not matched:
            # Handle end of data and padding
            if i < len(data):
                remaining_bits = data[i:]
                while remaining_bits not in RLL_ENCODING_TABLE and len(remaining_bits) < 8:
                    remaining_bits += '0'
                if remaining_bits in RLL_ENCODING_TABLE:
                    encoded_data += RLL_ENCODING_TABLE[remaining_bits]
                i = len(data)
            else:
                raise ValueError(f"No encoding found for sequence starting at position {i}")
    return encoded_data

def generate_random_string(length):
    """Generate a random alphanumeric string of a given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_challenge_and_solution_files(challenge_filename, solution_filename):
    """Generate challenge and solution files for RLL encoded random strings."""
    with open(challenge_filename, 'w') as challenge_file, open(solution_filename, 'w') as solution_file:
        for _ in range(NUM_KEYS):
            key_length = random.randint(20, 30)
            original_string = "Key: " + generate_random_string(key_length)
            encoded_string = rll_encode(ascii_to_binary(original_string))
           
            # Writing to files
            challenge_file.write(f"{encoded_string}\n")
            solution_file.write(f"{original_string}\n")

def main():
    """Main function to handle command-line arguments and file generation."""
    if len(sys.argv) != 3:
        print("Usage: python rll_script.py <challenge_filename> <solution_filename>")
        sys.exit(1)
    
    challenge_filename = sys.argv[1]
    solution_filename = sys.argv[2]
    create_challenge_and_solution_files(challenge_filename, solution_filename)

if __name__ == "__main__":
    main()

