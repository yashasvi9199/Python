from datetime import date

today = date.today()
print(f"Today's date : {today}")

# extracting attributes
print("Year : ", today.year)
print("Month : ", today.month)
print("Day : ", today.day)


# print all attributes
print(dir(today))
