def numCheck (x) :
    match x:
        case 10 if x%2==0:                      #   case 10 and x should an even number
            pri= "Matched 10 and it's even"
        case 10:
            pri = "Matched 10 and it's not even"
        case _:
            pri = "no results found"

    print(pri)

numCheck(10)
numCheck(12)