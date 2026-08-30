# Python List dataType and function :

```
Index:    0       1       2
        ┌─────┬─────┬─────┐
Value:  │  A  │  B  │  C  │
        └─────┴─────┴─────┘
```


# List Basic 

```
start=[]
print(start)
print(type(start));

nums=[1,2,3,4,5]
print(nums)
print(nums[0]+nums[4])


info=["ducat",2026,6.5,True]
print(type(info[0]))

//nested 

mix=[["user1",9],["user2",8],["user3",7]]

print(mix)
print(mix[0])
print(mix[0][0])
```




## Real-world applications of lists

```py
cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print("Cart:", cart)

cart.remove("Mouse")

print("Updated Cart:", cart)

print("Total Items:", len(cart))

```

```py
Cart: ['Laptop', 'Mouse', 'Keyboard']
Updated Cart: ['Laptop', 'Keyboard']
Total Items: 2
```



```
List
 │
 ├── Shopping Cart
 ├── Student Marks
 ├── Product Catalog
 ├── To-Do Tasks
 ├── Employee Names
 ├── Order Items
 ├── API Response Data
 └── Database Records
```

## Shallow Copy vs Deep Copy in Python Lists

**When working with Python lists, copying means creating another list based on an existing list. The important difference is what happens to nested objects.**

## Shallow Copy : A shallow copy creates a new outer list, but nested objects are still shared.

```py
mylist = [[10, 20], [30, 40]]

copy_list = mylist.copy()

copy_list[0][0] = 111

print(mylist)

print(copy_list)

[[111, 20], [30, 40]]
[[111, 20], [30, 40]]

```

## Deep Copy : A deep copy creates a new outer list and new copies of nested objects.


```py 
import copy

original = [[10, 20], [30, 40]]

copy_list = copy.deepcopy(original)

copy_list[0][0] = 999

print(original)
print(copy_list)

[[10, 20], [30, 40]]
[[999, 20], [30, 40]]
```



















