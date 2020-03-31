import csv
from utils import *
from random import randint


def print_example(words):
	print("%s %s %s %s %s" % (words[0][0], words[1][0], words[4][0], words[2][0], words[3][0]))
	raw_input()
	print("%s %s %s %s %s" % (words[0][1], words[1][1], words[4][1], words[3][1], words[2][1]))
	raw_input()

def main():
	vocabs = {}
	with open(csv_filename) as csvfile:
		words = csv.DictReader(csvfile)
		for row in words:
			major, _ = get_major(row)
			spanish_word = row[language]
			english_word = row[fieldnames[2]]
			rating = int(row[fieldnames[3]])
			if rating < 3:
				if major in vocabs:
					vocabs[major].append((english_word, spanish_word))
				else:
					vocabs[major] = [(english_word, spanish_word)]

	amount = []
	for i in range(5):
		amount.append(len(vocabs[categories[i][0]]))

	try:
		while True:
			indices = []
			for i in range(5):
				indices.append(randint(0, amount[i]))

			word_pairs = []
			for i in range(5):
				word_pair = vocabs[categories[i][0]][indices[i]]
				print(word_pair)
				word_pairs.append(word_pair)

			print(indices, amount, word_pairs)
			print_example(word_pairs)
			
			
	except KeyboardInterrupt:
		return

if __name__ == "__main__":
	main()
