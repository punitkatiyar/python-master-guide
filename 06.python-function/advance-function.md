# nested Function

```py
def outer():

    print("Outer")

    def inner():
        print("Inner")

    inner()

outer()

// Outer
// Inner
```

## Function Inside Function

```py
def calculate(a,b):

    def add():
        return a+b

    def multiply():
        return a*b

    print(add())
    print(multiply())

calculate(10,20)

```
## Higher Order Function

```
def greet():
    return "Hello"

def display(func):
    print(func())

display(greet)
```

## Function Returning Function

```py
def outer():

    def inner():
        print("Python")

    return inner

fun = outer()

fun()

```

## Docstring

```py
def add(a,b):
    """
    Returns addition of two numbers.
    """
    return a+b

print(add.__doc__)
```

## Type Hints

```py
def add(a:int,b:int)->int:
    return a+b

print(add(10,20))
```












