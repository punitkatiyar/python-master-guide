# Python dictionary 

**A dictionary (dict) in Python is used to store data in key-value pairs.**

- Word : key
- Meaning : value

```python
student = {
    "name": "user",
    "year": 2026,
    "course": "Python"
}
```

## When should you use a Dictionary?

- Store information with labels
- Quickly find a value using a key
- Represent a real-world object
- Store configuration/settings
- Work with JSON/API data
- Count items
- Create lookup tables
- Group related information

## Features of Dictionary

- Mutable (can be modified)
- Keys are unique
- Values can be duplicate
- Stores multiple data types
- Fast searching using keys

## Creating Dictionary

```python
# method 1
student = {
    "name": "user",
    "year": 2026
}
# method 2
student = dict(name="Amit", year=2026)

print(student)

# method 3
student = dict([
    ("name", "user"),
    ("year", 2026)
])

print(student)
```
## Accessing Values

```py
student = {
    "name": "user",
    "year": 2026
}

print(student["name"])

# method
print(student.get("age"))

# default value

print(student.get("city", "Not Found"))

```

## add item

```
student["course"] = "python"

```

## Updating Dictionary

```py
student = {
    "name": "ducat",
    "course": "java"
}

student["course"] = "python"

print(student)

# method

student.update({
    "age": 21,
    "city": "Kanpur"
})

```

## Remove

```py

student.pop("age")

## Removes the last inserted key-value pair.
student.popitem()


## del

del student["name"]

## clear()

student.clear()

```





