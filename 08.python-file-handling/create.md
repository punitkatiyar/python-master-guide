# file Handling 

## Use Case

- Employee reports
- Student reports
- Invoice files
- Attendance reports
- Application logs
- Expense reports
- Customer records



| Mode   | Description                       |
| ------ | --------------------------------- |
| `"r"`  | Read only (file must exist)       |
| `"w"`  | Write (create or overwrite)       |
| `"a"`  | Append (create if not exists)     |
| `"x"`  | Create new file (fails if exists) |
| `"rb"` | Read binary                       |
| `"wb"` | Write binary                      |

## Create File 

```py
file = open("example.txt", "w")
file.close()
```

## Create a file and write text

- The with statement automatically closes the file when you're done.

```py
with open("example.txt", "w") as file:
    file.write("Hello, World!")
```

## Append text to an existing file

```py
with open("example.txt", "a") as file:
    file.write("\nThis is a new line.")
```

## Create a file only if it doesn't exist

```py
with open("example.txt", "x") as file:
    file.write("New file created!")
```
## Example

```py
student_name = "Rahul"
age = 21
course = "Python"
marks = 85

with open("student_report.txt", "w") as file:
    file.write("===== STUDENT REPORT =====\n")
    file.write(f"Name: {student_name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Course: {course}\n")
    file.write(f"Marks: {marks}\n")

print("Student report created successfully!")
```

## Example : List

```py
students = [
    ("Rahul", 85),
    ("Priya", 92),
    ("Amit", 78)
]

with open("students.txt", "w") as file:
    for name, marks in students:
        file.write(f"Name: {name}, Marks: {marks}\n")

print("Student data saved!")
```


