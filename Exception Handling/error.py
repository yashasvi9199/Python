try:
    res = 2/0
except Exception as e:
    print("Something went wrong!!")
    print (e)
else:
    print("Voila!")