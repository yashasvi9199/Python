def checker(seq):
    match seq:
        case [a,b]:                     #   list with 2 entry
            print(f"Two element list : {a}, {b}")
        
        case [a,b,c]:
            print(f"Three element list : {a}, {b}, {c}")

        case _:
            print(f"Unknown data format {seq}")


checker([1,2])
checker([1,4,7])
checker([1])