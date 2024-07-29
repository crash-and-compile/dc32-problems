#!/usr/bin/env python3
import sys
import random
import itertools

# Configuration
WORDS_DICTIONARY = ["apple", "elephant", "tiger", "rat", "top", "peach", "hat", "turtle", "elephantine", "antelope",
        "access", "argued", "having", "nigeria", "catalogs", "careers",
        "derby", "yours", "connecticut", "lanka", "accommodations", "strongly",
        "timing", "first", "prepared", "insight", "malawi", "mechanics",
        "memories", "participated", "else", "lee", "signs", "editor",
        "providing", "israel", "complexity", "gently", "pasta", "analyzed",
        "algorithm", "abu", "compressed", "african", "society", "terminals",
        "scary", "completing", "elite", "descending", "fiji", "other",
        "robot", "wind", "representations", "amd", "reservations", "dt",
        "oh", "consideration", "thereof", "humanity", "left", "terrace",
        "efficiently", "properly", "legend", "vehicles", "substitute", "growing",
        "mens", "remedy", "championships", "wan", "instances", "passing",
        "thunder", "rochester", "sometimes", "vic", "clock", "refurbished",
        "presidential", "prevent", "thru", "switzerland", "bits", "about",
        "commodity", "antiques", "defining", "email", "huge", "focus",
        "sessions", "quick", "swimming", "lb", "machine", "opponents",
        "hardly", "pie", "swing", "lime", "dir", "oasis",
        "effectively", "privileges", "swiss"]
NUM_WORDS_PER_CHAIN_SET = 5
NUM_CHAIN_CHALLENGES = 50


def longest_chain_length(words):
    from collections import defaultdict, deque

    def build_graph(words):
        graph = defaultdict(list)
        starts_with = defaultdict(list)
        for word in words:
            starts_with[word[0]].append(word)
        for word in words:
            if word[-1] in starts_with:
                graph[word].extend(starts_with[word[-1]])
        return graph

    def find_longest_chain(graph, start_word):
        max_length, max_chain = 0, []
        stack = [(start_word, [start_word], len(start_word))]
        while stack:
            current_word, path, length = stack.pop()
            updated = False
            for next_word in graph[current_word]:
                if next_word not in path:
                    updated = True
                    stack.append((next_word, path + [next_word], length + len(next_word)))
            if not updated and length > max_length:
                max_length, max_chain = length, path
        return max_length, max_chain

    graph = build_graph(words)
    overall_max_length, overall_max_chain = 0, []
    for word in words:
        max_length, max_chain = find_longest_chain(graph, word)
        if max_length > overall_max_length:
            overall_max_length, overall_max_chain = max_length, max_chain

    return overall_max_length, overall_max_chain

def create_mixed_chain(dictionary):
    words = random.sample(dictionary, NUM_WORDS_PER_CHAIN_SET)  # Start with a random selection of 5 words

    # Ensure to insert at least one valid chain in the list
    first_word = random.choice(dictionary)
    second_word_candidates = [word for word in dictionary if word.startswith(first_word[-1]) and word != first_word]
    if second_word_candidates:
        second_word = random.choice(second_word_candidates)
        chain_start_index = random.randint(0, NUM_WORDS_PER_CHAIN_SET - 2)
        words[chain_start_index] = first_word
        words[chain_start_index + 1] = second_word

    return words

def main(challenge_filename, solution_filename):
    with open(challenge_filename, 'w') as challenge_file, open(solution_filename, 'w') as solution_file:
        for _ in range(NUM_CHAIN_CHALLENGES):
            selected_words = create_mixed_chain(WORDS_DICTIONARY)
            challenge_file.write(" ".join(selected_words) + "\n")
            longest_length, longest_chain = longest_chain_length(selected_words)
            solution_file.write(str(longest_length) + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <challenge_filename> <solution_filename>")
        sys.exit(1)

    challenge_filename = sys.argv[1]
    solution_filename = sys.argv[2]
    main(challenge_filename, solution_filename)

