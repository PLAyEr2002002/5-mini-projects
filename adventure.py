name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it, swim across, or build a raft? Type walk to walk around, swim to swim across, or raft to build a raft: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    elif answer == "raft":
        print("You built a raft and crossed the river safely.")
        answer = input(
            "You find a cave, would you like to enter the cave (yes/no)? ")
        if answer == "yes":
            print("You find a treasure chest in the cave and WIN!")
        elif answer == "no":
            print("You continue on your journey but get lost and lose the game.")
        else:
            print("Not a valid option. You lose.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it, head back, or try to repair the bridge (cross/back/repair)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    elif answer == "repair":
        print("You try to repair the bridge but it collapses and you lose.")
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)
