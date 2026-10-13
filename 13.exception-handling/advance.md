# Raising Exceptions with raise

> Python allows us to manually generate an exception using raise.

```py
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("Age must be 18 or above.")

print("Eligible")

```
