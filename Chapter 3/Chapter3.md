# Chapter 3: Lists & Tuples

## 📋 Overview
This chapter introduces two fundamental Python data structures used to store collections of values: **Lists** (mutable, ordered collections) and **Tuples** (immutable, ordered collections).

## 🎯 Learning Objectives
By the end of this chapter, you will be able to:
- Create and manipulate lists containing mixed data types
- Slice lists to extract sub-lists
- Use built-in list methods to add, remove, sort, and reverse elements
- Create tuples and understand why they are immutable
- Use built-in tuple methods

---

## 📚 Topics Covered

### 1. Lists in Python
A built-in data type that stores a set of values. Lists can store elements of different types (integer, float, string, etc.) and are **mutable**.

```python
marks = [87, 64, 33, 95, 76]        # marks[0], marks[1] ...
student = ["Karan", 85, "Delhi"]     # student[0], student[1] ...

student[0] = "Arjun"      # ✅ allowed — lists are mutable
len(student)              # returns length
```

### 2. List Slicing
Works the same way as string slicing.
```python
list_name[starting_idx : ending_idx]   # ending idx not included

marks = [87, 64, 33, 95, 76]
marks[1:4]      # [64, 33, 95]
marks[:4]       # same as marks[0:4]
marks[1:]       # same as marks[1:len(marks)]
marks[-3:-1]    # [33, 95]
```

### 3. List Methods
```python
list = [2, 1, 3]

list.append(4)          # [2, 1, 3, 4]  — adds element at the end
list.sort()              # [1, 2, 3]     — sorts ascending
list.sort(reverse=True)  # [3, 2, 1]     — sorts descending
list.reverse()            # [3, 1, 2]     — reverses the list
list.insert(idx, el)     # inserts element at a given index
```

```python
list = [2, 1, 3, 1]

list.remove(1)    # [2, 3, 1]   — removes first occurrence
list.pop(idx)      # removes element at given index
```

---

### 4. Tuples in Python
A built-in data type that lets us create **immutable** sequences of values.

```python
tup = (87, 64, 33, 95, 76)   # tup[0], tup[1] ...
tup[0] = 43                  # ❌ NOT allowed — tuples are immutable

tup1 = ()          # empty tuple
tup2 = (1,)        # single-element tuple (note the comma!)
tup3 = (1, 2, 3)   # multi-element tuple
```

### 5. Tuple Methods
```python
tup = (2, 1, 3, 1)

tup.index(el)   # returns index of the first occurrence — tup.index(1) → 1
tup.count(el)   # counts total occurrences — tup.count(1) → 2
```

---

## 💻 Practice Exercises

### Lists
1. Write a program to ask the user to enter the names of their 3 favorite movies & store them in a list.
2. Write a program to check if a list contains a palindrome of elements (Hint: use the `copy()` method).
   - Example: `[1, 2, 3, 2, 1]`, `[1, "abc", "abc", 1]`

### Tuples
3. Write a program to count the number of students with the `"A"` grade in the tuple:
   `["C", "D", "A", "A", "B", "B", "A"]`
4. Store the above values in a list & sort them from `"A"` to `"D"`.

---

## 🔑 Key Takeaways
- **Lists** are mutable — you can change, add, or remove elements after creation.
- **Tuples** are immutable — once created, their contents cannot be modified.
- Both support indexing and slicing in the same way as strings.
- Choose tuples over lists when data should remain constant (e.g., fixed configuration values).