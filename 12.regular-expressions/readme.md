# Regular Expressions (Regex) in Python

**Regular Expressions, commonly called Regex, are patterns used to search, match, validate, extract, replace, and manipulate text.** 

**Python provides Regex support through the built-in re module.**

```py
import re

text = "My email is punit@example.com"

result = re.findall(r"\w+@\w+\.\w+", text)

print(result)

```
