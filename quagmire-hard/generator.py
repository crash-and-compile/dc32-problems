#!/usr/bin/env python3

import sys
import random

# Configuration
NUM_WORDS_TO_ENCRYPT = 50
WORD_LIST = [
    "APPLE", "BANANA", "CHERRY", "DATE", "ELDERBERRY",
    "FIG", "GRAPE", "HONEYDEW", "KIWI", "LEMON",
    "MANGO", "NECTARINE", "ORANGE", "PAPAYA", "QUINCE",
    "RASPBERRY", "STRAWBERRY", "TANGERINE", "UGLI", "VANILLA",
    "WATERMELON", "XIGUA", "YAM", "ZUCCHINI",
    "SEARCH", "INFORMATION", "CONTACT", "BUSINESS", "ONLINE", "SERVICES", "SERVICE", "PEOPLE",
    "HEALTH", "PRODUCTS", "SHOULD", "PRODUCT", "SYSTEM", "POLICY", "NUMBER", "PLEASE",
    "AVAILABLE", "COPYRIGHT", "SUPPORT", "MESSAGE", "SOFTWARE", "RIGHTS", "PUBLIC", "SCHOOL",
    "THROUGH", "REVIEW", "PRIVACY", "COMPANY", "GENERAL", "RESEARCH", "UNIVERSITY", "JANUARY",
    "REVIEWS", "PROGRAM", "MANAGEMENT", "UNITED", "INTERNATIONAL", "CENTER", "TRAVEL", "COMMENTS",
    "DEVELOPMENT", "REPORT", "MEMBER", "DETAILS", "BEFORE", "HOTELS", "BECAUSE", "RESULTS",
    "OFFICE", "EDUCATION", "NATIONAL", "DESIGN", "POSTED", "INTERNET", "ADDRESS", "COMMUNITY",
    "WITHIN", "STATES", "SHIPPING", "RESERVED", "SUBJECT", "BETWEEN", "FAMILY", "SPECIAL",
    "PRICES", "WEBSITE", "TECHNOLOGY", "PROJECT", "VERSION", "SECTION", "SPORTS", "RELATED",
    "SECURITY", "COUNTY", "AMERICAN", "MEMBERS", "NETWORK", "COMPUTER", "SYSTEMS", "FOLLOWING",
    "DOWNLOAD", "WITHOUT", "ACCESS", "RESOURCES", "CURRENT", "CONTROL", "HISTORY", "PICTURES",
    "PERSONAL", "INCLUDING", "DIRECTORY", "LOCATION", "CHANGE", "RATING", "GOVERNMENT", "CHILDREN",
    "DURING", "RETURN", "STUDENTS", "SHOPPING", "ACCOUNT", "DIGITAL", "PROFILE", "PREVIOUS",
    "EVENTS", "DEPARTMENT", "DESCRIPTION", "INSURANCE", "ANOTHER", "PROPERTY", "QUALITY", "LISTING",
    "CONTENT", "COUNTRY", "PRIVATE", "LITTLE", "CUSTOMER", "DECEMBER", "COMPARE", "MOVIES",
    "INCLUDE", "COLLEGE", "ARTICLE", "PROVIDE", "SOURCE", "AUTHOR", "DIFFERENT", "AROUND",
    "COURSE", "CANADA", "PROCESS", "TRAINING", "CREDIT", "SCIENCE", "CATEGORIES", "ADVANCED",
    "ENGLISH", "ESTATE", "CONDITIONS", "SELECT", "WINDOWS", "PHOTOS", "THREAD", "CATEGORY",
    "GALLERY", "REGISTER", "HOWEVER", "OCTOBER", "NOVEMBER", "MARKET", "LIBRARY", "REALLY",
    "ACTION", "SERIES", "FEATURES", "INDUSTRY", "PROVIDED", "REQUIRED", "SECOND", "ACCESSORIES",
    "FORUMS", "SEPTEMBER", "BETTER", "QUESTIONS", "MEDICAL", "FRIEND", "SERVER", "APPLICATION",
    "ARTICLES", "FEEDBACK", "LOOKING", "ISSUES", "COMPLETE", "STREET", "COMMENT", "FINANCIAL",
    "THINGS", "WORKING", "AGAINST", "STANDARD", "PERSON", "MOBILE", "PAYMENT", "EQUIPMENT",
    "STUDENT", "PROGRAMS", "OFFERS", "RECENT", "STORES", "PROBLEM", "MEMORY", "PERFORMANCE",
    "SOCIAL", "AUGUST", "LANGUAGE", "OPTIONS", "EXPERIENCE", "CREATE", "AMERICA", "IMPORTANT"
]

def create_custom_alphabet(key):
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_unique = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    remaining_letters = ''.join([c for c in base_alphabet if c not in key_unique])
    custom_alphabet = key_unique + remaining_letters
    return custom_alphabet

def create_vigenere_table(custom_alphabet):
    base_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    table = []
    for i in range(len(base_alphabet)):
        shifted_alphabet = custom_alphabet[i:] + custom_alphabet[:i]
        table.append(shifted_alphabet)
    return table

def quagmire_encrypt(plaintext, key1, key2):
    custom_alphabet = create_custom_alphabet(key1)
    vigenere_table = create_vigenere_table(custom_alphabet)
    
    key2_index = 0
    ciphertext = ""

    for pt_char in plaintext.upper():
        if pt_char in custom_alphabet:
            k2_char = key2[key2_index % len(key2)].upper()
            row = custom_alphabet.index(k2_char)
            col = custom_alphabet.index(pt_char)
            ciphertext += vigenere_table[row][col]
            key2_index += 1
        else:
            ciphertext += pt_char
    
    return ciphertext

def generate_random_key(length=3):
    return ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=length))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <enciphered_output_filename> <plaintext_output_filename>")
        sys.exit(1)
    
    enciphered_output_filename = sys.argv[1]
    plaintext_output_filename = sys.argv[2]

    # Select words to encrypt
    selected_words = random.sample(WORD_LIST, NUM_WORDS_TO_ENCRYPT)
    key1 = "KRYPTOS"
    key2 = generate_random_key()

    # Encrypt the words
    encrypted_words = [quagmire_encrypt(word, key1, key2) for word in selected_words]

    # Write the plaintext and encrypted words to their respective files
    with open(plaintext_output_filename, 'w') as pt_file:
        pt_file.write('\n'.join(selected_words) + '\n')
    
    with open(enciphered_output_filename, 'w') as ct_file:
        ct_file.write('\n'.join(encrypted_words) + '\n')
    

