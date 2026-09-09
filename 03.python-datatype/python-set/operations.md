## Set Union : Union combines elements from two sets.

```py

A = {1, 2, 3}
B = {3, 4, 5}

result = A | B

print(result)

// use union

result = A.union(B)

print(result)

// {1, 2, 3, 4, 5}
// {1, 2, 3, 4, 5}
```

## Set Intersection : Intersection returns elements common to both sets.

```py

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

result = A & B

print(result)

result = A.intersection(B)

print(result)

// {3, 4}

// {3, 4}

```

### Real-world use case : Find students who enrolled in both courses:

```py

python_students = {"Amit", "Rahul", "Priya", "Neha"}

java_students = {"Rahul", "Priya", "Vikas", "Raj"}

common_students = python_students & java_students

print(common_students)

// {'Rahul', 'Priya'}

```

## Set Difference : Returns elements present in the first set but not in the second.

```py
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A - B)

```

### Real-world example : Students enrolled in Python but not Java

```py
python_students = {"Amit", "Rahul", "Priya", "Neha"}

java_students = {"Rahul", "Priya", "Vikas"}

only_python = python_students - java_students

print(only_python)
```














