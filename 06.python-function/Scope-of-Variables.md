## Local Variable

```py
def demo():
    x = 10
    print(x)

demo()

```

## Global Variable

```py
x = 100

def demo():
    print(x)

demo()
```

## global Keyword

```py
count = 0

def increment():
    global count
    count += 1

increment()

print(count)

```
