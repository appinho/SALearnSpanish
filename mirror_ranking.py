import csv
from utils import *

def main():
	vocabs1 = get_word_list("current_" + csv_filename)
	vocabs2 = get_word_list(csv_filename)

	for i in range(len(vocabs1)):

		vocabs2[i]["Rating"] = vocabs1[i]["Rating"]

	with open("new_" + csv_filename, 'w') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()
		for vocab in vocabs2:
			writer.writerow(vocab)
if __name__ == "__main__":
	main()