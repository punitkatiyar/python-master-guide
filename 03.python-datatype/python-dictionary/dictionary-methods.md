# Methods List


| Method         | Description                      |
| -------------- | -------------------------------- |
| `get()`        | Returns value of key             |
| `keys()`       | Returns all keys                 |
| `values()`     | Returns all values               |
| `items()`      | Returns key-value pairs          |
| `update()`     | Updates dictionary               |
| `pop()`        | Removes specified key            |
| `popitem()`    | Removes last item                |
| `clear()`      | Removes all items                |
| `copy()`       | Creates copy                     |
| `setdefault()` | Returns value or inserts default |
| `fromkeys()`   | Creates dictionary from keys     |


## key() : values()  Returns all keys and value

```python
student = {
    "name": "user",
    "year": 2026
}

print(student.keys())

print(student.values())



# dict_keys(['name', 'year'])
# dict_values(['user', 2026])
```

## items() : Returns key-value pairs 

```py
print(student.items())

# dict_items([('name', 'user'), ('year', 2026)])
```

## copy() 

```py
student = {
    "name": "punit",
    "course": "python"
}

new_student = student.copy()

print(new_student)

```

## Nested Dictionary

```
students = {
    "101": {
        "name": "Rahul",
        "age": 21
    },
    "102": {
        "name": "Amit",
        "age": 22
    }
}

print(students["101"]["name"])
```

## Dictionary Inside List

```py
students = [
    {"name": "Rahul", "marks": 90},
    {"name": "Amit", "marks": 85},
    {"name": "Priya", "marks": 95}
]

for student in students:
    print(student["name"], student["marks"])
```

## List Inside Dictionary

```py
student = {
    "name": "Rahul",
    "subjects": [
        "Python",
        "Java",
        "React"
    ]
}

print(student["subjects"][1])
```

## Merging Dictionaries

```py
dict1 = {
    "a": 1
}

dict2 = {
    "b": 2
}

result = dict1 | dict2

print(result)

```





















