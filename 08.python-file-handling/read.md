## Reading a File

```py
file = open("students.txt", "r")
data = file.read()
print(data)
file.close()
```

## Reading Limited Characters

```py
file = open("students.txt", "r")
data = file.read(5)
print(data)
file.close()

```

## readline() : Reads one line.

```py
file = open("students.txt", "r")
line = file.readline()
print(line)
file.close()

# read multiple line

file = open("students.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
```

## readlines() : Returns all lines as a list.

```py
file = open("students.txt", "r")
lines = file.readlines()
print(lines)
file.close()
```

## Reading a File Using a Loop

- This is often better for large files.
- removes extra whitespace and the newline character \n.

```py
file = open("students.txt", "r")

for line in file:
    print(line.strip())

file.close()
```





