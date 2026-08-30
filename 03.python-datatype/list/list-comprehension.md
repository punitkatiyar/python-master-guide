# List comprehension 

> it provides a compact way to create lists.

## Normal approach

```py
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)
```

## List comprehension

```py
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)
```

## With Condition

```py
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [n for n in numbers if n % 2 == 0]

print(even_numbers)
```
