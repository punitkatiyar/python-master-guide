## search()

**looks for the first occurrence of a pattern anywhere in the string.**

```py
import re

text = "I am learning Python"

result = re.search("Python", text)

if result:
    print("Python found")
```

### Use case

- logs
- documents
- user input
- source code

## match()

**checks only from the beginning of the string.**

```py
import re

text = "Python is powerful"

result = re.match("Python", text)

print(result)

# 

text = "I love Python"

result = re.match("Python", text)

print(result)

# None

```

## findall()

**returns all matching values.**

```py
import re

text = "Python is easy. Python is powerful. Python is popular."

result = re.findall("Python", text)

print(result)

# ['Python', 'Python', 'Python']

# Extract numbers

import re

text = "I have 10 apples, 20 oranges and 30 bananas."

numbers = re.findall(r"\d+", text)

print(numbers)

# ['10', '20', '30']
```

## re.findall() with Characters

```py
import re

text = "Python Java C++ JavaScript"

result = re.findall(r"\w+", text)

print(result)

# ['Python', 'Java', 'C', 'JavaScript']
```




