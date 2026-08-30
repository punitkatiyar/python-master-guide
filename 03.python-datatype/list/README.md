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












