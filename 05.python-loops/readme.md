# Python Loops

| Feature               | for Loop                 | while Loop                        |
| --------------------- | ------------------------ | --------------------------------- |
| Best For              | Iterating over sequences | Running until a condition changes |
| Iterations            | Usually fixed            | Usually unknown                   |
| Risk of Infinite Loop | Low                      | High if condition never changes   |
| Example               | List, tuple, string      | Login, game loop, ATM             |


```
lines = []
for i in range(3):
    line = input("Enter line: ")
    lines.append(line)

print(lines)
```
