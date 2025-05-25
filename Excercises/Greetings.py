'''
The task is to greet the person based on time and gender
'''

from datetime import datetime


# Getting name and Gender
name = input("Please enter your name : ")
name  = name.capitalize()

while True:
    gender = input("Please choose your gender (M/F)")
    if gender in ['m','M','f','F']:
        break
    else:
        print("Please choose valid option")

# if gender == 'm' or gender =='M':
#     salutations = 'Mr.'
# else:
#     salutations = 'Ms.'

salutations = 'Mr.' if gender=='m' or gender=='M' else 'Ms.'

dt = datetime.now()
hours = dt.hour
# print(hours)

match hours:
    case hours if hours > 6 and hours < 12:
        greet = "Good Morning,"
    case hours if hours > 12 and hours < 16:
        greet = "Good Afternoon,"
    case hours if hours > 16 and hours < 20:
        greet = "Good Evening,"
    case _:
        greet = "You should sleep now. Good Night!"

print(f"{greet} {salutations}{name}")