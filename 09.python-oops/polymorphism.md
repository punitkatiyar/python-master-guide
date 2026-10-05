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

## Real-world use case

### Step 1
```py
class CreditCard:

    def pay(self, amount):
        print("Paid using credit card")


class UPI:

    def pay(self, amount):
        print("Paid using UPI")


class NetBanking:

    def pay(self, amount):
        print("Paid using net banking")

```

## Step 2

```py
def process_payment(payment_method, amount):
    payment_method.pay(amount)
```

## Step 3

```py
process_payment(CreditCard(), 5000)
process_payment(UPI(), 2000)
process_payment(NetBanking(), 3000)
```



