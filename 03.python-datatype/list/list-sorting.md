# list sorting 

## sort()

```py

nums=[1,3,7,2,6,4,5]

// Ascending

nums.sort()

print(nums)

// Descending 

# nums.sort(reverse=True)

nums.reverse()

print(nums)
```

## sorted() creates a new sorted list without changing the original.** 

```py
numbers = [50, 10, 30]

new_numbers = sorted(numbers)

print(new_numbers)
print(numbers)

[10, 30, 50]
[50, 10, 30]
```

| `sort()`              | `sorted()`          |
| --------------------- | ------------------- |
| List method           | Built-in function   |
| Changes original list | Creates new list    |
| Returns `None`        | Returns sorted list |
