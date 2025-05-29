for i in range(0, 6):
    for j in range(i):
        if i == 4:
            continue
        print(i, end="")
    if i != 4:                  #this eliminates an unneccessary line space if i=4
        print()
