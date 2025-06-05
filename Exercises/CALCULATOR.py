# Creating a new fuction to Raise an exception
def checkOp(op):
    operators = ['/','*','+','-']
    if op not in operators:
        print("Available operators \'/\',\'*\',\'+\',\'-\'")
    else:
        return True
    
numb = True
opr = True

while numb:
            try:
                num1 = int(input("Please enter first number: "))
                num2 = int(input("PLease enter second number: "))
            except ValueError:
                print("Invalid Number. Only support for integers currently!")
            else:
                while opr: 
                            try:
                                operator = str(input("Please enter the character of operation: "))
                                checkOp(operator)
                            except:
                                print("Please Select a valid operator")
                            else:
                                if operator == '/':
                                    print(num1/num2)
                                elif operator == '*':
                                    print(num1*num2)
                                elif operator == '+':
                                    print(num1+num2)
                                elif operator == '-':
                                    print(num1-num2)
                                
                                opr = False
                numb = False