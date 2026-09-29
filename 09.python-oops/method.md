```py
class Student:

    def __init__(self,name):
        self.name = name

    def display(self):
        print(self.name)

s = Student("Rahul")
s.display()
```


```py
class Student:

    school = "ABC"

    @classmethod
    def get_school(cls):
        print(cls.school)

Student.get_school()
```


