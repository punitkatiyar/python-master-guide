# Inheritance :: Reuse existing class functionality.



## Types of Inheritance

### Single Inheritance
```
A
|
B
```
```py
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass

d = Dog()

d.sound()

```
### Multilevel Inheritance
```
A
|
B
|
C
```
```py
class Animal:
    pass


class Dog(Animal):
    pass


class Puppy(Dog):
    pass
```



### Multiple Inheritance
```
 A    B
  \  /
   C
```
```py
class Camera:

    def take_photo(self):
        print("Taking photo")

class Phone:

    def make_call(self):
        print("Making call")

class Smartphone(Camera, Phone):
    pass


phone = Smartphone()

phone.take_photo()
phone.make_call()
```
### Hierarchical Inheritance
```
    A
   / \
  B   C
```
```py
class Animal:
    def eat(self):
        print("Eating")


class Dog(Animal):
    pass


class Cat(Animal):
    pass
```

