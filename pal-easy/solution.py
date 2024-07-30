#!/usr/bin/env python3

import sys
from collections import Counter

def is_anapalindrome(word):
    word = word.lower()  # Normalize case
    length = len(word)
    half = length // 2

    if length % 2 == 0:
        return Counter(word[:half]) == Counter(word[half:])
    else:
        return Counter(word[:half]) == Counter(word[half+1:])

def main(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().splitlines()
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        return
    
    for word in words:
        if is_anapalindrome(word):
            print("True")
        else:
            print("False")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>", file=sys.stderr)
        sys.exit(1)
    
    main(sys.argv[1])

