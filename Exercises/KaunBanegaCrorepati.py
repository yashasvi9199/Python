import time
quest = [
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
    {
        "question": "What comes after Saturday?",
        "answer": "a",
        "a": "Sunday",
        "b": "Monday",
        "c": "Tuesday",
        "d": "Wednesday",
    },
]

amount = [
    "1,000",
    "2,000",
    "3,000",
    "5,000",
    "10,000",  # ? Level
    "20,000",
    "40,000",
    "80,000",
    "1,60,000",
    "3,20,000",  # ? Level
    "6,40,000",
    "12,50,000",
    "25,00,000",
    "50,00,000",
    "1,00,00,000",  # ? Level
]

level = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Name = None
first_run = True


# * Greeting
def welcome():
    while True:
        global Name
        Name = input("Enter your name: ")
        Name = Name.capitalize()
        print(
            f"Your name is {Name}. Correct? \nPress enter to continue or any key to re-enter your name"
        )
        choice = input()
        if choice == "":
            break

    print(f"Welcome {Name}, to Kaun Banega Crorepati. ")


def checkAmount(ans, index, quit=False):
    print()
    lvl = level[index]
    if quit is False:

        if ans is False:

            if lvl <= 5:
                cash = 0

            elif lvl > 5 and lvl <= 10:
                cash = amount[4]  # ? Logically it is 5th level

            elif lvl > 10:
                cash = amount[9]  # ? Logically it is 10th level

        elif ans is True:
            cash = amount[index]

    elif quit is True:
        cash = amount[index - 1]

    return cash


# * Checking quit and then printing options for quest
def checkQuit(index):
    #! Warning guest about quitting dangers
    print(
        f"Are you sure you want to quit here? \nWe are currently at Q{level[index]} with an amount of Rs.{amount[index]}"
    )
    print(
        f"If you quit now, your Dhanraashi will be Rs.{checkAmount(False,index,True)}"
    )

    while True:
        # * Asking guest for choice
        choice = input("Press enter to continue or 'n' to quit ")
        match choice.lower():
            case "":

                print(f"{quest[index]['question']}")

                print(f"a. {quest[index]['a']}      b. {quest[index]['b']}")
                print(f"c. {quest[index]['c']}      d. {quest[index]['d']}")

                return True  # * Continue the game and print options
                # break     Not needed due to return statement
            case "n":
                print(
                    f"Well played {Name} ji. It was a wonderful game with you today. \nYour Dhanraashi will be Rs.{checkAmount(False,index,True)}"
                )
                return False  # * End the game and give him final amount
            case _:
                print("\nPlease enter valid option!")


def checkAnswer(index):
    while True:
        ans = input("Choose from options a-d : ")
        if ans.lower() in ["a", "b", "c", "d"]:
            if ans.lower() == quest[index]["answer"]:
                print(f"Correct Answer, {Name}. You won {amount[index]}")
                return True
            else:
                print(
                    f"This was wrong answer {Name} ji. We need to end our journey here as the answer was {quest[index]['answer']}!"
                )
                print(
                    f"Today you will be taking with you an amount of Rs.{checkAmount(False,index)}"
                )

                return False
            break
        else:
            print("\nPlease enter valid option!")


# *Printing question
def printQuestion(index):

    print(f"{quest[index]['question']}")

    print(f"a. {quest[index]['a']}      b. {quest[index]['b']}")
    print(f"c. {quest[index]['c']}      d. {quest[index]['d']}")

    # * Printing options based on choices
    # ? If the guest is not at level 5, he cannot willingly quit.
    if level[index] > 5:

        global first_run
        while True:
            print()  # * Indentation for ease in printing strings
            
            #* Delay for 1 second only for first print
            if first_run:
                time.sleep(1)
                first_run = False

            # * Asking guest for choice
            quit = input("Do you want to quit? Press enter to continue or 'n' to quit ")

            if quit == "":
                return True

            elif quit.lower() == "n":

                # ? Write something here to check his cash and quit game
                choice = checkQuit(index)

                # * Continue the game if choice is True
                if choice:
                    return True

                # * End the game if choice is False
                else:
                    return False
            else:
                print("Please choose correct option")


# * Initiating question and level with amount
def printGreeting(index):
    print(f"{Name} ji, Here is Q{level[index]} for an amount of Rs.{amount[index]}")


welcome()
for index in range(0, 15):
    print()
    printGreeting(index)

    # * Checking Quit/ Response of guest and Printing question and options
    checkResponse = printQuestion(index)
    if checkResponse is False:
        # * Quitting game and exiting loop for game on guest's choice
        break

    # * Checking answer
    answer = checkAnswer(index)
    if answer is False:
        # * Quitting game and exiting loop for game on wrong answer
        break
