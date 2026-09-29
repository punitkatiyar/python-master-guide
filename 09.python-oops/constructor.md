## Constructor (init)

```py
class Student: 

    def __init__(self):
        print(self)
        print("Constructor Called")
app = Student()
```

## Constructor with Parameters

```py
class Student: 
    def __init__(self,fullName):
        self.name=fullName
        print(self)
        print("Constructor Called")

app = Student("Punit")

print(app.name)
```

## self Keyword

```py
class Student:

    def __init__(self,name):
        self.name = name

s = Student("Punit")

print(s.name)
```

## Instance Variable

```py
class Student:

    def __init__(self,name):
        self.name = name

s1 = Student("Rahul")
s2 = Student("Amit")

print(s1.name)
print(s2.name)

```




