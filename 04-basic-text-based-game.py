

# lets make a text based game. it will loop on and on, and display some screens.
# in each screen you will have a set of choices, choosing one will get you to the next screen.



print("You enter a big forrest, now the wolf is coming. What will you do?")
print("1 - run away")
print("2 - talk to the wolf")
print("3 - fight")
choice = input("enter your choice: ")

if choice == "1":
    print("you run towards a house, What will you do?")
    print("1 - enter the house" )
    print("2 - run away")
    choice = input("enter your choice: ")
    if choice == "1":
        print("the witch eats you. game over")
    elif choice == "2":
        print("you stumble and fall. game over")
    else:
        print("error, no such choice")
elif choice == "2":
    print("the wolf turns out to be nice, he asks you for a present")
    print("1 - give him a snack")
    print("2 - give him a saussage")
    choice = input("enter your choice: ")
    if choice == "1":
        print("the wolf says 'thank you' and gives you the key to the treasure")
    elif choice == "2":
        print("the wolf says he is a vegetarian and goes away")
    else:
        print("error, no such choice")
elif choice == "3":
    print("you win the fight, but you gained nothing...")
else:
    print("error, no such choice")

print("*** game over ***")

# exercise: make your own adventure game like this.
# Extend it to behave differently, based on some choices you did in a previous screen.
# Extend it to get different score, based on the decissions you are making
# extend the game so that you have different outcomes based on random number being drawn.
# you can get random numbers as follows.

import random
# the next statement will assign a random number between 1 and ten to the variable choice.
random_choice = random.randint(1,10)
print("random choice: ", random_choice)