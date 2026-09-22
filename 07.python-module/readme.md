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








  



