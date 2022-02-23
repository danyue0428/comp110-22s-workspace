"""Some examples of tender, loving function definitions."""

def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return (f"I love you {name}!!!!")

#print(love("Nancy"))

def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message in times."""
    love_note: str = ""
    i: int = 0
    while i < n:
        # Concatenation
        i += 1
        love_note += love(to) + "\n"
    return love_note

def mystery(n: int) -> str:
    """A useless function."""
    i: int = 0
    while i < n:
        if i % 2 ==1:
            return "ohh"
        i += 1
    return "ahh"

print(mystery(4))