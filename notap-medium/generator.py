#!/usr/bin/env python3

import random
import sys

# Configuration variables
NUM_GAMES = 50
FRAMES_PER_GAME = 10

def generate_game():
    game = []
    for frame in range(FRAMES_PER_GAME - 1):  # First 9 frames
        first_roll = random.randint(0, 9)
        game.append(str(first_roll))
        if first_roll == 9:  # 9-pin no-tap strike, ends frame
            continue
        else:
            second_roll = random.randint(0, 10 - first_roll)
            if second_roll == 9:
                second_roll=8
            game.append(str(second_roll) if second_roll != 10 else 'X')

    # 10th frame without any 9s
    first_roll = random.randint(0, 8)
    game.append(str(first_roll))
    second_roll = random.randint(0, 10 - first_roll)
    second_roll = min(second_roll, 8)  # Ensure no roll of 9
    game.append(str(second_roll) if second_roll != 10 else 'X')
    if first_roll + second_roll >= 10:  # Spare or strike
        third_roll = random.randint(0, 8)
        game.append(str(third_roll))

    return ''.join(game)

def score_game(game):
    score = 0
    frame_index = 0
    rolls = list(game)
    
    #print(f"Scoring game: {game}")
    
    for frame in range(FRAMES_PER_GAME - 1):
        first_roll = rolls[frame_index]
        if first_roll == '9':  # Strike under 9-pin no-tap
            score += 10
            #print(f"Frame {frame + 1}: 9 (strike), Score: {score}")
            if frame_index + 1 < len(rolls):
                next_roll = rolls[frame_index + 1]
                score += 10 if next_roll == '9' else (10 if next_roll == 'X' else int(next_roll))
                if frame_index + 2 < len(rolls):
                    next_next_roll = rolls[frame_index + 2]
                    score += 10 if next_next_roll == '9' else (10 if next_next_roll == 'X' else int(next_next_roll))
            frame_index += 1
        else:
            first_roll = int(first_roll)
            second_roll = rolls[frame_index + 1]
            if second_roll == 'X':  # Raw 10 pins second roll
                second_roll = 10
            else:
                second_roll = int(second_roll)
            frame_score = first_roll + second_roll
            if frame_score == 10:
                score += 10
                #print(f"Frame {frame + 1}: {first_roll} {second_roll} (spare), Score: {score}")
                if frame_index + 2 < len(rolls):
                    next_roll = rolls[frame_index + 2]
                    score += 10 if next_roll == '9' else (10 if next_roll == 'X' else int(next_roll))
            else:
                score += frame_score
                #print(f"Frame {frame + 1}: {first_roll} {second_roll}, Score: {score}")
            frame_index += 2
    
    # 10th frame
    first_roll = int(rolls[frame_index])
    second_roll = int(rolls[frame_index + 1])
    third_roll = int(rolls[frame_index + 2]) if frame_index + 2 < len(rolls) else 0

    if first_roll == 9:
        first_roll = 10  # 9-pin no-tap strike counts as 10
    if second_roll == 9:
        second_roll = 9  # 9 as a second roll counts as 9, not 10

    score += first_roll + second_roll

    if first_roll == 10 or first_roll + second_roll == 10:  # Spare or strike
        if third_roll == 9:
            third_roll = 9  # 9 as a third roll counts as 9, not 10
        score += third_roll

    #print(f"Frame 10: {first_roll} {second_roll} {third_roll}, Score: {score}")

    return score

def generate_games(num_games):
    games = []
    for _ in range(num_games):
        game = generate_game()
        games.append(game)
    return games

def main(notation_file, scores_file):
    games = generate_games(NUM_GAMES)
    with open(notation_file, 'w') as nf, open(scores_file, 'w') as sf:
        for game in games:
            nf.write(game + '\n')
            score = score_game(game)
            sf.write(str(score) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <notation_file> <scores_file>")
        sys.exit(1)

    notation_file = sys.argv[1]
    scores_file = sys.argv[2]

    main(notation_file, scores_file)

