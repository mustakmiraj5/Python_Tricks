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
    
    # Determine quadrant of of a point
    class Quadrant:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def determine(self):
            if self.x > 0 and self.y > 0:
                return "First Quadrant"
            elif self.x < 0 and self.y > 0:
                return "Second Quadrant"
            elif self.x < 0 and self.y < 0:
                return "Third Quadrant"
            elif self.x > 0 and self.y < 0:
                return "Fourth Quadrant"
            else:
                return "Origin"
            
    # Circle
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius * self.radius

        def perimeter(self):
            return 2 * 3.14 * self.radius


if __name__ == "__main__":
    # Example usage off add 2 numbers
    addition = MainClass.AddNumbers(5, 7)
    result = addition.add()
    print(f"The sum of 5 and 7 is: {result}")

    # Example usage of subtract 2 numbers
    subtraction = MainClass.SubtractNumbers(10, 3)
    result = subtraction.subtract()
    print(f"The difference between 10 and 3 is: {result}")

    result = MainClass.AddNumbers(11,23).add()
    print(result)
    # Determine quadrant
    print("Quadrant: "+MainClass.Quadrant(-3, 4).determine())
    # Circle
    print("Circle Area: "+str(MainClass.Circle(5).area()))
    print("Circle Perimeter: "+str(MainClass.Circle(5).perimeter()))
