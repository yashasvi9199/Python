class isNameError(Exception):
    def __init__(self , arg):
        self.args = arg

class newError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise isNameError("Name Error raised")      #TODO Try commenting this one for next error to work
    raise newError("New Error raised")
except isNameError as e:
    print(e.args)
except newError as f:
    print(f.args)