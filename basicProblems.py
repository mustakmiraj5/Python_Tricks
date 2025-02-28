class MainClass:
    class AddNumbers:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2

        def add(self):
            return self.num1 + self.num2
        
    class SubtractNumbers:
        def __init__(self, num1, num2):
            self.num1 = num1
            self.num2 = num2

        def subtract(self):
            return self.num1 - self.num2

if __name__ == "__main__":
    # Example usage off add 2 numbers
    addition = MainClass.AddNumbers(5, 7)
    result = addition.add()
    print(f"The sum of 5 and 7 is: {result}")

    # Example usage of subtract 2 numbers
    subtraction = MainClass.SubtractNumbers(10, 3)
    result = subtraction.subtract()
    print(f"The difference between 10 and 3 is: {result}")