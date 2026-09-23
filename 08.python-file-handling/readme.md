# Python File Handling

> File handling means working with files stored on your computer.

```py
Create
  ↓
Open
  ↓
Read / Write / Append
  ↓
Update
  ↓
Close
```
**Python file handling is used to create, read, write, update, search, copy, move, and delete files and folders. It is especially useful for automation, data processing, logging, configuration management, and real-world applications.**

## Creating A File 

- create a file using the built-in open() function.

> **file = open("filename.txt", "mode")**

| Mode | Meaning         | If file doesn't exist  |
| ---- | --------------- | ---------------------- |
| `r`  | Read            | Error                  |
| `w`  | Write           | Creates file           |
| `a`  | Append          | Creates file           |
| `x`  | Create new file | Error if exists        |
| `r+` | Read + Write    | Error                  |
| `w+` | Write + Read    | Creates/overwrites     |
| `a+` | Append + Read   | Creates                |
| `b`  | Binary mode     | Used with another mode |
| `t`  | Text mode       | Default                |


- Always close a manually opened file:

# 

# Question 1: OS Module

> How many built-in functions and features does the Python os module provide?

# Question 2: File Handling with Multiple Python Modules

> Create 10 different Python files (.py) containing user-defined functions according to the following requirements:

> The functions should follow this distribution:

> 4 files should contain functions that use loops (for or while).

> 3 files should contain functions that use if-else statements.

> 3 files can contain functions of your choice (e.g., string operations, mathematical calculations, list operations, recursion, etc.).

> Every file must use  four major Python data types:

- List
- Dictionary
- Set
- Tuple

> Create a main.py file that:
> Opens each Python file using file handling (open()).

```
Python File Handling
│
├── 1. What is File Handling?
├── 2. File Types
├── 3. Opening Files
├── 4. Reading Files
├── 5. Writing Files
├── 6. Appending Data
├── 7. File Modes
├── 8. Working with Paths
├── 9. Using with Statement
├── 10. File Methods
├── 11. Binary Files
├── 12. CSV Files
├── 13. JSON Files
├── 14. Exception Handling
├── 15. File & Directory Operations
├── 16. Temporary Files
├── 17. Large File Processing
├── 18. Best Practices
```
