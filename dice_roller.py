import random

print("This is your virtual dice roller")

while True:
    play = input("Would you like to roll? (Y/N)")
    if play == "Y":
        dice_roll = random.randint(1,6)
        print("Random dice roll: " + str(dice_roll))
    elif play == "N":
        print("You do not want to roll.")
        break
    else:
        print("Please enter either Y or N")