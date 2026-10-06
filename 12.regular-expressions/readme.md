# Regular Expressions (Regex) in Python

**Regular Expressions, commonly called Regex, are patterns used to search, match, validate, extract, replace, and manipulate text.** 

**Python provides Regex support through the built-in re module.**

```py
import re
text = "My email is punit@example.com"
result = re.findall(r"\w+@\w+\.\w+", text)
print(result)
```
## Common use cases

| Use Case | Example |
|---|---|
| Email validation | `user@example.com` |
| Phone validation | `9876543210` |
| Extract numbers | Find `100`, `250`, `500` |
| Find words | Search for `"Python"` |
| Password validation | Uppercase + lowercase + number |
| URL extraction | Find website URLs |
| Log analysis | Extract IP addresses/errors |
| Data cleaning | Remove unwanted characters |
| Text replacement | Replace multiple spaces |
| Form validation | Username, PIN, email, etc. |
