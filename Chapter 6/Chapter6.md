# Chapter 6: Functions & Recursion in Python

A complete guide to writing reusable code blocks and solving problems recursively.

---

## 📖 Overview
This chapter covers:
- **Functions** — reusable blocks of code that perform a specific task
- **Recursion** — a function calling itself to solve smaller sub-problems

---

## 🧩 Functions

### Defining & Calling a Function
```python
def greet():
    print("Hello!")

greet()   # calling the function
```

### Parameters & Arguments
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ali")   # "Ali" is the argument passed to parameter "name"
```

### Default Parameter Values
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Hello, Guest!
greet("Sara")    # Hello, Sara!
```

### Return Values
```python
def add(a, b):
    return a + b

result = add(3, 4)   # result = 7
```
- `return` sends a value back to the caller and **ends the function**.
- `print()` just displays output — it doesn't give the function a usable value.

### Types of Arguments
| Type | Example | Description |
|---|---|---|
| Positional | `add(3, 4)` | matched by order |
| Keyword | `add(a=3, b=4)` | matched by name |
| Default | `def greet(name="Guest")` | used if no value is passed |
| Variable-length (`*args`) | `def total(*nums)` | accepts any number of positional args |
| Variable-length (`**kwargs`) | `def info(**data)` | accepts any number of keyword args |

```python
def total(*nums):
    return sum(nums)

total(1, 2, 3, 4)   # 10
```

### Variable Scope
- **Local variable:** defined inside a function, accessible only within it.
- **Global variable:** defined outside all functions, accessible everywhere.
- Use the `global` keyword to modify a global variable from inside a function.

```python
x = 10   # global

def show():
    x = 5   # local, different from global x
    print(x)

show()       # 5
print(x)     # 10
```

---

## 🔁 Recursion

### What is Recursion?
- A function that calls **itself** to break a problem into smaller sub-problems.
- Every recursive function needs:
  1. **Base case** — the condition that stops the recursion.
  2. **Recursive case** — where the function calls itself with a smaller input.

### Example — Factorial
```python
def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)   # recursive case

print(factorial(5))   # 120
```

### Example — Fibonacci
```python
def fibonacci(n):
    if n <= 1:           # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

### Key Points
- Without a proper base case, recursion leads to **infinite calls** and a `RecursionError`.
- Each recursive call is added to the **call stack** until the base case is reached.
- Recursion is elegant for problems with a naturally repeating structure (factorials, Fibonacci, tree/graph traversal).

---

## 📊 Iterative vs Recursive — Quick Comparison
| Feature | Iterative (loops) | Recursive |
|---|---|---|
| Uses | loops (`for`/`while`) | function calling itself |
| Memory usage | lower | higher (call stack) |
| Readability | can get complex for nested problems | often cleaner for repetitive/tree-like problems |
| Risk | infinite loop | infinite recursion / stack overflow |
| Base requirement | loop condition | base case |

---

## ✅ Chapter Checklist
- [ ] Define and call functions with parameters
- [ ] Use default parameter values
- [ ] Understand `return` vs `print()`
- [ ] Use `*args` and `**kwargs`
- [ ] Understand local vs global scope
- [ ] Write a recursive function with a proper base case
- [ ] Trace recursive calls (factorial/Fibonacci) step by step