#!/usr/bin/env python3

import sys
import itertools
import string
from collections import Counter

# Bigram frequencies in English text (normalized)
ENGLISH_BIGRAMS = {
    'TH': 0.027, 'HE': 0.023, 'IN': 0.020, 'ER': 0.017, 'AN': 0.016, 'RE': 0.014, 'ND': 0.013,
    'AT': 0.012, 'ON': 0.011, 'NT': 0.011, 'HA': 0.011, 'ES': 0.010, 'ST': 0.010, 'EN': 0.010,
    'ED': 0.009, 'TO': 0.009, 'IT': 0.009, 'OU': 0.008, 'EA': 0.008, 'HI': 0.008, 'IS': 0.008,
    'OR': 0.007, 'TI': 0.007, 'AS': 0.007, 'TE': 0.007, 'ET': 0.007, 'NG': 0.007, 'OF': 0.007,
    'AL': 0.006, 'DE': 0.006, 'SE': 0.006, 'LE': 0.006, 'SA': 0.006, 'SI': 0.006, 'AR': 0.006
}

def create_custom_alphabet(key):
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_unique = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    remaining_letters = ''.join([c for c in base_alphabet if c not in key_unique])
    custom_alphabet = key_unique + remaining_letters
    return custom_alphabet

def create_vigenere_table(custom_alphabet):
    table = []
    for i in range(len(custom_alphabet)):
        shifted_alphabet = custom_alphabet[i:] + custom_alphabet[:i]
        table.append(shifted_alphabet)
    return table

def quagmire_decrypt(ciphertext, key1, key2):
    custom_alphabet = create_custom_alphabet(key1)
    vigenere_table = create_vigenere_table(custom_alphabet)
    
    key2_index = 0
    plaintext = ""

    for ct_char in ciphertext.upper():
        if ct_char in custom_alphabet:
            k2_char = key2[key2_index % len(key2)].upper()
            row = custom_alphabet.index(k2_char)
            col = vigenere_table[row].index(ct_char)
            plaintext += custom_alphabet[col]
            key2_index += 1
        else:
            plaintext += ct_char
    
    return plaintext

def bigram_score(text):
    bigrams = [text[i:i+2] for i in range(len(text)-1)]
    bigram_counts = Counter(bigrams)
    score = 0
    for bigram in bigrams:
        if bigram in ENGLISH_BIGRAMS:
            score += ENGLISH_BIGRAMS[bigram]
    return score

def brute_force_decrypt(encrypted_words, key1):
    possible_keys = [''.join(p) for p in itertools.product(string.ascii_uppercase, repeat=3)]
    best_score = 0
    best_decrypted_words = []
    best_key = ""

    for key2 in possible_keys:
        decrypted_attempt = [quagmire_decrypt(word, key1, key2) for word in encrypted_words]
        combined_text = ''.join(decrypted_attempt)
        score = bigram_score(combined_text)
        if score > best_score:
            best_score = score
            best_decrypted_words = decrypted_attempt
            best_key = key2

    return best_decrypted_words, best_key

if len(sys.argv) != 2:
    print("Usage: python solver.py <enciphered_input_filename>")
    sys.exit(1)

enciphered_input_filename = sys.argv[1]

with open(enciphered_input_filename, 'r') as ct_file:
    encrypted_words = ct_file.read().splitlines()

key1 = "KRYPTOS"

decrypted_words, found_key = brute_force_decrypt(encrypted_words, key1)

if decrypted_words:
    print('\n'.join(decrypted_words))
else:
    print("Failed to find a valid key.")

