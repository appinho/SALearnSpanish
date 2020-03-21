import numpy as np

language = 'German'
fieldnames = ['Index', language, 'English', 'Rating', 'Major', 'Minor', 'Gender', 'Quantity']
csv_filename = 'vocabs.csv'

categories = np.array([
	["Pronoun", ["Person", "Possessive", "Article"], True],
	["Verb", ["Regular", "Irregular"], False],
	["Object", ["Food", "Body", "Places", "Nature", "Travel",
	"Home", "Career", "Education", "Action", "Time", "Misc"], True],
	["Adjective", ["Taste", "Size", "Weather", "Numbers", "Place", "Feeling", "Misc"], False],
	["Adverb", [], False],
	["Conjunction", [], False]
])

additionals = np.array([
	["Gender", ["Male", "Female", "Neutral"]],
	["Quantity", ["Singular", "Plural"]]
])

def print_question(question, options):
	print(question),
	for i, option in enumerate(options):
		print("%d) %s" % (i + 1, option)),
	print("")

def check_input(r):
	while True:
		answer = raw_input()
		try:
			answer = int(answer)
			if answer > 0 and answer <= r:
				break
			else:
				print("Type in a number!")
		except ValueError:
			print("Type in a number!")
	return answer

def ask_vocab(row):
	print("%s: %s" % (fieldnames[2], row[fieldnames[2]]))
	raw_input()
	print("%s: %s" % (fieldnames[1], row[fieldnames[1]]))
	print("Correct 1) Yes 2) No")
	correct = check_input(2)
	rating = int(row[fieldnames[3]])
	if correct == 1:
		rating = min(5, rating + 1)
	else:
		rating = max(1, rating - 1)
	row[fieldnames[3]] = rating