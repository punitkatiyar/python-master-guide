# Python set datatype

**A set in Python is a collection used to store unique values. It is especially useful when you need to remove duplicates, perform mathematical set operations, or quickly check whether an item exists.**

## 1. What is a Set?

- Stores only unique values
- Does not maintain insertion order (do not rely on order)
- Is mutable (you can add/remove elements)
- Cannot contain mutable objects like lists or dictionaries
- Uses curly braces {} or the set() constructor

```
SET
 │
 ├── Create
 │    ├── {}
 │    └── set()
 │
 ├── Add / Remove
 │    ├── add()
 │    ├── update()
 │    ├── remove()
 │    ├── discard()
 │    ├── pop()
 │    └── clear()
 │
 ├── Operations
 │    ├── Union          |
 │    ├── Intersection   &
 │    ├── Difference     -
 │    └── Symmetric      ^
 │
 ├── Relationships
 │    ├── Subset
 │    ├── Superset
 │    └── Disjoint
 │
 ├── Comprehension
 │
 ├── Duplicate Removal
 │
 └── Advanced
      ├── Hashing
      ├── frozenset
      └── Set as dictionary key
```

## Set vs List vs Tuple vs Dictionary


| Feature         | List       | Tuple      | Set         | Dictionary     |
| --------------- | ---------- | ---------- | ----------- | -------------- |
| Syntax          | `[]`       | `()`       | `{}`        | `{key:value}`  |
| Ordered         | ✅          | ✅          | ❌           | ✅*             |
| Mutable         | ✅          | ❌          | ✅           | ✅              |
| Duplicates      | ✅          | ✅          | ❌           | Keys ❌         |
| Indexing        | ✅          | ✅          | ❌           | By key         |
| Fast membership | Moderate   | Moderate   | ✅           | ✅              |
| Main use        | Collection | Fixed data | Unique data | Key-value data |



