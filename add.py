import csv
from utils import *
from random import randint

def main():
    vocabs = []
    with open(csv_filename) as csvfile:
        words = csv.DictReader(csvfile)
        for row in words:
            vocabs.append(row)
    
    index = len(vocabs) + 1
    try:
        while True:
            print("Spanish")
            spanish = raw_input()
            print("English")
            english = raw_input()
            row = {fieldnames[0]: index, fieldnames[1]: spanish, fieldnames[2]: english, 
                fieldnames[3]: 3, fieldnames[5]: None, fieldnames[6]: None, fieldnames[7]: None}
            print("Vocab #%d" % (index))

            print_question("Category: ", categories[:,0])
            category = check_input(len(categories[:,0]))
            row[fieldnames[4]] = category
            category -= 1
            if len(categories[category][1]) > 0:
                print_question(categories[category][0], categories[category][1])
                minor = check_input(len(categories[category][1]))
                row[fieldnames[5]] = minor
            if categories[category][2]:
                for a, additional in enumerate(additionals):
                    print_question(additional[0], additional[1])
                    addon = check_input(len(additional[1]))
                    row[fieldnames[6 + a]] = addon
            with open(csv_filename, 'a') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow(row)
            index += 1

    except KeyboardInterrupt:
        return

if __name__ == "__main__":
    main()
