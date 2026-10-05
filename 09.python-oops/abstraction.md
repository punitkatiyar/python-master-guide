# Abstraction

**Abstraction means hiding implementation details and exposing only the necessary interface.**

**Python provides abstract classes through the abc module.**

```py
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

```

- Now child classes must implement pay()

```py
class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")
```
- Usage:
  
```py
upi = UPI()
upi.pay(500)
```
