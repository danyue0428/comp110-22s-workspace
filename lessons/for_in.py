"""An example of for in syntax."""

names: list[str] = ["Nancy", "Stephaine", "Ellen", "Tina"]

# Example of iterating through names using a while loop
print("while output:")
i: int = len(names) - 1
while i >= 0:
    name: str = names[i]
    print(name)
    i -= 1

# The following for..in loop is the same as the while loop
print("for..in loop output:")
for name in names:  # identifier: variable name/function name
    print(name)