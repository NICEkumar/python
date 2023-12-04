import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato = {row.letter: row.code for (letter, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = {letter:nato[letter] for letter in input('Name :').upper()}
print(name)