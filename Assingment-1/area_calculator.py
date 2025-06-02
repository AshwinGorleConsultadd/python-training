import math

def get_rectangle_area(length, width):
    return length * width

def get_circle_area(radius):
    return math.pi * radius * radius

def get_float_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

choice = input("Choose shape (rectangle/circle): ").strip().lower()

if choice == "rectangle":
    length = get_float_input("Enter length: ")
    width = get_float_input("Enter width: ")
    if length is not None and width is not None:
        print("Area of rectangle:", get_rectangle_area(length, width))
elif choice == "circle":
    radius = get_float_input("Enter radius: ")
    if radius is not None:
        print("Area of circle:", get_circle_area(radius))
else:
    print("Invalid choice")
