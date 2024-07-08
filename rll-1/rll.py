#!/usr/bin/env python3

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
    return ''.join(f'{ord(c):08b}' for c in data)

def binary_to_ascii(data):
    chars = [data[i:i+8] for i in range(0, len(data), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

def rll_encode(data):
    i = 0
    encoded_data = ''
    while i < len(data):
        for length in sorted(RLL_ENCODING_TABLE.keys(), key=len, reverse=True):
            if data[i:i+len(length)] == length:
                encoded_data += RLL_ENCODING_TABLE[length]
                i += len(length)
                break
        else:
            unencodable_segment = data[i:i+8]  # Capture the problematic segment
            raise ValueError(f"No encoding found for sequence '{unencodable_segment}' starting at position {i}")
    return encoded_data

def rll_decode(encoded_data):
    i = 0
    decoded_data = ''
    while i < len(encoded_data):
        for length in sorted(RLL_DECODING_TABLE.keys(), key=len, reverse=True):
            if encoded_data[i:i+len(length)] == length:
                decoded_data += RLL_DECODING_TABLE[length]
                i += len(length)
                break
        else:
            undecodable_segment = encoded_data[i:i+8]  # Capture the problematic segment
            raise ValueError(f"No decoding found for sequence '{undecodable_segment}' starting at position {i}")
    return decoded_data

def encode_ascii_string(ascii_string):
    binary_data = ascii_to_binary(ascii_string)
    encoded_data = rll_encode(binary_data)
    return encoded_data

def decode_ascii_string(encoded_string):
    binary_data = rll_decode(encoded_string)
    ascii_string = binary_to_ascii(binary_data)
    return ascii_string

# Example usage
if __name__ == "__main__":
    original_string = 'Hello, World!'
    try:
        encoded_data = encode_ascii_string(original_string)
        print(f"Original ASCII String: {original_string}")
        print(f"Encoded Data: {encoded_data}")
        
        decoded_string = decode_ascii_string(encoded_data)
        print(f"Decoded ASCII String: {decoded_string}")
    except ValueError as e:
        print(e)

