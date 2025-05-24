from datetime import datetime

now = datetime.now()
print("Today's date time : ", now)

# creating datetime object
dt = datetime(year=2025, month=7, day=21, hour=17, minute=22, second=17)
print(f"New Date time : {dt}")

# attempting without attribute declaration
dt = datetime(2020,8,14)
print(dt)