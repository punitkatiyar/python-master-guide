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

```
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

```
- Always close a manually opened file:




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
