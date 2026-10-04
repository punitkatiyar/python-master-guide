## File Pointer :: Python maintains a cursor called a file pointer.

```py
with open("data.txt", "r") as file:
    print(file.read(5))
    print(file.read(5))
```

## tell() :: Shows the current position.

```py
with open("data.txt", "r") as file:
    print(file.tell())
    file.read(5)
    print(file.tell())
```

## seek() :: Moves the pointer

```py
with open("data.txt", "r") as file:
    print(file.read(5))
    file.seek(0)
    print(file.read(5))
```
