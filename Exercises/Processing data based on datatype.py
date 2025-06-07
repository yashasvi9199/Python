class myClass:
    def proc(self, value):
        if isinstance(value, int):
            print("Integer")
        elif isinstance(value, float):
            print("Float")
        elif isinstance(value, str):
            print("String")
        elif isinstance(value, bool):
            print("Boolean")
        elif isinstance(value, list):
            print("List")
        elif isinstance(value, tuple):
            print("Tuple")
        elif isinstance(value, dict):
            print("Dictionary")
        elif isinstance(value, set):
            print("Set")
        elif value is None:
            print("None")
        else:
            print("Unknown")


obj = myClass()
obj.proc(10)
obj.proc(10.5)
obj.proc("Hello")
obj.proc(True)
obj.proc([1, 2, 3])
obj.proc((1, 2, 3))
obj.proc({"name": "John", "age": 30})
obj.proc({1, 2, 3})
obj.proc(None)
