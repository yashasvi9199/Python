def greet (name):
    match name:
        case 'Yash' | 'Yashasvi':
            print("Hello Yash")
        case _:
            print("Hello Stranger!")


greet('Yash')
greet("Yashasvi")
greet("Kuku")