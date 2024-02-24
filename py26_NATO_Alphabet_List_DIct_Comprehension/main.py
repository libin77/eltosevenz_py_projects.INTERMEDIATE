import pandas

# DataFrame from csv
phonetic_data_frame = pandas.read_csv("nato_phonetic.csv")

# Dictionary Comprehension to extract dict from data frame
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data_frame.iterrows()}

user_name = input("Enter your name: ").upper()

# List Comprehension with condition
result = [phonetic_dict[let] for let in user_name if not let.isspace()]

print(result)
