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

```python 
lines = []
for i in range(3):
    line = input("Enter line: ")
    lines.append(line)

print(lines)
```
