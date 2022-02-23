"""An example function definition."""

"""declare a function: my_max"""
def my_max(a: int, b: int) -> int:
    """Returns the largeset argument."""
    if a >= b:
        return a
        
    return b 

# print(my_max(10 + 1, 10))
# result: int = my_max(100, -50)
# print(result)

"""declare a few varibles"""
x: int = 6
y: int = 5 + 2
"""function call"""
z: int = my_max(x, y)
print(z)

