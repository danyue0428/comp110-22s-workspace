"""practice with if-then-else statement"""

choice: int = int(input("Enter a number: "))

# Implement the logic to print
# A when < 25
# B when >= 25 and <50
# C when >75
#D when >= 50 and <= 75

if choice < 25:
    print("A")
elif choice < 50:
    print ("B")
elif choice > 75:
    print("C")
else:
    print("C")