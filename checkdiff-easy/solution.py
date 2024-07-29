#!/usr/bin/env python3
import sys

def calculate_checkdifference(data):
    checkdifference = 255
    for index, byte in enumerate(data):
        if index % 2 == 0:
            checkdifference -= byte
        else:
            checkdifference += byte
    return checkdifference

def main():
    if len(sys.argv) != 2:
        print("Usage: python solution_script.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    
    try:
        with open(input_file, 'r') as file:
            for line in file:
                # Split the line into data part and checkdifference part
                data_part, provided_checkdiff_str = line.rstrip().split(':')
                # Convert provided checkdifference back to integer
                provided_checkdiff = int(provided_checkdiff_str)
                # Calculate actual checkdifference
                actual_checkdiff = calculate_checkdifference(data_part.encode('utf-8'))
                # Output True or False based on the comparison
                print("True" if actual_checkdiff == provided_checkdiff else "False")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Data format error in the input file.")
        sys.exit(1)

if __name__ == "__main__":
    main()

