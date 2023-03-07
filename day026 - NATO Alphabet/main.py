import pandas


def get_phonetic_code():
    try:
        user_word = input("Enter a word to get it's phonetic code: ").upper()
        word_codes = [codes_dict[letter] for letter in user_word]
        for code in word_codes:
            print(f"{code[0]}: {code}")
    except KeyError:
        print("Only letters of the alphabet are valid. Try again.")
        get_phonetic_code()


data = pandas.read_csv("nato_phonetic_alphabet.csv")
codes_dict = {row.letter: row.code for index, row in data.iterrows()}

get_phonetic_code()
