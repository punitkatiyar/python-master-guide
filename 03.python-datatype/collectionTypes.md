## Collection Data Types

## list (Array) : Ordered, mutable (changeable) collection.

**✔ Example**
```
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
```

**✔ Use Cases**

Storing multiple items, Dynamic data like cart items, API responses that return arrays.

🔹 7. tuple
✔ What is it?

Ordered, immutable collection.

✔ Example
point = (10, 20)

✔ Use Cases

Fixed data (coordinates, configuration)

Dictionary keys

Performance boost (faster than lists)

🔹 8. set
✔ What is it?

Unordered collection of unique items.

✔ Example
unique_ids = {1, 2, 3, 3, 2}
print(unique_ids)  # {1, 2, 3}

✔ Use Cases

Removing duplicates

Membership testing (in)

Mathematical operations (union, intersection)

🔹 9. dict (Dictionary)
✔ What is it?

Key-value pair collection.

✔ Example
person = {
    "name": "Punit",
    "age": 25,
    "is_student": False
}

✔ Use Cases

JSON-like structures

API data

Settings/config

Database records

🔵 Special Data Types
🔹 10. NoneType
✔ What is it?

Represents no value / empty value.

✔ Example
result = None

✔ Use Cases

Default return value

Indicating missing data

Optional function arguments

🔹 11. bytes
✔ What is it?

Immutable sequence of bytes.

✔ Example
data = b"Hello"

✔ Use Cases

Working with files (binary mode)

Network communication

Encryption

🔹 12. bytearray
✔ What is it?

Mutable version of bytes.

✔ Example
arr = bytearray(b"Hello")
arr[0] = 72

✔ Use Cases

Editing binary data

Low-level data operations

🔹 13. range
✔ What is it?

Sequence of numbers (commonly used in loops).

✔ Example
for i in range(1, 6):
    print(i)

✔ Use Cases

Loops

Creating number sequences

Indexing
