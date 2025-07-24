import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
def genrate_phonetic():
    word = input("Enter a word: ").upper()
    try :
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, Alphabets only ")
        genrate_phonetic()
    print(output_list)
genrate_phonetic()