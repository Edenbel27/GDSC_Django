class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Creating two instances of the Rectangle class
rectangle1 = Rectangle(4.0, 3.0)
rectangle2 = Rectangle(5.0, 2.5)

# Printing the area and perimeter of rectangle1
print("Rectangle 1:")
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())

# Printing the area and perimeter of rectangle2
print("Rectangle 2:")
print("Area:", rectangle2.area())
print("Perimeter:", rectangle2.perimeter())