# Chapter 5: Loops in Python

## 📋 Overview
This chapter covers Python's looping constructs — `while` and `for` — used to repeat instructions, along with loop-control tools like `break`, `continue`, `range()`, and the `pass` statement.

## 🎯 Learning Objectives
By the end of this chapter, you will be able to:
- Write `while` loops to repeat a block of code based on a condition
- Write `for` loops to iterate over sequences (lists, strings, tuples)
- Use `for...else` to detect whether a loop completed without a `break`
- Use `break` and `continue` to control loop execution
- Generate number sequences using `range()`
- Use `pass` as a placeholder statement

---

## 📚 Topics Covered

### 1. `while` Loops
Loops are used to repeat instructions.

```python
while condition:
    # some work
```

### 2. `for` Loops
Used for sequential traversal — of lists, strings, tuples, etc.

```python
list = [1, 2, 3]

for el in list:
    print(el)
```

### 3. `for` Loop with `else`
The `else` block executes only if the loop completes without hitting a `break`.

```python
for el in list:
    print(el)
else:
    print("END")
```
> 💡 The `else` block does **not** execute if `break` is used inside the loop.

### 4. Break & Continue
- **`break`**: Terminates the loop immediately when encountered.
- **`continue`**: Terminates the current iteration and continues with the next one.

```python
for el in list:
    if el == target:
        break        # stop searching once found

for num in range(1, 20):
    if num % 3 == 0:
        continue      # skip multiples of 3
    print(num)
```

### 5. `range()`
Returns a sequence of numbers, starting from 0 by default, incrementing by 1 by default, and stopping **before** the specified number.

```python
range(start?, stop, step?)

for el in range(5):
    print(el)          # 0 1 2 3 4

for el in range(1, 5):
    print(el)          # 1 2 3 4

for el in range(1, 5, 2):
    print(el)          # 1 3
```

### 6. `pass` Statement
A null statement that does nothing — used as a placeholder for future code (commonly in exception handling).

```python
for el in range(10):
    pass
```

---

## 💻 Practice Exercises

### Using `while` / general loops
1. Print numbers from 1 to 100.
2. Print numbers from 100 to 1.
3. Print the multiplication table of a number `n`.
4. Print the elements of the list `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` using a loop.
5. Search for a number `x` in the tuple `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` using a loop.

### Using `for`
6. Print the elements of `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]` using `for`.
7. Search for a number `x` in the tuple above using `for`.

### Using `for` & `range()`
8. Print numbers from 1 to 100.
9. Print numbers from 100 to 1.
10. Print the multiplication table of a number `n`.

### Break & Continue
11. Take the search example above and stop the search once the element is found.
12. Print all numbers in a range, excluding multiples of 3.

### While vs For
13. WAP to find the sum of the first `n` numbers (using `while`).
14. WAP to find the factorial of the first `n` numbers (using `for`).

---

## 🔑 Key Takeaways
- Use `while` when the number of iterations is unknown ahead of time; use `for` when iterating over a known sequence or range.
- `break` exits the loop entirely; `continue` skips only the current iteration.
- `range(start, stop, step)` never includes the `stop` value.