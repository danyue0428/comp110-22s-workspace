"""EX03- Wordle - Structured With Functions."""

__author__ = "730490913"


def contains_char(a: str, b: str) -> bool: 
    """Testing each index of the first parameter string to see if it is equal to the second parameter."""
    assert len(b) == 1  # make sure we check one letter in word b per round
    i = 0
    while i < len(a):
        if a[i] == b:
            return True
        else:
            i += 1
    else: 
        return False


def emojified(guess: str, secret: str) -> str:
    """Checking whether the specific number of order of guess word is in the secret word."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    n = 0
    result = ""
    while n < len(secret):
        z: bool = contains_char(secret, guess[n])
        if guess[n] == secret[n]:
            result += GREEN_BOX
        else: 
            if z is True:
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        n += 1
    return result  # color box


def input_guess(length: int) -> str:
    """Establishing the guess word."""
    guess: str = input(f"Enter a {length} character word: ")  # ask for the guess word
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    else:
        return str(guess)  # get the input of the same length of guess word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # Your code will go here
    secret: str = "codes" 
    length: int = len(secret)  # work regardless of the secret's length
    N = 1
    while N <= 6:  # 6 times
        print(f"=== Turn {N}/6 ===")  # prompt
        guess: str = input_guess(length)  # establish the guess word
        print(emojified(guess, secret))  # get the color boxes, contains_char is inside of emojified
        if guess == secret:
            print(f"You won in {N}/6 turns!")
            return  # do not exit the program, the player can the same word chardle the next day
        else:
            N += 1
    else: 
        print("X/6 - Sorry, try again tomorrow!")  # use up all times


if __name__ == "__main__":
    main()