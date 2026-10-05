# Multithreading in Python

**Multithreading in Python allows a program to run multiple threads concurrently within the same process. It is especially useful for I/O-bound tasks such as downloading files, making API requests, reading files, database operations, and handling multiple client requests.**

> Important: Python's standard CPython implementation has the GIL (Global Interpreter Lock), so multithreading generally does not provide true parallel execution for CPU-heavy Python code. For CPU-bound work, multiprocessing or other approaches are usually more appropriate.

## What is a Thread?

**A thread is a lightweight unit of execution inside a process.**


- Sequential execution
```py
Task A → Task B → Task C → Task D
```

- Multithreading
```
        ┌── Task A
Program ├── Task B
        ├── Task C
        └── Task D
```
