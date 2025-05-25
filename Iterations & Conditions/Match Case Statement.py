def greet (name):
    match name:
        case 'Yash':
            print("Hello Yash")
        case 'Yashasvi':
            print("Hello Yashasvi")
        case _:
            print("Hello Stranger!")


greet('Yash')
greet("Yashasvi")
greet("Kuku")