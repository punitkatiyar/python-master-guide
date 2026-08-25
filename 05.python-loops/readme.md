# Python Loops

**A loop in Python is used to execute a block of code repeatedly until a condition becomes false or all items in a sequence have been processed and Python provides two types of loops**

> for loop

> while loop

| Feature               | for Loop                 | while Loop                        |
| --------------------- | ------------------------ | --------------------------------- |
| Best For              | Iterating over sequences | Running until a condition changes |
| Iterations            | Usually fixed            | Usually unknown                   |
| Risk of Infinite Loop | Low                      | High if condition never changes   |
| Example               | List, tuple, string      | Login, game loop, ATM             |

## The Python range() 

**function is used to generate a sequence of numbers, most commonly with for loops.**

| Parameter | Meaning                     | Default  |
| --------- | --------------------------- | -------- |
| `start`   | Starting number             | `0`      |
| `stop`    | Ending limit (not included) | Required |
| `step`    | Difference between numbers  | `1`      |






## range(stop)

```python
for num in range(5):
    print(num)
```

## range(start, stop)

```python
for num in range(1,5):
    print(num)
```

### range(start, stop, step)

```python
for num in range(1,10,2):
    print(num)
```
## Using a Negative Step : Countdown

```python
for i in range(10, 0, -1):
    print(i)

for i in range(5, 0, -1):
    print(i)

print("Start!")
```
## Converting range() to a List

```python
numbers = list(range(5))
print(numbers)

numbers = list(range(2, 10, 2))
print(numbers)
```

## range() with Lists

```python
students = ["Rahul", "Ravi", "Rohit"]

for i in range(len(students)):
    print(i, students[i])
```

## range() with len()

```python

languages = ["Python", "JavaScript", "Java", "C++"]
for i in range(len(languages)):
    print(f"{i}: {languages[i]}")
```









