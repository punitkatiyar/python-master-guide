# List Built-in functions

| Function      | Purpose                | Example            |
| ------------- | ---------------------- | ------------------ |
| `list()`      | Create/convert to list | `list("ABC")`      |
| `len()`       | Number of items        | `len(items)`       |
| `min()`       | Smallest value         | `min(numbers)`     |
| `max()`       | Largest value          | `max(numbers)`     |
| `sum()`       | Total                  | `sum(numbers)`     |
| `sorted()`    | Return sorted list     | `sorted(numbers)`  |
| `enumerate()` | Index + value          | `enumerate(items)` |

## list()

```py
nums=list(1,2,3,4,5)

print(nums)
```



## len() : Returns the number of items.

```py
students = ["Amit", "Rahul", "ravi", "Rohit"]

print(len(students))
```


## min(), max(), sum()

```py
marks = [75, 88, 92, 65, 80]

print(min(marks)) // 65
print(max(marks)) // 92
print(sum(marks)) // 400

// Average
average = sum(marks) / len(marks)

print(average)
```

## sorted() creates a new sorted list without changing the original.

```py
numbers = [50, 10, 30]

new_numbers = sorted(numbers)

print(new_numbers)
print(numbers)

[10, 30, 50]
[50, 10, 30]
```

## enumerate() is useful when you need both index and value.

```py 
students = ["Rahul", "Amit", "Priya"]

for index, student in enumerate(students):
    print(f"Student {index + 1}: {student}")

Student 1: Rahul
Student 2: Amit
Student 3: Priya
```







