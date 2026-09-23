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

```
project/
│
├── main.py
└── calculator.py
```

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

## Different Ways to Import Modules

> **Method 1 — Import entire module**

```py
import math

print(math.sqrt(16))
```

> **Method 2 — Import specific function**

```py
from math import sqrt

print(sqrt(16))
```

> **Method 3 — Import multiple functions**

```py
from math import sqrt, pow

print(sqrt(25))
print(pow(2, 3))
```

> **Method 4 — Alias**

```py
import datetime as dt

print(dt.datetime.now())

# example

import pandas as pd
```


# Question 1: OS Module

> How many built-in functions and features does the Python os module provide?

# Question 2: File Handling with Multiple Python Modules

> Create 10 different Python files (.py) containing user-defined functions according to the following requirements:

> The functions should follow this distribution:

> 4 files should contain functions that use loops (for or while).

> 3 files should contain functions that use if-else statements.

> 3 files can contain functions of your choice (e.g., string operations, mathematical calculations, list operations, recursion, etc.).

> Every file must use  four major Python data types:

- List
- Dictionary
- Set
- Tuple

> Create a main.py file that:
> Opens each Python file using file handling (open()).

```
Project/
│
├── file1.py
├── file2.py
├── file3.py
├── file4.py
├── file5.py
├── file6.py
├── file7.py
├── file8.py
├── file9.py
├── file10.py
└── main.py
```








  



