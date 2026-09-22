# Built-in / Standard Library Modules

## math module

```py
import math

print(math.sqrt(25))
print(math.pow(2, 3))
print(math.pi)

# 5.0
# 8.0
# 3.141592653589793
```
> Use case: Mathematical calculations.

## rand

```py
import random

number = random.randint(1, 100)

print(number)
```

### Use case:

- Games
- OTP generation
- Random selection
- Simulations

## datetime

```py
from datetime import datetime

now = datetime.now()

print(now)
```

### Use case:

- Attendance systems
- Billing
- Logs
- Date/time calculations

## os

```py
import os

print(os.getcwd())
print(os.listdir())

# show single file
path=os.listdir()
print(path[0])
```

### Use case:

- File management
- Directory operations
- Operating-system interaction

## json

```py
import json

student = {
    "name": "Rohit",
    "year": 2026
}

data = json.dumps(student)

print(data)

```

> Use case: Working with APIs and JSON data.




