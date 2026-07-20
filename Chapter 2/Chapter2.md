# Chapter 2: Strings & Conditional Statements

## 📋 Overview
This chapter covers Python's **string** data type in depth — indexing, slicing, and built-in string functions — followed by **conditional statements**, which let programs make decisions and execute different code paths based on conditions.

## 🎯 Learning Objectives
By the end of this chapter, you will be able to:
- Perform basic string operations like concatenation and length calculation
- Access individual characters using indexing
- Extract substrings using slicing (including negative indices)
- Use built-in string methods to manipulate text
- Write conditional logic using `if`, `elif`, and `else`

---

## 📚 Topics Covered

### 1. Strings
A string is a data type that stores a sequence of characters.

**Basic Operations**
```python
"hello" + "world"    # "helloworld"  (concatenation)
len(str)              # length of a string
```

### 2. Indexing
Each character in a string has a positional index, starting from 0.

```python
str = "Apna_College"
#      0123456789...

str[0]     # 'A'
str[1]     # 'p'
str[0] = 'B'   # ❌ Not allowed — strings are immutable
```

### 3. Slicing
Used to access a portion (substring) of a string.

```python
str[starting_idx : ending_idx]   # ending_idx is NOT included

str = "ApnaCollege"
str[1:4]      # "pna"
str[:4]       # same as str[0:4]
str[1:]       # same as str[1:len(str)]
```

**Negative Indexing**
```python
str = "Apple"
#      -5-4-3-2-1

str[-3:-1]    # "pl"
```

### 4. String Functions
```python
str = "I am a coder."

str.endsWith("er.")     # True if string ends with substring
str.capitalize()        # Capitalizes the first character
str.replace(old, new)   # Replaces all occurrences of old with new
str.find(word)          # Returns the first index of the first occurrence
str.count("am")         # Counts occurrences of a substring
```

---

### 5. Conditional Statements
Used to execute code blocks based on whether a condition is `True` or `False`.

**Syntax**
```python
if condition:
    Statement1
elif condition:
    Statement2
else:
    StatementN
```

**Example — Grading Students Based on Marks**
```python
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"
```

---

## 💻 Practice Exercises

### Strings
1. Write a program to input the user's first name & print its length.
2. Write a program to find the number of occurrences of `'$'` in a string.

### Conditional Statements
3. Write a program to check if a number entered by the user is odd or even.
4. Write a program to find the greatest of 3 numbers entered by the user.
5. Write a program to check if a number is a multiple of 7 or not.

---

## 🔑 Key Takeaways
- Strings are **immutable** in Python — individual characters cannot be reassigned.
- Slicing follows the `[start:end]` convention where `end` is exclusive.
- `if-elif-else` chains are evaluated top to bottom, and only the first matching block runs.