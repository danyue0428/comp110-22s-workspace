"""Examples of importing Python."""

# from package import module
from lessons import helpers

# Alias a module / imported name as another name
from lessons import helpers as hp

# Import names defines globally in a module
from lessons.helpers import powerful, THE_ANSWER

def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))
    print(f"The answer: {hp.THE_ANSWER}")
    print(THE_ANSWER)
    print(powerful(2, 4))
# Idiom = modile that contains main function
if __name__ == "__main__":
    main()
