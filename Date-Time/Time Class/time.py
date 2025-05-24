from datetime import datetime

t= datetime.now().time()        # since we only need time and not the date as well
print(f"Time is: {t}")

# extracting the values
print("Hours : ", t.hour)
print("Minutes : ", t.minute)
print("Seconds : ", t.second)
print("Microsecond : ", t.microsecond)