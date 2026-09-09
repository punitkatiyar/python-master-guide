# Adding Elements

## add()

```py
languages = {"Python", "Java"}

languages.add("JavaScript")

print(languages)

// {'JavaScript', 'Python', 'Java'}

languages.add("Python")

print(languages)

// NameError: name 'languages' is not defined

```

## update() : Adding Multiple Elements

```py
languages = {"Python", "Java"}

languages.update(["JavaScript", "C++", "Go"])

print(languages)

// {'Java', 'C++', 'Python', 'JavaScript', 'Go'}

```

## remove()

```py
numbers = {10, 20, 30, 40}

numbers.remove(30)

print(numbers)

// {40, 10, 20}

numbers.remove(100)

// KeyError

```

## discard()

```py
numbers = {10, 20, 30}

numbers.discard(20)
numbers.discard(100)

print(numbers)

// 
```

```
| Operation    | Element exists | Element doesn't exist |
| ------------ | -------------- | --------------------- |
| `remove(x)`  | Removes        | ❌ `KeyError`          |
| `discard(x)` | Removes        | ✅ No error            |
```

## pop() : Removes and returns an arbitrary element.

```py
numbers = {10, 20, 30, 40}

value = numbers.pop()

print("Removed:", value)

print("Remaining:", numbers)

// Removed 40
// Remaining {10,20,30}
```

## clear() : Removes everything.

```py
numbers = {10, 20, 30}

numbers.clear()

print(numbers)
```











