#!/usr/bin/env python3
import sys

# Define the encoding table for RLL (2,7)
RLL_DECODING_TABLE = {
    '1000': '11',
    '0100': '10',
    '100100': '000',
    '000100': '010',
    '001000': '011',
    '00001000': '0011',
    '00100100': '0010'
}

def binary_to_ascii(data):
    """Convert binary data to ASCII, ensuring only complete bytes are processed."""
    chars = []
    # Ensure data length is a multiple of 8
    if len(data) % 8 != 0:
        data = data[:-(len(data) % 8)]  # Trim excess bits that do not make up a full byte
    for i in range(0, len(data), 8):
        byte = data[i:i+8]
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)


def rll_decode(encoded_data):
    """Decode data using RLL decoding."""
    i = 0
    decoded_data = ''
    while i < len(encoded_data):
        matched = False
        for length in sorted(RLL_DECODING_TABLE.keys(), key=len, reverse=True):
            if encoded_data[i:i+len(length)] == length:
                decoded_data += RLL_DECODING_TABLE[length]
                i += len(length)
                matched = True
                break
        if not matched:
            if i >= len(encoded_data) - 8:
                # Suspected padding at the end
                break
            else:
                raise ValueError(f"No decoding found for sequence '{encoded_data[i:]}' starting at position {i}")
    return decoded_data


def decode_file(input_filename, output_filename):
    """Decode RLL encoded data from a file and save the decoded output to another file."""
    with open(input_filename, 'r') as file:
        encoded_lines = file.readlines()
    
    decoded_strings = []
    for line in encoded_lines:
        encoded_string = line.strip()
        binary_data = rll_decode(encoded_string)
        decoded_string = binary_to_ascii(binary_data)
        decoded_strings.append(decoded_string)
    
    with open(output_filename, 'w') as file:
        for string in decoded_strings:
            file.write(f"{string}\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python rll_decoder.py <encoded_filename> <decoded_filename>")
        sys.exit(1)
    
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    decode_file(input_filename, output_filename)

if __name__ == "__main__":
    main()

