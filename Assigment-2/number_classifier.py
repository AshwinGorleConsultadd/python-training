def is_prime(n):
    if n <= 1:
        return False
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
        if count > 2:
            return False
    return count == 2


def classify_number(n):
    if n < 0:
        print("Negative number")
    elif n == 0:
        print("Zero is neither prime nor odd/even")
    elif n == 1:
        print("1 is not a prime number")
    else:
        if is_prime(n):
            print("Prime number")
        if n % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

try:
    num = int(input("Enter a number: "))
    classify_number(num)
except ValueError:
    print("Invalid input. Please enter an integer.")
