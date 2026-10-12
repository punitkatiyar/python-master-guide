# Exception Handling in Python

**Exception handling is a mechanism in Python used to handle runtime errors without stopping the entire program unexpectedly.**

## Common Built-in Exceptions

| Exception | Meaning | Example |
|---|---|---|
| `ValueError` | Invalid value | `int("abc")` |
| `TypeError` | Wrong data type | `"10" + 5` |
| `ZeroDivisionError` | Division by zero | `10 / 0` |
| `IndexError` | Invalid list index | `items[10]` |
| `KeyError` | Missing dictionary key | `data["age"]` |
| `FileNotFoundError` | File doesn't exist | `open("abc.txt")` |
| `AttributeError` | Invalid attribute | `obj.xyz` |
| `NameError` | Variable doesn't exist | `print(x)` |
| `ImportError` | Import problem | invalid import |
| `ModuleNotFoundError` | Module unavailable | `import xyz` |
| `PermissionError` | Permission denied | restricted file |
| `OverflowError` | Numeric overflow | extremely large calculation |

## Basic Exception Handling Syntax

- The try block contains code that may generate an exception
- The except block handles the exception.

```py
try:
    # code that may cause an exception

except:
    # code to handle the exception
```

```py
try:
    number = int(input("Enter a number: "))
    print(10 / number)

except:
    print("Something went wrong!")
```

## Example one

```py
a = 10
b = 0

print(a / b)

# ZeroDivisionError: division by zero
```

## Solution

```py
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## Example Two

```py
balance = 5000
withdraw = int(input("Enter amount: "))

balance = balance - withdraw

print("Remaining balance:", balance)
```

## Solution

```py
balance = 5000

try:
    withdraw = int(input("Enter amount: "))
    balance = balance - withdraw
    print("Remaining balance:", balance)

except ValueError:
    print("Please enter a valid number.")
```

## Handling Different Exceptions

```py
try:
    number = int(input("Enter number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")

```

## Multiple Exceptions in One except

```py
try:
    number = int(input("Enter number: "))
    result = 100 / number

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")
```







