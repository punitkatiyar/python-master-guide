## Email Validation

```py
import re

email = "punit@example.com"

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
```

## Mobile Number Validation

```py
import re

phone = "9876543210"

pattern = r"^[6-9]\d{9}$"

if re.match(pattern, phone):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
```

## Password Validation

- minimum 8 characters
- uppercase letter
- lowercase letter
- digit
- special character

```py
import re

password = "Python@123"

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

if re.match(pattern, password):
    print("Strong password")
else:
    print("Weak password")

```

## Extract Hashtags

```py
import re

text = "Learning #Python #Django #Programming"

hashtags = re.findall(r"#\w+", text)

print(hashtags)

# ['#Python', '#Django', '#Programming']

```
