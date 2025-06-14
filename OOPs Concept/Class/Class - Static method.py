class student:

    @staticmethod
    def staticMethod(x):
        print("You are inside static method", x)


s = student()   # using static call as it does not have instance method
s.staticMethod(10)

# ? We cannot access class or instance variables in static method unless we call the class or instance method