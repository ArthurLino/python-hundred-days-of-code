with open("./Input/Letters/starting_letter.txt") as default_letter:
    content = default_letter.read()

with open("./Input/Names/invited_names.txt") as names:
    for name in names.read().split():
        new_letter_content = content.replace("[name]", name).replace("Angela", "Arthur")

        with open(f"./Output/ReadyToSend/letter_to_{name}", mode="w") as new_letter:
            new_letter.write(new_letter_content)
