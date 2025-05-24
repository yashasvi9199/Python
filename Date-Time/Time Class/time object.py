from datetime import datetime
from datetime import time

# Create empty Time object
t = time()
print(t)

# With attributes
T = time(hour=7, minute=23, second=45)
print(T)

# without attributes
T = time(7, 28, 45)
print(T)

# with microseconds
T = time(8, 45, 23, 852)
print(T)