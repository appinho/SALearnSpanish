import csv
from utils import *
from random import randint

def main():
    vocabs = []
    with open(csv_filename) as csvfile:
        words = csv.DictReader(csvfile)
        for row in words:
            vocabs.append(row)

    try:
        while True:
            index = randint(0, len(vocabs) - 1)
            random_rating = randint(1, 6)
            vocab = vocabs[index]
            rating = int(vocab['Rating'])
            if rating < random_rating:
                ask_vocab(vocab)
                # print(rating, "->", vocab['Rating'])
    except KeyboardInterrupt:
        with open("new_" + csv_filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for vocab in vocabs:
                writer.writerow(vocab)

if __name__ == "__main__":
    main()
