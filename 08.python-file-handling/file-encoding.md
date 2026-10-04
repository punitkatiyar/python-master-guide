# File Encoding

## Read File
```py
with open("data.txt", "r", encoding="utf-8") as file:
    data = file.read()

print(data)
```

## Write File
```py
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("नमस्ते Python")
```
