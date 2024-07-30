#!/usr/bin/env python3
import sys
import random

# Configuration variables
NUM_REGULAR = 90  # Number of regular numbers
NUM_MP = 30       # Number of Meta-prime numbers
NUM_QMP = 20      # Number of Quasi-meta-prime numbers

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

def sieve_of_eratosthenes(limit):
    """Use the Sieve of Eratosthenes to find all primes up to a limit."""
    sieve = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (sieve[p] == True):
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
        p += 1
    sieve[0], sieve[1] = False, False  # 0 and 1 are not prime numbers
    return [p for p, prime in enumerate(sieve) if prime]

def find_prime_with_no_near_primes(primes, range_size=4):
    """Find a random prime such that no number within +/- range_size is prime."""
    prime_set = set(primes)  # Convert list to set for fast membership testing
    attempts = 0
    while True:
        index = random.randint(20, len(primes) - 1)
        prime = primes[index]
        
        valid = True
        for i in range(1, range_size + 1):
            if (prime + i in prime_set) or (prime - i in prime_set):
                valid = False
                break
        
        if valid:
            return prime
        attempts += 1
        if attempts > 1000:  # To avoid infinite loops
            return None

def create_number_from_sum(target_sum):
    """Generate a number where the digits sum up to the target sum."""
    digits = []
    while target_sum > 9:
        digit = random.randint(1, 9) if len(digits) == 0 else random.randint(0, 9)
        digits.append(digit)
        target_sum -= digit
    digits.append(target_sum)  # Append the remaining sum as the last digit
    number = int(''.join(map(str, digits)))
    return number

def generate_numbers(primes):
    """Generate numbers categorized as regular, MP, or QMP."""
    numbers = []
    prime_set = set(primes)
    
    # Generate MP numbers
    for _ in range(NUM_MP):
        prime = random.choice(primes)
        number = create_number_from_sum(prime)
        numbers.append((number, 'MP'))

    # Generate QMP numbers
    for _ in range(NUM_QMP):
        prime = random.choice(primes)
        if prime + 1 not in prime_set and prime - 1 not in prime_set:
            sum_digits = random.choice([prime + 1, prime - 1])
            number = create_number_from_sum(sum_digits)
            numbers.append((number, 'QMP'))

    # Generate regular numbers
    for _ in range(NUM_REGULAR):
        prime = find_prime_with_no_near_primes(primes)
        if prime:
            number = create_number_from_sum(prime - 2)
            numbers.append((number, ''))

    random.shuffle(numbers)
    return numbers

def write_files(numbers_file, answers_file, numbers):
    """Write numbers and their classifications to files."""
    with open(numbers_file, 'w') as nf, open(answers_file, 'w') as af:
        for number, label in numbers:
            nf.write(f"{number}\n")
            af.write(f"{label}\n" if label else f"NONE\n")

# Main execution
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py numbers_file.txt answers_file.txt")
        sys.exit(1)

    primes = sieve_of_eratosthenes(500)  # Ensure a large enough pool of primes
    numbers = generate_numbers(primes)
    write_files(sys.argv[1], sys.argv[2], numbers)

