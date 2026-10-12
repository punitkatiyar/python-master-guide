# Real-World Use Case: Bank Withdrawal

> Exception handling is very useful in banking applications.

```py
balance = 10000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if amount > balance:
        raise ValueError("Insufficient balance.")

    balance -= amount

except ValueError as e:
    print("Transaction failed:", e)

else:
    print("Withdrawal successful.")
    print("Remaining balance:", balance)

finally:
    print("Thank you for using our banking service.")
```
