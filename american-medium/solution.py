#!/usr/bin/env python3
import sys


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

def main(file_name):
    with open(file_name, 'r') as file:
        numbers = file.readlines()

    for num in numbers:
        num = num.strip()  # Remove any trailing newlines or spaces
        if is_american(num):
            print(num)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 solver.py <filename>")
        sys.exit(1)
    main(sys.argv[1])

