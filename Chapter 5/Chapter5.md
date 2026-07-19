# Chapter 5: Loops in Python

A complete guide to repetition and iteration control in Python.

---

## 📖 Overview
Loops let you execute a block of code repeatedly. Python provides two main types:
- **`while` loop** — repeats as long as a condition is `True`
- **`for` loop** — iterates over a sequence (list, string, range, etc.)

---

## 🔁 While Loop

### Syntax
```python
while condition:
    # code block
```

### Example
```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

### Key Points
- The condition is checked **before** each iteration.
- You must update the variable inside the loop, or it becomes an **infinite loop**.
- Useful when the number of iterations isn't known in advance (e.g., waiting for valid user input).

### While Loop with else
```python
while condition:
    # code
else:
    # runs once when condition becomes False (not on break)
```

---

## 🔂 For Loop

### Syntax
```python
for item in sequence:
    # code block
```

### Example — Iterating a List
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Example — Iterating a String
```python
for char in "Python":
    print(char)
```

### The `range()` Function
| Form | Meaning |
|---|---|
| `range(stop)` | 0 to stop-1 |
| `range(start, stop)` | start to stop-1 |
| `range(start, stop, step)` | start to stop-1, incrementing by step |

```python
for i in range(1, 10, 2):
    print(i)   # 1 3 5 7 9
```

### Key Points
- Best used when the number of iterations is known or based on a sequence's length.
- Can loop directly over lists, tuples, strings, dictionaries, and sets.

---

## ⛔ Loop Control Statements

| Statement | Effect |
|---|---|
| `break` | exits the loop immediately |
| `continue` | skips current iteration, moves to next |
| `pass` | does nothing — placeholder for empty blocks |

```python
for i in range(1, 10):
    if i == 5:
        break        # stops loop entirely at 5
    if i % 2 == 0:
        continue     # skips even numbers
    print(i)
```

---

## 🔄 Nested Loops
- A loop inside another loop — the inner loop completes all its iterations for every single iteration of the outer loop.

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```

**Common use cases:** printing patterns, working with grids/matrices, comparing pairs of items.

---

## 🧩 Common Loop Patterns
- **Counting/Accumulating:** summing values, counting occurrences
- **Searching:** finding an item in a list, checking membership
- **Pattern printing:** stars, numbers, pyramids using nested loops
- **Iterating with index:** using `enumerate()` to get both index and value

```python
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)
```

---

## 📊 While vs For — Quick Comparison
| Feature | while loop | for loop |
|---|---|---|
| Best for | Unknown number of iterations | Known sequence/range |
| Condition-based | Yes | No (iterates over items) |
| Risk of infinite loop | Higher (if condition never False) | Lower |
| Common use | Waiting/validating input | Iterating collections |

---

## ✅ Chapter Checklist
- [ ] Write and control a `while` loop
- [ ] Write and control a `for` loop
- [ ] Use `range()` with start, stop, and step
- [ ] Apply `break`, `continue`, and `pass` correctly
- [ ] Build nested loops for patterns/grids
- [ ] Use `enumerate()` while looping