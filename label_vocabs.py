import csv
import pandas as pd
import sys
import os
from utils import *




def main():
    vocabs = []

    if len(sys.argv) == 2:
        start = int(sys.argv[1])
    else:
        if not os.path.isfile(csv_filename):
            with open(csv_filename, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
            start = 0
        else:
            with open(csv_filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                start = sum(1 for row in reader) - 1
    print("Starting at %d" % start)
    with open('1000_words.txt', 'r') as txtfile:
        txtfilelines =txtfile.readlines()
        for txtfileline in txtfilelines:
            words = txtfileline.split()
            vocabs.append(words)


    try:
        for index, vocab in enumerate(vocabs[start:]):
            row = {fieldnames[0]: vocab[0], fieldnames[1]: vocab[1], fieldnames[2]: vocab[2], 
                fieldnames[3]: 3, fieldnames[5]: None, fieldnames[6]: None, fieldnames[7]: None}
            # ask_vocab(row)

            # print_question("Category: ", categories[:,0])
            # category = check_input(len(categories[:,0]))
            # row[fieldnames[4]] = category
            # category -= 1
            # if len(categories[category][1]) > 0:
            #     print_question(categories[category][0], categories[category][1])
            #     minor = check_input(len(categories[category][1]))
            #     row[fieldnames[5]] = minor
            # if categories[category][2]:
            #     for a, additional in enumerate(additionals):
            #         print_question(additional[0], additional[1])
            #         addon = check_input(len(additional[1]))
            #         row[fieldnames[6 + a]] = addon
            with open(csv_filename, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(row)

    except KeyboardInterrupt:
        print('Finish!')

if __name__ == "__main__":
    main()