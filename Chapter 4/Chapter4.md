# Chapter 4: Dictionary & Set

## 📋 Overview
This chapter covers two more essential Python data structures: **Dictionaries**, which store data as key-value pairs, and **Sets**, which store unordered collections of unique, immutable elements.

## 🎯 Learning Objectives
By the end of this chapter, you will be able to:
- Create and access dictionaries using keys
- Work with nested dictionaries
- Use built-in dictionary methods
- Create sets and understand their uniqueness constraint
- Use built-in set methods, including union and intersection

---

## 📚 Topics Covered

### 1. Dictionary in Python
Dictionaries store data values in **key:value** pairs. They are **unordered**, **mutable**, and do **not allow duplicate keys**.

```python
dict = {
    "name": "shradha",
    "cgpa": 9.6,
    "marks": [98, 97, 95],
}

dict["name"], dict["cgpa"], dict["marks"]

dict["key"] = "value"     # assigns a new key or updates an existing one
```

### 2. Nested Dictionaries
Dictionaries can contain other dictionaries as values.

```python
student = {
    "name": "shradha",
    "score": {
        "chem": 98,
        "phy": 97,
        "math": 95,
    }
}

student["score"]["math"]   # 95
```

### 3. Dictionary Methods
```python
myDict.keys()             # returns all keys
myDict.values()           # returns all values
myDict.items()            # returns all (key, value) pairs as tuples
myDict.get("key")         # returns the value for a given key
myDict.update(newDict)    # inserts/updates specified items in the dictionary
```

---

### 4. Set in Python
A set is a collection of **unordered** items. Each element must be **unique** and **immutable**.

```python
nums = {1, 2, 3, 4}

set2 = {1, 2, 2, 2}   # repeated elements stored only once → resolves to {1, 2}

null_set = set()       # empty set syntax (NOT {})
```

### 5. Set Methods
```python
set.add(el)         # adds an element
set.remove(el)       # removes the element
set.clear()          # empties the set
set.pop()            # removes a random value

set.union(set2)          # combines both sets' values & returns a new set
set.intersection(set2)   # combines common values & returns a new set
```

---

## 💻 Practice Exercises

### Dictionary
1. Store the following word meanings in a Python dictionary:
   - `table`: "a piece of furniture", "list of facts & figures"
   - `cat`: "a small animal"
2. Given a list of subjects for students, assume one classroom is required per subject. How many classrooms are needed by all students?
   ```
   "python", "java", "C++", "python", "javascript",
   "java", "python", "java", "C++", "C"
   ```
3. Write a program to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add entries one by one, using subject name as key and marks as value.

### Set
4. Figure out a way to store `9` and `9.0` as separate values in a set. (Hint: use built-in data types.)

---

## 🔑 Key Takeaways
- Dictionaries map unique keys to values, making lookups fast and expressive.
- Nested dictionaries allow modeling of hierarchical/structured data.
- Sets automatically remove duplicates and are ideal for membership tests and set operations like union/intersection.