#!/usr/bin/env python3
import random

# Configuration
NUM_AMERICAN = 100  # Number of American numbers to generate
NUM_RED_HERRINGS = 100  # Number of red herring numbers to generate

def generate_increasing_sequence():
    length = random.randint(2, 8)
    sequence = []
    start = random.randint(1, 9 - length)  # Ensure there's room for an increasing sequence
    for i in range(length):
        sequence.append(start + i)
    return sequence

def convert_to_base_10(sequence, base):
    return sum(d * base ** i for i, d in enumerate(reversed(sequence)))

def generate_red_herring():
    # Randomly choose the number of digits from 2 to 8
    num_digits = random.randint(2, 8)
    number = random.randint(10**(num_digits-1), 10**num_digits - 1)
    # Ensure this number is not accidentally American
    while is_american(number):
        number = random.randint(10**(num_digits-1), 10**num_digits - 1)
    return number

def is_american(number):
    number = int(number)

    def convert_to_base(n, b):
        digits = []
        while n > 0:
            digits.append(n % b)
            n = n // b
        return digits[::-1]  # Reverse to match the order from highest to lowest place value

    # Check all bases from 2 to 10
    for base in range(2, 11):
        digits = convert_to_base(number, base)
        # Check if the digits form a strictly increasing sequence where each digit is exactly 1 greater than the previous
        if len(digits) > 1 and all(digits[i] + 1 == digits[i + 1] for i in range(len(digits) - 1)):
            return True
    return False

def main(file1, file2):
    american_numbers = []
    red_herrings = []

    while len(american_numbers) < NUM_AMERICAN or len(red_herrings) < NUM_RED_HERRINGS:
        if len(american_numbers) < NUM_AMERICAN:
            sequence = generate_increasing_sequence()
            base = sequence[-1] + 1  # Base is one more than the maximum digit
            number = convert_to_base_10(sequence, base)
            american_numbers.append(number)

        if len(red_herrings) < NUM_RED_HERRINGS:
            red_herring = generate_red_herring()
            red_herrings.append(red_herring)

    # Create a copy of american_numbers for mixing in the first file
    mixed_numbers = american_numbers[:]

    # Integrate red herrings randomly into mixed_numbers
    for herring in red_herrings:
        insert_index = random.randint(0, len(mixed_numbers))
        mixed_numbers.insert(insert_index, herring)

    with open(file1, 'w') as f1, open(file2, 'w') as f2:
        for num in mixed_numbers:
            f1.write(f"{num}\n")
        for num in american_numbers:
            f2.write(f"{num}\n")


if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])

