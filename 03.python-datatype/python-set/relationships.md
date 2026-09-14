# Subset

## A set is a subset if all its elements exist in another set.

```py
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))

// true
```

# Superset

## A set is a superset when it contains all elements of another set.

```py
A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B))
```

# Disjoint Sets

## Two sets are disjoint when they have no common elements.

```py
A = {1, 2, 3}
B = {4, 5, 6}

print(A.isdisjoint(B))

```
