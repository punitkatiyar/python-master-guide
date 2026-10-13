# Raising Exceptions with raise

> Python allows us to manually generate an exception using raise.

```py
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("Age must be 18 or above.")

print("Eligible")

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
