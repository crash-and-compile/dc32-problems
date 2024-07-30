#!/usr/bin/env python3
import sys

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def digit_sum_prime(num):
    """Check if the sum of the digits of a number is a prime."""
    sum_digits = sum(int(digit) for digit in str(num))
    return is_prime(sum_digits)

def quasi_meta_prime(num):
    """Determine if the sum of the digits of num is exactly one more or one less than a prime number."""
    sum_digits = sum(int(digit) for digit in str(num))
    return (is_prime(sum_digits + 1) or is_prime(sum_digits - 1)) and not is_prime(sum_digits)

def process_file(filename):
    """Read numbers from a file and print their meta-prime or quasi-meta-prime status."""
    with open(filename, 'r') as file:
        for line in file:
            number = int(line.strip())
            if digit_sum_prime(number):
                print(f"MP")
            elif quasi_meta_prime(number):
                print(f"QMP")
            else:
                print(f"NONE")

# Usage
if len(sys.argv) != 2:
    print("Usage: python script.py <filename>")
else:
    process_file(sys.argv[1])

