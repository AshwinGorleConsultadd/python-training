
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

