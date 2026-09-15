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
student = {
    "name": "user",
    "year": 2026
}

student = dict(name="Amit", year=2026)

print(student)

student = dict([
    ("name", "user"),
    ("year", 2026)
])

print(student)

```


