# Python List dataType and function :

```
Index:    0       1       2
        ┌─────┬─────┬─────┐
Value:  │  A  │  B  │  C  │
        └─────┴─────┴─────┘
```

## List methods

| Method      | Purpose            |
| ----------- | ------------------ |
| `append()`  | Add one item       |
| `extend()`  | Add multiple items |
| `insert()`  | Add at position    |
| `remove()`  | Remove by value    |
| `pop()`     | Remove by index    |
| `clear()`   | Remove everything  |
| `index()`   | Find position      |
| `count()`   | Count occurrences  |
| `sort()`    | Sort list          |
| `reverse()` | Reverse list       |
| `copy()`    | Copy list          |

## Built-in functions

| Function      | Purpose                | Example            |
| ------------- | ---------------------- | ------------------ |
| `list()`      | Create/convert to list | `list("ABC")`      |
| `len()`       | Number of items        | `len(items)`       |
| `min()`       | Smallest value         | `min(numbers)`     |
| `max()`       | Largest value          | `max(numbers)`     |
| `sum()`       | Total                  | `sum(numbers)`     |
| `sorted()`    | Return sorted list     | `sorted(numbers)`  |
| `enumerate()` | Index + value          | `enumerate(items)` |

## Real-world applications of lists

```py
cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print("Cart:", cart)

cart.remove("Mouse")

print("Updated Cart:", cart)

print("Total Items:", len(cart))

```

```py
Cart: ['Laptop', 'Mouse', 'Keyboard']
Updated Cart: ['Laptop', 'Keyboard']
Total Items: 2
```



```
List
 │
 ├── Shopping Cart
 ├── Student Marks
 ├── Product Catalog
 ├── To-Do Tasks
 ├── Employee Names
 ├── Order Items
 ├── API Response Data
 └── Database Records
```


## Searching in a List 

1. **index() Returns the index of an item.**

```py
techs = ["java", "node", "python"]

print(techs.index("python"))
```
2. **count() Counts how many times a value occurs.**

```py
numbers = [10, 20, 10, 30, 10]

print(numbers.count(10))
```
**Use Case Example : Counting how many times a product was purchased:**

```py
orders = ["Laptop", "Mouse", "Laptop", "Keyboard", "Laptop"]

print(orders.count("Laptop"))
```

## Sorting a List

**sort()**

```py
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)

// Descending:

numbers.sort(reverse=True)
```

**sorted() creates a new sorted list without changing the original.** 

```py
numbers = [50, 10, 30]

new_numbers = sorted(numbers)

print(new_numbers)
print(numbers)

[10, 30, 50]
[50, 10, 30]
```

| `sort()`              | `sorted()`          |
| --------------------- | ------------------- |
| List method           | Built-in function   |
| Changes original list | Creates new list    |
| Returns `None`        | Returns sorted list |









