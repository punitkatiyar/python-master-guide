# Polymorphism 

> The same interface or method name can behave differently depending on the object.

```py
class Dog:

    def sound(self):
        print("Bark")


class Cat:

    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```


