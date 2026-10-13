# Raising Exceptions with raise

> Python allows us to manually generate an exception using raise.

```py
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("Age must be 18 or above.")

print("Eligible")

```

## assert in Python

**In Python, assert is a keyword used to check whether a condition is true. If the condition is True, the program continues. If the condition is False, Python raises an AssertionError**

> It is mainly used for debugging, testing assumptions, and validating internal program logic.

```py

# syntax

assert condition, "Error message"

# example

age = 25

assert age >= 18, "Age must be 18 or above"

print("Eligible")

# AssertionError: Age must be 18 or above

```


## Exception Handling in Functions

```py
def divide(a, b):

    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero."


print(divide(10, 2))
print(divide(10, 0))
```

## Create a custom exception class

**When built-in exceptions are not descriptive enough, create your own exception by inheriting from Python's Exception class.**

```PY
class InvalidAgeError(Exception):
    pass


age = 15

try:
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above")

    print("Eligible")

except InvalidAgeError as e:
    print("Error:", e)
```
