from datetime import datetime

now = datetime.now()
print(now)
print(f"Datatype: {type(now)}")

str = now.strftime("%d/%m/%Y %H:%M:%S")
print("Date Time String : ", str)
print(f"Datatype : {type(str)}")
