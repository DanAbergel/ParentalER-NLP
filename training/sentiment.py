import sys
import os
import json

POSITIVE_PATH = "positive_words.txt"
NEGATIVE_PATH = "negative_words.txt"

# Load lexicons, lowercase, strip newlines
with open(POSITIVE_PATH) as f:
    pos = set(word.strip().lower() for word in f)
with open(NEGATIVE_PATH) as f:
    neg = set(word.strip().lower() for word in f)

def calculate_sentiment(text):
    score = 0
    for word in text.split():
        word = word.lower()
        if word in pos:
            score += 1
        if word in neg:
            score -= 1
    return score

def calc_score(file_path):
    assert os.path.isfile(file_path), "Your path does not exist!"

    total = 0
    count = 0

    # NDJSON → one JSON object per line
    with open(file_path) as f:
        for line in f:
            rating = json.loads(line)
            total += calculate_sentiment(rating["text"])
            count += 1

    return total / count if count > 0 else 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sentiment.py <filename>")
        sys.exit(1)

    avg = calc_score(sys.argv[1])
    print(f"Average sentiment score for {sys.argv[1]}: {avg}")