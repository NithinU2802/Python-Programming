import math

def calculate(radius):
    area = math.pi * radius**2
    return area

radius = float(input("Enter the radius of the circle: "))
area = calculate(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")
