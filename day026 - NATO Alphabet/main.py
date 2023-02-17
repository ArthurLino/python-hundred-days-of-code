import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
codes_dict = {row.letter: row.code for index, row in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter a word to get the it's phonetic code: ").upper()
word_codes = [codes_dict[letter] for letter in user_word]
for code in word_codes:
    print(f"{code[0]}: {code}")
