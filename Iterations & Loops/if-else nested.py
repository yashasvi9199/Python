age = 60
isMember = True

if age >= 60:
    if isMember:
        discount = 30
    else:
        discount = 20
        
    print(f"Congratulations for your {discount}% discount")
else:
    print("Not eligible")