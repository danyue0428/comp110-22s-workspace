"""Implement function skeletons."""

__author__ = "730490913"


def only_evens(xs: list[int]) -> list[int]:
    """Return a list containing only the element of the input list that were even."""
    even_list: list[int] = list()
    for x in xs:
        if x % 2 == 0:
            even_list.append(x)
    return even_list


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Return a list which is a subset of the given list, between the specified start index and end index - 1."""
    rolls: list[int] = list()
    x = int(start)
    y = int(end)
    if x < 0:
        x = 0
    if y > len(xs):
        y = len(xs)
    if len(xs) == 0 or x > len(xs) or y <= 0:
        return rolls
    i: int = 0 
    for xss in xs:
        if i >= x and i < y:
            rolls.append(xss)
        i += 1
    return rolls

    
def concat(a: list[int], b: list[int]) -> list[int]:
    """Generating a new list which contains all of the elements of the first list followed by all of the second list."""
    c: list[int] = list()
    for aa in a:
        c.append(aa)
    for bb in b:
        c.append(bb)
    return c
