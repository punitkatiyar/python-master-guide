# Working with Directories

## Create directory:

```py
# method 1
import os
os.mkdir("reports")

# method 2
from pathlib import Path
Path("reports").mkdir()
```
## Create nested directories:
```py

Path("data/2026/reports").mkdir(parents=True, exist_ok=True)

```

## List Files in a Directory

```py
from pathlib import Path
folder = Path(".")

for file in folder.iterdir():
    print(file)

```

## Delete a Folder

```py
import os
os.rmdir("reports")
```



