# Python Data Types
**Python has several built-in data types that help you store, organize, and process data efficiently.**

1. **Primitive Types** → int, float, complex, bool, str
2. **Collection Types** → list, tuple, set, dict
3. **Special Types** → NoneType, bytes, bytearray, range

| Category | Data Type    | Example                | Common Use Case                      |
| -------- | ------------ | ---------------------- | ------------------------------------ |
| Numeric  | `int`        | `age = 25`             | Age, quantity, count                 |
| Numeric  | `float`      | `price = 99.99`        | Price, percentage, measurements      |
| Numeric  | `complex`    | `z = 3 + 4j`           | Scientific/mathematical calculations |
| Boolean  | `bool`       | `is_active = True`     | Conditions, flags                    |
| Text     | `str`        | `"Python"`             | Names, messages, descriptions        |
| Sequence | `list`       | `[10, 20, 30]`         | Collection of editable items         |
| Sequence | `tuple`      | `(10, 20, 30)`         | Fixed collection of items            |
| Sequence | `range`      | `range(1, 10)`         | Loops and number sequences           |
| Mapping  | `dict`       | `{"name": "Punit"}`    | Key-value data                       |
| Set      | `set`        | `{10, 20, 30}`         | Unique values                        |
| Binary   | `bytes`      | `b"Hello"`             | Binary/network/file data             |
| Binary   | `bytearray`  | `bytearray(b"Hello")`  | Mutable binary data                  |
| Binary   | `memoryview` | `memoryview(b"Hello")` | Efficient binary memory access       |
| None     | `NoneType`   | `result = None`        | No value / empty result              |



## how to input data using Python

```py
# 1. Basic Input in Python

variable = input("Enter something: ");

name = input("Enter your name: ")
print("Hello", name)

# 2. Input as Number (int / float)

age = int(input("Enter your age: "))
print("Your age is:", age)

salary = float(input("Enter your salary: "))
print("Salary:", salary)

# 3. Taking Multiple Inputs

a, b = input("Enter two numbers: ").split()
print(a, b)

a, b = map(int, input("Enter two numbers: ").split())
print(a + b)

# 4. Input in a List

numbers = list(map(int, input("Enter numbers: ").split()))
print(numbers)

```












