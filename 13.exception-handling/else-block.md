# else Block

**The else block executes only when no exception occurs.**

## Syntax

```py
try:
    # risky code

except:
    # error handling

else:
    # successful execution
```

## Example

```py
try:
    number = int(input("Enter number: "))
    result = 100 / number

except ValueError:
    print("Invalid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)
```
