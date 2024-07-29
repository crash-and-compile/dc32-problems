#!/usr/bin/env python3
import sys
import random
import string

# Configuration variables
LENGTH_OF_STRING = 20  # Length of each random string
NUMBER_OF_LINES = 100  # Total number of lines to generate
CORRECT_COUNT = 70     # Number of correct checkdifferences
INCORRECT_COUNT = 30   # Number of incorrect checkdifferences (derived from total lines - correct count)

def calculate_checkdifference(data):
    checkdifference = 255
    for index, byte in enumerate(data):
        if index % 2 == 0:
            checkdifference -= byte
        else:
            checkdifference += byte
    return checkdifference

def generate_random_string(length=LENGTH_OF_STRING):
    # Exclude colon from the characters to avoid parsing issues
    valid_chars = string.ascii_letters + string.digits + string.punctuation.replace(':', '') + ' '
    return ''.join(random.choice(valid_chars) for _ in range(length))

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <output_file1> <output_file2>")
        sys.exit(1)

    output_file1 = sys.argv[1]
    output_file2 = sys.argv[2]
    entries = []

    # Generate correct entries
    for _ in range(CORRECT_COUNT):
        random_string = generate_random_string()
        data = random_string.encode('utf-8')
        checkdiff = calculate_checkdifference(data)
        entries.append((f"{random_string}:{checkdiff}", "True"))

    # Generate incorrect entries
    for _ in range(INCORRECT_COUNT):
        random_string = generate_random_string()
        data = random_string.encode('utf-8')
        checkdiff = calculate_checkdifference(data)
        # Introduce a small error in the checkdifference (1 to 3 offset)
        error = random.choice([-3, -2, -1, 1, 2, 3])
        checkdiff += error
        entries.append((f"{random_string}:{checkdiff}", "False"))

    # Shuffle the entries to mix correct and incorrect ones
    random.shuffle(entries)

    # Write the entries to files
    with open(output_file1, 'w') as f1, open(output_file2, 'w') as f2:
        for entry, truth in entries:
            f1.write(entry + "\n")
            f2.write(truth + "\n")

if __name__ == "__main__":
    main()

