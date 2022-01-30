"""EX01 - Chardle - A cute setp toward Wordle."""

__author__ = "730490913"

word: str = str(input("Enter a 5-character word: "))
if len(str(word)) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = str(input("Enter a single character: "))
if len(str(character)) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + str(character) + " in " + str(word))

number_of_matching_characters: int = 0

if character == word[0]:
    print(str(character) + " found at index 0")
    number_of_matching_characters = number_of_matching_characters + 1
if character == word[1]:
    print(str(character) + " found at index 1")
    number_of_matching_characters = number_of_matching_characters + 1
if character == word[2]:
    print(str(character) + " found at index 2")
    number_of_matching_characters = number_of_matching_characters + 1
if character == word[3]:
    print(str(character) + " found at index 3")
    number_of_matching_characters = number_of_matching_characters + 1
if character == word[4]: 
    print(str(character) + " found at index 4")
    number_of_matching_characters = number_of_matching_characters + 1

if number_of_matching_characters > 0:
    if number_of_matching_characters == 1:
        print(str(number_of_matching_characters) + " instance of " + str(character) + " found in " + str(word))
    else:
        print(str(number_of_matching_characters) + " instances of " + str(character) + " found in " + str(word))
else:
    print("No instances of " + str(character) + " found in " + str(word))
