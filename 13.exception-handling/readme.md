# Exception Handling in Python

**Exception handling is a mechanism in Python used to handle runtime errors without stopping the entire program unexpectedly.**


## case one

```py
a = 10
b = 0

print(a / b)

# ZeroDivisionError: division by zero
```

## case Two

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
