# finally Block 

**The finally block always executes, whether an exception occurs or not.**

```py
try:
    number = 10 / 2

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Program execution completed.")
```

## use case

- Closing files
- Closing database connections
- Releasing resources
- Closing network connections
- Cleaning temporary resources
