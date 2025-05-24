# import datetime           this will throw errors ; Check bottom

from datetime import datetime


# POSIX timestamp in milliseconds only
ct = datetime.now()
print(f"Current Time: {ct}")

ts = ct.timestamp()
print(f"Timestamp : {ts}")                               # 1748078883.6943746

#  Convert date time
dt = datetime.fromtimestamp(ts)
print(f"The date and Time is : {dt}")



'''
import datetime

ct = datetime.datetime.now()
ts = ct.timestamp()

dt = datetime.datetime.fromtimestamp(ts)

Had to mention is twice to access the attribute datetime in class datetime
'''