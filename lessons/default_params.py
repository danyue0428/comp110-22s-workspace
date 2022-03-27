"""Examples of default parameters."""


def add(x: int, y: int = 0, z: int = 2) -> int:
    """Default parameters gives more flexibility to a function."""
    # x and y are by default zero
    # Default parameters must follow required parameters
    return x + y + z


print(add(1))
print(add(1, 2))
print(add(1, 0, 3))
