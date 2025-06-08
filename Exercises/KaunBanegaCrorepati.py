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

Name = "Yash"


def welcome():
    while True:
        Name = input("Enter your name: ")
        Name = Name.capitalize()
        print(
            f"Your name is {Name}. Correct? \nPress enter to continue or any key to re-enter your name"
        )
        choice = input()
        if choice == "":
            break

    print(f"Welcome {Name}, to Kaun Banega Crorepati. ")


def checkAnswer(index):
    while True:
        ans = input("Choose from options a-d : ")
        if ans.lower() in ["a", "b", "c", "d"]:
            if ans.lower() == quest[index]["answer"]:
                print(f"Correct Answer, {Name}. You won {amount[index]}")
                return True
            else:
                print(
                    f"This was wrong answer {Name} ji. We need to end our journey here!"
                )
                return False
            break
        else:
            print("\nPlease enter valid option!")


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
        cash = amount[index-1]

    return cash

def checkQuit(index):
    print()

    if level[index] <= 5:
        print(f"a. {quest[index]['a']}      b. {quest[index]['b']}")
        print(f"c. {quest[index]['c']}      d. {quest[index]['d']}")
    else:
        quit = input("Do you want to quit? Press enter to continue or any other key to quit ")
        if quit == "":
            print(f"a. {quest[index]['a']}      b. {quest[index]['b']}")
            print(f"c. {quest[index]['c']}      d. {quest[index]['d']}")
            return True         #TODO Throw True to continue the game
        else:
            print()
            #! Warning guest about quitting dangers
            print(f"Are you sure you want to quit here? \nWe are currently at Q{level[index]} with an amount of Rs.{amount[index]}")
            print(f"If you quit now, your Dhanraashi will be Rs.{checkAmount(False,index,True)}")
            return False        #TODO End the game here with False condition in main()

def printQuestion(index):
    print(f"{quest[index]['question']}")

def printGreeting(index):
    print(f"{Name} ji, Here is Q{level[index]} for an amount of Rs.{amount[index]}")


# welcome()
for index in range(12, 13):
    printGreeting(index)

    printQuestion(index)

    quit = checkQuit(index)

    answer = checkAnswer(index)

    cash = checkAmount(answer, index)

    print(f"Your Dhanraashi is {cash}")

    print("FFFFFFFF")
