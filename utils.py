import numpy as np
import csv

language = 'Spanish'
fieldnames = ['Index', language, 'English', 'Rating', 'Major', 'Minor', 'Gender', 'Quantity']
csv_filename = 'vocabs.csv'

categories = np.array([
	["Pronoun", ["Person", "Possessive", "Article"], True],
	["Verb", ["Regular", "Irregular"], False],
	["Object", ["Food", "Body", "Places", "Nature", "Travel",
	"Home", "Career", "Education", "Action", "Time", "Misc"], True],
	["Adjective", ["Sense", "Size", "Weather", "Numbers", "Place", "Feeling", "Time", "Misc"], False],
	["Adverb", [], False],
	["Conjunction", [], False],
	["Phrase", ["Greetings", "Small Talk", "Polite", "Problems", "Questions", "Answers", "Occasions", "Good bye", "Misc"], False]
])

additionals = np.array([
	["Gender", ["Male", "Female", "Neutral"]],
	["Quantity", ["Singular", "Plural"]]
])

def get_word_list(filename, major=-1, minor=-1):
	vocabs = []
	with open(filename) as csvfile:
		words = csv.DictReader(csvfile)
		for row in words:
			major_id, minor_id = get_major_minor_ids(row)
			if (major == -1 or major == major_id) and (minor == -1 or minor == minor_id):
				vocabs.append(row)
	return vocabs

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

def get_major(row):
	major_id = int(row[fieldnames[4]]) - 1
	return categories[major_id][0], major_id

def get_major_minor_ids(row):
	major_id = int(row[fieldnames[4]]) - 1
	if categories[major_id][1]:
		minor_id = int(row[fieldnames[5]]) - 1
	else:
		minor_id = None
	return major_id, minor_id

def get_major_minor(row):
	major_id, minor_id = get_major_minor_ids(row)
	major = categories[major_id]
	if minor_id is not None:
		return major[0], major[1][minor_id]
	else:
		return major[0], None

def get_gender_quantity(row):
	_, major_id = get_major(row)
	major = categories[major_id]
	if major[2]:
		gender_id = int(row['Gender']) - 1
		quantity_id = int(row['Quantity']) - 1
		return additionals[0][1][gender_id], additionals[1][1][quantity_id]
	else:
		return None, None

def ask_vocab(row):
	major, minor = get_major_minor(row)
	if minor is not None:
		print("%s: %s (%s/%s)" % (fieldnames[2], row[fieldnames[2]], 
			major , minor))
	else:
		print("%s: %s (%s)" % (fieldnames[2], row[fieldnames[2]], 
			major))
	raw_input()
	gender, quantity = get_gender_quantity(row)
	if gender:
		print("%s: %s (%s/%s)" % (fieldnames[1], row[fieldnames[1]], gender, quantity))
	else:
		print("%s: %s" % (fieldnames[1], row[fieldnames[1]]))
	print("Correct 1) Yes 2) No")
	correct = check_input(2)
	rating = int(row[fieldnames[3]])
	if correct == 1:
		rating = min(5, rating + 1)
	else:
		rating = max(1, rating - 1)
	row[fieldnames[3]] = rating