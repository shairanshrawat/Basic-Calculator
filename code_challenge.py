class Operator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b


if __name__ == "__main__":
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))
    oper = Operator(a, b)
    operation = input("Enter the operation to perform with the two numbers: ")

    if operation == "+" or operation.lower() == "add":
        result = oper.add()
    elif operation == "-" or operation.lower() == "subtract":
        result = oper.sub()
    elif operation == "*" or operation.lower() == "multiply":
        result = oper.mul()
    elif operation == "/" or operation.lower() == "divide":
        result = oper.div()
    else:
        print("Please enter a valid operation")

    print("Result is: %.2f" %result)    



