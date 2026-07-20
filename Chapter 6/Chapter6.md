# Chapter 6: Functions & Recursion

## 📋 Overview
This chapter covers how to define and use **functions** in Python — reusable blocks of code that perform a specific task — along with **default parameters** and **recursion**, where a function calls itself to solve a problem.

## 🎯 Learning Objectives
By the end of this chapter, you will be able to:
- Define and call user-defined functions
- Differentiate between built-in and user-defined functions
- Use default parameter values
- Understand and write recursive functions with proper base cases

---

## 📚 Topics Covered

### 1. Functions in Python
A function is a block of statements that performs a specific task.

```python
def func_name(param1, param2..):     # Function Definition
    # some work
    return val

func_name(arg1, arg2..)              # function call
```

**Example**
```python
def sum(a, b):
    s = a + b
    return s

print(sum(2, 3))    # 5
```

### 2. Built-in vs. User-Defined Functions
| Built-in Functions | User-Defined Functions |
|---|---|
| `print()`, `len()`, `type()`, `range()` | Functions you write yourself, e.g. `sum()` |

### 3. Default Parameters
Assigns a default value to a parameter, which is used when no argument is passed for it.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()          # Hello Guest
greet("Karan")   # Hello Karan
```

---

### 4. Recursion
When a function calls itself repeatedly, with a **base case** to stop the recursion.

**Example — Print `n` to 1 backwards**
```python
def show(n):
    if n == 0:            # base case
        return
    print(n)
    show(n - 1)
```

**Example — Factorial (`n!`)**
```python
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)
```

---

## 💻 Practice Exercises

### Functions
1. WAF (Write a Function) to print the length of a list. (`list` is the parameter)
2. WAF to print the elements of a list in a single line. (`list` is the parameter)
3. WAF to find the factorial of `n`. (`n` is the parameter)
4. WAF to convert USD to INR.

### Recursion
5. Write a recursive function to calculate the sum of the first `n` natural numbers.
6. Write a recursive function to print all elements in a list. (Hint: use `list` and `index` as parameters.)

---

## 🔑 Key Takeaways
- Functions promote code reuse and modularity — define once, call many times.
- Default parameters make function calls flexible when arguments are optional.
- Every recursive function **must** have a base case, or it will run indefinitely and cause a stack overflow.