with open("./Input/Names/invited_names.txt") as name_files:
    invited_guests = name_files.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    sample_letter = letter.read()

for guest in invited_guests:
    mod_letter = sample_letter.replace("[name]", guest.strip())
    with open(f"./Output/ReadyToSend/{guest.strip()}_letter", mode='w') as new_letter:
        new_letter.write(mod_letter)

