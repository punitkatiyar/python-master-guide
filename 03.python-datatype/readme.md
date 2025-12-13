# Python Data Types
**Python has several built-in data types that help you store, organize, and process data efficiently.**

1. **Primitive Types** → int, float, complex, bool, str
2. **Collection Types** → list, tuple, set, dict
3. **Special Types** → NoneType, bytes, bytearray, range

## how to input data using Python

```
# 1. Basic Input in Python

variable = input("Enter something: ");

name = input("Enter your name: ")
print("Hello", name)

# 2. Input as Number (int / float)

age = int(input("Enter your age: "))
print("Your age is:", age)

salary = float(input("Enter your salary: "))
print("Salary:", salary)

# 3. Taking Multiple Inputs

a, b = input("Enter two numbers: ").split()
print(a, b)

a, b = map(int, input("Enter two numbers: ").split())
print(a + b)

# 4. Input in a List

numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)

```












