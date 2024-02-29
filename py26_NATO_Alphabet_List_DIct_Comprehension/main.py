import pandas

# DataFrame from csv
phonetic_data_frame = pandas.read_csv("nato_phonetic.csv")

# Dictionary Comprehension to extract dict from data frame
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data_frame.iterrows()}


def generate_phonetic():
    user_name = input("Enter your name: ").upper()
    try:
        # List Comprehension with condition
        result = [phonetic_dict[let] for let in user_name if not let.isspace()]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()


