import pandas


phonetic_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dictionary = {row.letter: row.code for (index, row) in phonetic_alphabet.iterrows()}

user_input = input("Please Enter Your Name:").upper()

phonetic_name = [phonetic_dictionary[letter] for letter in user_input]

print(phonetic_name)
