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









