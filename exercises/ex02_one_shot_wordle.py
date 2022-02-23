"""EX02 - One - shot - wordle."""

__author__ = "730490913"

# extablishing a secret and guess word
secret_word: str = "python"
length: int = len(secret_word)
guess_word: str = str(input(f"What is your {length}-letter guess? "))

# setting emoji boxes
x = 0  # index of the word
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result = ""

# checking the length of guess_word
# if the length is not equal to the length of secret word, we can't execute line 22
while len(guess_word) != length: 
    guess_word = input(f"That was not {length} letters! Try again: ")

# checking indices for correct matches(the same index of the secret)
while x < len(secret_word): 
    if guess_word[x] == secret_word[x]:
        result = result + GREEN_BOX
    else:
        # checking other indices for correct letters at incorrect positions
        existence: bool = False
        indices: int = 0
        while existence is not True and indices < len(secret_word):
            if guess_word[x] == secret_word[indices]:
                existence = True
            else:
                indices += 1
        if existence is True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    x += 1

# output
print(result)

if guess_word == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
