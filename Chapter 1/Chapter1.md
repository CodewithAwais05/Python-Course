# Chapter 1: Python Basics

## 📋 Overview
This chapter introduces the Python programming language — what it is, how programs are executed, and the foundational building blocks every Python program relies on: variables, data types, keywords, operators, type conversion, and user input.

## 🎯 Learning Objectives
By the end of this chapter, you will be able to:
- Explain what programming and Python are, and how code gets translated into machine instructions
- Write and run your first Python program
- Understand the Python character set and identifier naming rules
- Declare variables and identify Python's core data types
- Use arithmetic, relational, assignment, and logical operators
- Differentiate between type conversion and type casting
- Accept input from a user via the keyboard

---

## 📚 Topics Covered

### 1. Programming & Translators
A program written in a high-level language (like Python) must be translated into machine code before a computer can execute it. This is done by a **Compiler** or an **Interpreter**.

```
Code (Python) → Translator (Compiler/Interpreter) → Machine Code → Machine
```

### 2. What is Python?
- Simple & easy to learn
- Free & Open Source
- High-level language
- Developed by **Guido van Rossum**
- Portable (runs across platforms)

### 3. Our First Program
```python
print("Hello World")
```

### 4. Python Character Set
| Category | Examples |
|---|---|
| Letters | A–Z, a–z |
| Digits | 0–9 |
| Special Symbols | + - * / etc. |
| Whitespaces | space, tab, carriage return, newline, formfeed |
| Other characters | All ASCII & Unicode characters |

### 5. Variables
A variable is a name given to a memory location in a program.

```python
name = "Shradha"
age = 23
price = 25.99
```

### 6. Rules for Identifiers
1. Can be a combination of uppercase/lowercase letters, digits, or underscore (`_`).
2. Cannot start with a digit (`variable1` ✅, `1variable` ❌).
3. Cannot contain special symbols like `!`, `#`, `@`, `%`, `$`.
4. Can be of any length.

### 7. Data Types
- **Integer**
- **String**
- **Float**
- **Boolean**
- **None**

```python
print(type(age))          # <class 'int'>
print(type(pi))           # <class 'float'>
print(type(complex_num))  # <class 'complex'>
print(type(A))            # <class 'bool'>
print(type(name))         # <class 'str'>
```

### 8. Keywords
Keywords are reserved words in Python and cannot be used as identifiers:

`and`, `as`, `assert`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `False`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `None`, `not`, `or`, `pass`, `raise`, `return`, `True`, `try`, `while`, `with`, `yield`

> ⚠️ Note: `True`, `False`, and `None` must be capitalized.

### 9. Comments in Python
```python
# Single Line Comment

"""
Multi Line
Comment
"""
```

### 10. Types of Operators
| Category | Operators |
|---|---|
| Arithmetic | `+` `-` `*` `/` `%` `**` |
| Relational/Comparison | `==` `!=` `>` `<` `>=` `<=` |
| Assignment | `=` `+=` `-=` `*=` `/=` `%=` `**=` |
| Logical | `not` `and` `or` |

### 11. Type Conversion
Python automatically converts compatible types during operations (implicit conversion).
```python
a, b = 1, 2.0
sum = a + b     # Works fine — int converted to float

a, b = 1, "2"
sum = a + b     # Error! Incompatible types
```

### 12. Type Casting
Explicitly converting one data type to another using built-in functions.
```python
a, b = 1, "2"
c = int(b)
sum = a + c     # Works — "2" cast to int
```

| Function | Description |
|---|---|
| `int(y [,base])` | Converts `y` to an integer |
| `float(y)` | Converts `y` to a floating-point number |
| `complex(real [,imag])` | Creates a complex number |
| `str(y)` | Converts `y` to a string |
| `tuple(y)` | Converts `y` to a tuple |
| `list(y)` | Converts `y` to a list |
| `set(y)` | Converts `y` to a set |
| `dict(y)` | Creates a dictionary from `y` |
| `ord(y)` | Converts a character to an integer |
| `hex(y)` | Converts an integer to a hexadecimal string |
| `oct(y)` | Converts an integer to an octal string |

### 13. Input in Python
```python
input()             # Result is always a string (str)
int(input())         # Cast input to int
float(input())       # Cast input to float
```

---

## 💻 Practice Exercises
1. Write a program to input 2 numbers & print their sum.
2. WAP to input the side of a square & print its area.
3. WAP to input 2 floating point numbers & print their average.
4. WAP to input 2 int numbers, `a` and `b`. Print `True` if `a` is greater than or equal to `b`, otherwise print `False`.

---

## 🔑 Key Takeaways
- Python code is translated to machine code via an interpreter.
- Variables don't need explicit type declarations — Python infers types dynamically.
- `input()` always returns a string; cast it explicitly when numeric input is needed.