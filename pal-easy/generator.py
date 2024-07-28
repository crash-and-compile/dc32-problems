#!/usr/bin/env python3

import sys
import random

# Configuration
NUM_ANAPALINDROMES = 30
NUM_REGULAR_WORDS = 50

# Capitals and numbers to throw them off a little bit
# Lists of anapalindromes and regular words
ANAPALINDROMES = [
        "Anna", "Barbra", "Beebe", "Berber", "DECed", "Dada", "Einsteins",
        "Estes", "Hannah", "ISIS", "Isis", "Kafka", "Khoikhoi", "Laval",
        "Layla", "Lulu", "Lyly", "Malayalam", "Miami", "Mimi", "Onion",
        "Oshkosh", "Otto", "Salas", "Tartar", "Tevet", "Thoth", "Tonto",
        "Toto", "Tutu", "Volvo", "alfalfa", "beriberi", "bonbon", "boob",
        "cancan", "chichi", "civic", "deed", "deified", "dodo", "edged",
        "edified", "ensconces", "entente", "estates", "ginning", "hotshot",
        "hotshots", "intestine", "intestines", "kayak", "kook", "level",
        "ma'am", "madam", "magma", "mama", "mamma", "meme", "minim",
        "murmur", "museums", "muumuu", "noon", "onion", "papa", "pawpaw",
        "peep", "pompom", "poop", "pushups", "radar", "reappear", "redder",
        "refer", "restaurateurs", "rotor", "sagas", "salsa", "sees", "sense",
        "servers", "sexes", "shahs", "shush", "signings", "solos", "stats",
        "tartar", "teammate", "tenet", "testes", "toot", "tutu", "verve",
        "8008","8oo8","7337","5al5a","7ar7ar","7oo7"
]

REGULAR_WORDS = [
    "glads", "hummocks", "yawning", "persiflage", "controllable", "subordinates",
    "deigning", "straiten", "Lords", "frisks", "database", "sours", "toneless", "Niccolo",
    "waft", "grandly", "gusset", "yuletide", "outgrowth", "pigment", "process",
    "insectivore", "palaver", "polios", "merino", "spook", "Benedictine", "rejects",
    "Cole", "Adan", "calorie", "indenturing", "somnambulism", "Antarctica", "Dunedin",
    "dully", "delaying", "friction", "tranquillest", "strictly", "paradigmatic", "residue",
    "empowers", "Phillips", "deem", "Costello", "unfavorable", "prospector", "bogging",
    "backdrop", "highchairs", "soars", "boneyest", "incompetently", "weeing", "envelope",
    "secured", "revolutionized", "yacks", "gentries", "huffing", "Zworykin", "Dawson",
    "bard", "timescales", "falterings", "wool"
]

def generate_challenge_solution(challenge_file, solution_file):
    if NUM_ANAPALINDROMES > len(ANAPALINDROMES) or NUM_REGULAR_WORDS > len(REGULAR_WORDS):
        print("Error: Requested more words than available in the lists.", file=sys.stderr)
        return

    selected_anapalindromes = random.sample(ANAPALINDROMES, NUM_ANAPALINDROMES)
    selected_regular_words = random.sample(REGULAR_WORDS, NUM_REGULAR_WORDS)

    challenge_words = selected_anapalindromes + selected_regular_words
    random.shuffle(challenge_words)

    with open(challenge_file, 'w') as cf:
        cf.write("\n".join(challenge_words) + "\n")

    with open(solution_file, 'w') as sf:
        for word in challenge_words:
            if word.lower() in map(str.lower, ANAPALINDROMES):
                sf.write(word + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_challenge.py <challenge_file> <solution_file>", file=sys.stderr)
        sys.exit(1)

    challenge_file = sys.argv[1]
    solution_file = sys.argv[2]

    generate_challenge_solution(challenge_file, solution_file)

