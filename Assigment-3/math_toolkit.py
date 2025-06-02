def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def sum_of_squares(*args):
    return sum(x * x for x in args)

while True:
    print("\nMath Toolkit Menu:")
    print("1. Factorial of a number")
    print("2. Average of numbers")
    print("3. Sum of squares using *args")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        try:
            num = int(input("Enter a number: "))
            print("Factorial:", factorial(num))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    elif choice == "2":
        try:
            nums = input("Enter numbers separated by space: ").split()
            nums = [float(n) for n in nums]
            print("Average:", average(nums))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    elif choice == "3":
        try:
            args = input("Enter numbers separated by space: ").split()
            args = [int(a) for a in args]
            print("Sum of squares:", sum_of_squares(*args))
        except ValueError:
            print("Invalid input. Please enter valid integers.")
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please select from 1 to 4.")
