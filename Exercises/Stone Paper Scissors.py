import random

options = ["a", "b", "c"]
won = 0
lost = 0


def converter(opt):
    match opt:
        case "a":
            return "stone"
        case "b":
            return "paper"
        case "c":
            return "scissors"


for _ in range(3):
    option = random.choice(options)
    computer = converter(option)
    while True:
        choice = input("Enter 'a' for stone, 'b' for paper, 'c' for scissors: ").lower()
        if choice not in ["a", "b", "c"]:
            print("Select correct option")
        else:
            player = converter(choice)
            print(f"You chose {player} and computer chose {computer}")
            break
    decision = (
        "Won"
        if (choice == "a" and option == "b")
        or (choice == "b" and option == "c")
        or (choice == "c" and option == "a")
        else "Drawed" if choice == option else "Lost"
    )
    print(f"You {decision} the match")

    if decision == "Won":
        won += 1
    elif decision == "Lost":
        lost += 1

if won > lost:
    print("Your Won the game")
elif won < lost:
    print("Computer Won the game")
else:
    print("Game Drawed")

    
