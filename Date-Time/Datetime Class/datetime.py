from datetime import datetime

# get current date and time
dt = datetime.now()
print(dt)                      # 2025-05-24 13:37:54.826209        YYYY-MM-DD HH:MM:SS.MS

# Print it's class type
print(type(dt))                # <class 'datetime.datetime'>

# Get date, time, timestamp
print('Date : ', dt.date())
print('Time : ', dt.time())
print('Timestamp : ', dt.timestamp())

## GETTING ATTRIBUTES

# Get Year, month, day
print('Year : ', dt.year)
print('Month : ', dt.month)
print('Day : ', dt.day)

# Get hour, minute, second, microsecond
print(f"Hours : {dt.hour}")
print(f"Minutes : {dt.minute}")
print(f"Second : {dt.second}")
print(f"Micro-seconds : {dt.microsecond}")