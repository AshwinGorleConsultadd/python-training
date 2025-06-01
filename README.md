
## Python Training
# 1. Core Syntax & Basic Concepts

### a) Python Indentation Rules
Python uses indentation means spaces or tabs to define blocks of code. It's not just for readability but it is required for compiler as well. Each block such as **if**, **for**, **def**, etc. must be indented with the same amount.

✅ Example:

    if True:
        print("This is inside the if block.")
    print("This is outside the if block.")
 


### b) Variables and Data Types
In Python variables store values. we don't need to declare a type  Python figures it out automatically.

**Common data types:**
- int: Whole numbers → **x = 5**
- float: Decimal numbers → **pi = 3.14**
- str: Text → **name = **Ashwin**
- bool: True/False → **is_active = True**
- None: Represents “nothing” → **value = None**


### c) Basic Operators

**Arithmetic operators:**
- **+** (add), **-** (subtract), ***** (multiply), **/** (divide)
- **//** (floor division, gives whole number)
- **%** (modulo, gives remainder)

**Comparison operators:**
- **==** (equal), **!=** (not equal), **>** (greater), **<** (less)

**Logical operators:**
- **and**: both must be true  
- **or**: at least one must be true  
- **not**: reverses a condition  

✅ Example:

    a = 10
    b = 5
    print(a > b and a != b)  # True
 


### d) Input/Output Handling

- **input()** → takes user input as a string  
- **print()** → displays output to the screen  

✅ Example:

    name = input("Enter your name: ")
    print("Hello", name)
 

---

### e) Error Handling Basics

Use **try**, **except**, and **finally** to manage errors and prevent your program from crashing.

✅ Example:

    try:
        num = int(input("Enter a number: "))
        print(10 / num)
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    finally:
        print("Done.")
 





# 2. Control Flow & Logic

### a) Conditional Statements (if, elif, else)  

✅ Example:

    age = 18
    if age < 13:
        print("Child")
    elif age < 18:
        print("Teenager")
    else:
        print("Adult")


### b) Loops (for, while)  
Loops are used to repeat code multiple times.

- **for loop** is used to iterate over a sequence (like a list, range, or string).
- **while loop** runs as long as a condition is true.

✅ Example (for loop):

    for i in range(5):
        print(i)

✅ Example (while loop):

    count = 0
    while count < 3:
        print("Count is", count)
        count += 1


### c) Loop Control (break, continue, pass)

- **break**: exits the loop completely.  
- **continue**: skips to the next loop iteration.  
- **pass**: does nothing, used as a placeholder when code is required syntactically.

✅ Example (break):

    for i in range(10):
        if i == 5:
            break
        print(i)

✅ Example (continue):

    for i in range(5):
        if i == 2:
            continue
        print(i)

✅ Example (pass):

    for i in range(3):
        if i == 1:
            pass  # Placeholder for future code
        print("Looping:", i)

 
# 3. Functions & Modular Code

### a) Defining & Calling Functions, Parameters, Return Values  
Functions are reusable blocks of code that perform a task.  
Use the **def** keyword to define a function

✅ Example:

    def greet(name):
        return "Hello " + name

    message = greet("Ashwin")
    print(message)


### b) Default Arguments and Keyword Arguments  
Functions can have default values for parameters.  
You can also call arguments by name (keyword arguments) for clarity.

✅ Example:

    def greet(name="Guest"):
        print("Hello", name)

    greet()  # Uses default
    greet(name="Ashwin")  # Keyword argument


### c) Scope of Variables (Global vs. Local)  
- **Local variables** exist only inside a function.  
- **Global variables** are defined outside and can be accessed everywhere.  
To modify a global variable inside a function, use the **global** keyword.

✅ Example:

    x = 10  # global

    def show():
        x = 5  # local
        print("Local x:", x)

    show()
    print("Global x:", x)


### d) Variable-Length Arguments (*args and **kwargs)  
- **\*args** lets you pass a variable number of positional arguments.  
- **\*\*kwargs** lets you pass keyworded (named) arguments.

✅ Example:

    def add_numbers(*args):
        return sum(args)

    print(add_numbers(1, 2, 3, 4))

    def show_info(**kwargs):
        for key, value in kwargs.items():
            print(key, ":", value)

    show_info(name="Ashwin", age=25)


### e) Importing and Using Modules  
Modules are files containing Python code.  
can use **import** to include them in our script.

✅ Example:

    import math
    print(math.sqrt(16))


### f) Organizing Code into Packages and __init__.py  
A package is a folder containing multiple modules.  
Adding an **\_\_init\_\_.py** file turns a folder into a Python package.  
This file can be empty or contain setup code for the package.

✅ Example structure:

    my_package/
        __init__.py
        module1.py
        module2.py

Inside **\_\_init\_\_.py**, you can control what gets imported when the package is used:

    from .module1 import functionA

Then can use:

    from my_package import functionA

This makes our code more organized and reusable.



# 4. Data Structures

### a) Lists  
Lists are used to store multiple items in a single variable.  
We can add, remove, or sort items.

✅ Example:

    fruits = ["apple", "banana", "cherry"]

- **Slicing** → We can get parts of a list:  

- **Appending** → Add item to end:  

- **Popping** → Remove last item or by index:  

- **Sorting** → Sort the list:  
    `fruits.sort()`


### b) Dictionaries  
Dictionaries store data in key-value pairs.  
We use keys to access their associated values.

✅ Example:

    person = {"name": "Ashwin", "age": 25}

- Accessing values:  
    `print(person["name"])` → `"Ashwin"`

- Adding new key-value pair:  
    `person["city"] = "Mumbai"`

- Getting keys or values:  
    `person.keys()` → `dict_keys(['name', 'age', 'city'])`  
    `person.values()` → `dict_values(['Ashwin', 25, 'Mumbai'])`


### c) Sets  
Sets store unique items and ignore duplicates.  
We use sets for mathematical operations like union and intersection.

✅ Example:

    a = {1, 2, 3}
    b = {3, 4, 5}

- **Union** → Combines both:  
    `print(a | b)` → `{1, 2, 3, 4, 5}`

- **Intersection** → Common items:  
    `print(a & b)` → `{3}`

- Adding element:  
    `a.add(6)`

- Removing element:  
    `a.remove(2)`


### d) Tuples  
Tuples are like lists but they are **immutable** (we can’t change their values after creation).

✅ Example:

    coordinates = (10, 20)

- Access values:  
    `print(coordinates[0])` → `10`

- Tuples are useful when we want a fixed set of values that should not be changed.




# 5. File Handling

### a) Reading/Writing Text Files  
We use the **open()** function to open a file and then read or write its content.  
Always remember to close the file after we’re done using it, or use a **with** block which closes it automatically.

✅ Example (write):

    file = open("example.txt", "w")
    file.write("Hello, file!")
    file.close()

✅ Example (read):

    file = open("example.txt", "r")
    content = file.read()
    print(content)
    file.close()

✅ Recommended way (using with):

    with open("example.txt", "r") as file:
        print(file.read())


### b) CSV File Operations (csv module)  
We use the **csv** module to read and write CSV (Comma-Separated Values) files.  
CSV files are often used for spreadsheets and data exchange.

✅ Example (write CSV):

    import csv

    with open("data.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age"])
        writer.writerow(["Ashwin", 25])

✅ Example (read CSV):

    with open("data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


### c) JSON Data Handling (json module)  
We use the **json** module to work with JSON data, which is common in APIs and config files.

✅ Example (write JSON):

    import json

    data = {"name": "Ashwin", "age": 25}
    with open("data.json", "w") as file:
        json.dump(data, file)

✅ Example (read JSON):

    with open("data.json", "r") as file:
        content = json.load(file)
        print(content)

Using JSON is useful when we want to store structured data or work with web services.


# 6. Object-Oriented Programming (OOP)

### a) Classes, Objects, Attributes, Methods  
Object-Oriented Programming helps us structure code using **classes** and **objects**.  
A **class** is like a blueprint, and an **object** is an actual instance of that blueprint.

- **Attributes** are variables inside a class.  
- **Methods** are functions inside a class.

✅ Example:

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            print("Hello, my name is", self.name)

    p = Person("Ashwin", 25)
    p.greet()


### b) Inheritance (Parent/Child Classes)  
We can create a new class (child) that inherits properties and methods from an existing class (parent).  
This promotes code reuse.

✅ Example:

    class Animal:
        def sound(self):
            print("This is an animal sound.")

    class Dog(Animal):
        def sound(self):
            print("Bark!")

    d = Dog()
    d.sound()  # Output: Bark!


### c) Encapsulation (Private/Protected Attributes)  
Encapsulation means hiding internal details.  
We can control access using **protected** and **private** attributes.

- **Protected** attributes: use one underscore `_`  
- **Private** attributes: use two underscores `__`

✅ Example:

    class Car:
        def __init__(self):
            self._speed = 100       # Protected
            self.__engine = "V8"    # Private

        def show_info(self):
            print("Speed:", self._speed)
            print("Engine:", self.__engine)

    c = Car()
    c.show_info()
    print(c._speed)       # Accessible (but should be treated as protected)
    # print(c.__engine)   # Not directly accessible (raises error)

Encapsulation helps us protect important parts of our code from being changed accidentally.


# 7. Advanced Topics

### a) List Comprehensions  
List comprehensions provide a clean and concise way to create new lists.

✅ Example: Squares of even numbers from 1 to 20

    squares = [x**2 for x in range(1, 21) if x % 2 == 0]

✅ Example: Words that start with a vowel

    words = ["apple", "banana", "orange", "grape", "umbrella"]
    vowels = "aeiou"
    result = [word for word in words if word[0].lower() in vowels]


### b) Lambda Functions  
Lambda functions are small anonymous functions.  
We use them when we need a simple function for a short period.

✅ Example: Find max of three numbers

    max_of_three = lambda a, b, c: max(a, b, c)
    print(max_of_three(5, 12, 7))  # Output: 12

✅ Example: Convert Celsius to Fahrenheit using map()

    celsius = [0, 10, 20, 30]
    fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
    print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0]


### c) Generators and Iterators  
Generators are functions that return values one at a time using `yield`, which saves memory.  
Iterators are objects that we can loop through with `__iter__()` and `__next__()`.

✅ Example: Generator for prime numbers up to 50

    def prime_generator():
        for num in range(2, 51):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                yield num

    for prime in prime_generator():
        print(prime)

✅ Example: Infinite even number generator

    def even_numbers():
        n = 2
        while True:
            yield n
            n += 2

    gen = even_numbers()
    for _ in range(5):
        print(next(gen))  # Output: 2, 4, 6, 8, 10

✅ Example: Class-based Fibonacci iterator

    class Fibonacci:
        def __init__(self, n):
            self.n = n
            self.a = 0
            self.b = 1
            self.count = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.count >= self.n:
                raise StopIteration
            self.count += 1
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result

    for num in Fibonacci(10):
        print(num)

These advanced concepts help us write more Pythonic and memory-efficient code.

# 8. Debugging, Testing & Code Quality

### a) Using print() for Debugging  
The simplest way to debug code is by using **print()** statements to check variable values and program flow.  
It's helpful for quick checks during development.

✅ Example:

    def add(a, b):
        print("a =", a)
        print("b =", b)
        return a + b

    result = add(5, 3)
    print("Result:", result)


### b) Basic Unit Testing (unittest module)  
Unit testing helps us make sure that individual pieces of code work correctly.  
We can use the **unittest** module to write test cases.

✅ Example:

    import unittest

    def multiply(a, b):
        return a * b

    class TestMath(unittest.TestCase):
        def test_multiply(self):
            self.assertEqual(multiply(2, 3), 6)
            self.assertEqual(multiply(0, 5), 0)

    if __name__ == "__main__":
        unittest.main()

We can also use **pytest** as an alternative testing tool. It's more concise and widely used in the industry.


### c) Code Readability (PEP8 Guidelines)  
**PEP8** is the official style guide for writing clean and readable Python code.  
Following PEP8 helps us and others understand the code better.

Key PEP8 tips:
- Use **4 spaces** for indentation (not tabs).
- Use **snake_case** for variable and function names.
- Keep lines under **79 characters** long.
- Leave **2 blank lines** between top-level functions or class definitions.
- Add **spaces** around operators → `x = a + b`
- Use **docstrings** to describe what functions and classes do.

✅ Example (clean code):

    def calculate_area(length, width):
        """Returns the area of a rectangle."""
        return length * width

Writing clean code makes collaboration easier and reduces bugs.




# 9. Virtual Environments & Package Management

### a) Creating and Managing Virtual Environments  
A **virtual environment** is an isolated Python environment that allows us to manage dependencies separately for each project.  
This helps avoid version conflicts and keeps our global Python clean.

✅ Create a virtual environment:

    python -m venv myenv

✅ Activate the environment:

- On Windows:

      myenv\Scripts\activate

- On Mac/Linux:

      source myenv/bin/activate

✅ Deactivate the environment:

    deactivate

We can also use `virtualenv` (a third-party tool) in the same way. First, install it using:

    pip install virtualenv


### b) Installing Packages with pip  
Once inside a virtual environment, we can use **pip** to install external packages.

✅ Example:

    pip install requests

To see installed packages:

    pip list

To save dependencies:

    pip freeze > requirements.txt

To install from a file:

    pip install -r requirements.txt


### c) Assignment Example: Use `requests` to Call a Free API

✅ Create a file `api_fetch.py` and write the following:

    import requests

    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Bitcoin Price in USD:", data['bpi']['USD']['rate'])
    else:
        print("Failed to fetch data")

This script fetches Bitcoin prices from a free API and prints them.  
We can run this only after installing `requests` in our virtual environment.

Using virtual environments and pip ensures our projects are clean, portable, and easy to manage.

