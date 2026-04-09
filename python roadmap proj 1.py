import random

print("I'm thinking of a number from 1 to 10\n")
print("I'll give you 3 difficulties, please choose one")
print("Please select the difficulty level:\n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")

diff = int(input("\nEnter your difficulty level (numbers): "))  # convert to int
print("\nGreat! You've chosen difficulty level", diff)

if diff == 1:
    chances = 10
elif diff == 2:
    chances = 5
elif diff == 3:
    chances = 3
else:
    print("Invalid difficulty!")
    chances = 0

secret = random.randint(1, 10)  # generate ONCE, outside the loop

for i in range(chances):
    number = int(input("\nNow, enter a number from 1 - 10: "))  # convert to int
    if number == secret:
        print("Hooray! You did it!")
        break
    else:
        print("Try again!\n")
else:
    print(f"Out of chances! The number was {secret}.")