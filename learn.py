import csv
from utils import *
from random import randint
import sys

def get_average_rating(vocabs):
    average_rating = 0.0
    for vocab in vocabs:
        average_rating += int(vocab['Rating'])
    average_rating /= len(vocabs)
    return average_rating

def main():

    if len(sys.argv) >= 2:
        major = int(sys.argv[1])
    else:
        major = -1
    if len(sys.argv) == 3:
        minor = int(sys.argv[2])
    else:
        minor = -1

    vocabs = get_word_list("current_" + csv_filename, major, minor)
    print("# Words %s" % len(vocabs))
    
    average_rating = get_average_rating(vocabs)
    print("Start with average rating %f" % average_rating)
    try:
        while True:
            index = randint(0, len(vocabs) - 1)
            random_rating = randint(1, 4)
            vocab = vocabs[index]
            rating = int(vocab['Rating'])
            if rating < random_rating:
                print("ID %d" % index)
                ask_vocab(vocab)
                # print(rating, "->", vocab['Rating'])
    except KeyboardInterrupt:
        new_average_rating = get_average_rating(vocabs)
        print("End with rating jump %f->%f" % (average_rating, new_average_rating))

        existing_vocabs = get_word_list("current_" + csv_filename)

        for vocab in vocabs:
            line = int(vocab[fieldnames[0]]) - 1
            if int(vocab[fieldnames[0]]) == int(existing_vocabs[line][fieldnames[0]]):
                existing_vocabs[line] = vocab
            else:
                print("WARNING WRONG ID WHEN WRITING")

        with open("current_" + csv_filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for vocab in existing_vocabs:
                writer.writerow(vocab)

if __name__ == "__main__":
    main()
