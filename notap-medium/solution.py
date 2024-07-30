#!/usr/bin/env python3
import sys

def score_game(game):
    frames = []
    rolls = []  # Collect all pin falls as integers
    game = game.strip().replace(' ', '')  # Clean input

    # Convert all throws into integer list of pinfalls
    for roll in game:
        if roll == 'X':
            rolls.append(10)
        else:
            rolls.append(int(roll))

    # Parse rolls into frames
    roll_index = 0
    while roll_index < len(rolls):
        if len(frames) < 9:  # First 9 frames
            if rolls[roll_index] >= 9:  # No-tap strike (either 9 or 10)
                frames.append([10])
                roll_index += 1
            elif roll_index < len(rolls) - 1:
                if rolls[roll_index] + rolls[roll_index + 1] == 10:  # Spare
                    frames.append([rolls[roll_index], rolls[roll_index + 1]])
                    roll_index += 2
                else:  # Normal frame
                    frames.append([rolls[roll_index], rolls[roll_index + 1]])
                    roll_index += 2
        else:  # 10th frame handling
            current_frame = []
            while roll_index < len(rolls) and len(current_frame) < 3:  # Collect up to 3 rolls in 10th frame
                pin_count = rolls[roll_index]
                current_frame.append(10 if pin_count >= 9 else pin_count)
                roll_index += 1
            frames.append(current_frame)
            break

    # Calculate score
    score = 0
    frame_scores = []  # To store score per frame for debugging
    for i in range(len(frames)):
        frame = frames[i]
        score += sum(frame)

        if i < 9:  # Bonuses for the first 9 frames
            if frame[0] == 10:  # Strike
                next_two_throws = []
                if i + 1 < len(frames):
                    next_two_throws.extend(frames[i + 1])
                    if len(next_two_throws) < 2 and i + 2 < len(frames):
                        next_two_throws.extend(frames[i + 2])
                score += sum(next_two_throws[:2])
            elif len(frame) == 2 and sum(frame) == 10:  # Spare
                if i + 1 < len(frames):
                    score += frames[i + 1][0]
        
        frame_scores.append((frame, sum(frame)))  # Debug info for the frame

    return score, frame_scores

def main(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():
                score, frame_scores = score_game(line)
                print(str(score))
                #print(f"Total Score: {score}")
                #for idx, (fr, fr_score) in enumerate(frame_scores, 1):
                #    print(f"Frame {idx}: {fr}, Frame Score: {fr_score}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)

