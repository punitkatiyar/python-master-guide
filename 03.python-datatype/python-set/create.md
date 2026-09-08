# Create set

## Empty set

```py
my_set = set()

print(type(my_set))
```

## Normal set

```py
numbers = {10, 20, 30, 40}

print(numbers)

// {40, 10, 20, 30}
```

## Duplicate values

```py
numbers = {10, 20, 20, 30, 30, 40}

print(numbers)

// {10, 20, 30, 40}
```

## Creating a Set from a List 🎯 Use case: Remove duplicates

```py
numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = set(numbers)

print(unique_numbers)

// {40, 10, 20, 30}

courses = ["html", "css", "html", "Python", "css"]

unique_courses = list(set(courses))

print(unique_courses)

// ['Python', 'css', 'html']

```

