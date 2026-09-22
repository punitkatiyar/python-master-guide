# What is a Module?

**A module is a single Python file (.py) that contains variables, functions, classes, and executable code.**

> Module = one Python file

> Package = collection of related Python modules

> Framework = complete structure/tools for building an application

## Types of Modules

- Built-in Modules
- User-Defined Module
- Third-Party Modules

## Example Of Module 

```py
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

## Use The Module

```py
# main.py

import calculator

print(calculator.add(10, 20))
print(calculator.subtract(20, 5))
print(calculator.PI)

```

## Why use modules?

- Reuse code
- Organize large programs
- Avoid duplicate code
- Make code easier to maintain
- Separate functionality



