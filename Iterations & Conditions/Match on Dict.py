def person(data):
    match data:
        case {"name" : name, "age" : age}:
            print(f"Welcome {name}! You are {age} years old.")
        
        case {"name" : name,  "job" : job}:
            print(f"Hello {name}. You work as a {job}")
        
        case _:
            print("Incorrect format data")

person({"name":"Alice","age":25})
person({"name":"Yash", "Job":"Software Engineer"})      #   notice it didn't give case data as the key:value bindings are case sensitive