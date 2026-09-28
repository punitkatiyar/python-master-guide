# Constructor (init)

```py
class Student: 

    def __init__(self):
        print(self)
        print("Constructor Called")
app = Student()
```


```
class Student: 
    def __init__(self,fullName):
        self.name=fullName
        print(self)
        print("Constructor Called")

app = Student("Punit")

print(app.name)
```
