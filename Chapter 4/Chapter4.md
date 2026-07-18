# Chapter 4: Dictionary & Sets

A complete guide to Python's key-value and unique-collection data structures.

---

## 📖 Overview
This chapter covers two important built-in data structures in Python:
- **Dictionaries** — store data as key-value pairs
- **Sets** — store unique, unordered collections of items

---

## 🔑 Dictionaries

### What is a Dictionary?
- An unordered (insertion-ordered since Python 3.7+), mutable collection of **key-value pairs**.
- Defined using curly braces: `my_dict = {"name": "Ali", "age": 22}`
- Keys must be unique and immutable (`str`, `int`, `tuple`); values can be of any type.

### Creating & Accessing
```python
student = {"name": "Sara", "age": 20, "course": "Python"}
print(student["name"])        # Access by key
print(student.get("age"))     # Safer access using get()
```

### Common Dictionary Methods
| Method | Use |
|---|---|
| `.keys()` | returns all keys |
| `.values()` | returns all values |
| `.items()` | returns key-value pairs as tuples |
| `.get(key)` | safely fetch a value (no error if key missing) |
| `.update()` | add/update multiple key-value pairs |
| `.pop(key)` | remove a key and return its value |
| `.popitem()` | remove the last inserted key-value pair |
| `.clear()` | empty the dictionary |

### Adding, Updating, Deleting
```python
student["grade"] = "A"          # add new key
student["age"] = 21             # update existing key
del student["course"]           # delete a key
```

### Looping Through a Dictionary
```python
for key, value in student.items():
    print(key, ":", value)
```

### Key Concept
Dictionary keys must be **unique and immutable** — using a mutable type (like a list) as a key raises a `TypeError`.

---

## 🔢 Sets

### What is a Set?
- An unordered, mutable collection of **unique** items.
- Defined using curly braces (without key-value pairs): `my_set = {1, 2, 3}`
- Automatically removes duplicate values.

### Creating & Modifying
```python
fruits = {"apple", "banana", "cherry"}
fruits.add("mango")            # add an item
fruits.remove("banana")        # remove an item (error if not found)
fruits.discard("kiwi")         # remove safely (no error if not found)
```

### Common Set Methods
| Method | Use |
|---|---|
| `.add(x)` | add a single item |
| `.update()` | add multiple items |
| `.remove(x)` | remove item (raises error if missing) |
| `.discard(x)` | remove item (no error if missing) |
| `.pop()` | remove a random item |
| `.clear()` | empty the set |

### Set Operations
| Operation | Symbol | Method |
|---|---|---|
| Union | `\|` | `.union()` |
| Intersection | `&` | `.intersection()` |
| Difference | `-` | `.difference()` |
| Symmetric Difference | `^` | `.symmetric_difference()` |

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a | b)   # {1, 2, 3, 4}
print(a & b)   # {2, 3}
print(a - b)   # {1}
print(a ^ b)   # {1, 4}
```

### Key Concept
Sets are great for removing duplicates and performing fast membership tests, but they **don't maintain order** and **can't be indexed**.

---

## 📊 Dictionary vs Set — Quick Comparison
| Feature | Dictionary | Set |
|---|---|---|
| Stores | Key-value pairs | Unique values only |
| Syntax | `{"key": "value"}` | `{value1, value2}` |
| Ordered? | Insertion-ordered | Unordered |
| Duplicates | Keys must be unique | All values unique |
| Indexing | Access via key | Not indexable |
| Use case | Structured/labeled data | Uniqueness & set math |

---

## ✅ Chapter Checklist
- [ ] Create and access dictionaries
- [ ] Use `.get()`, `.update()`, `.items()`
- [ ] Loop through dictionary key-value pairs
- [ ] Create and modify sets
- [ ] Perform union, intersection, difference operations
- [ ] Understand when to use a dictionary vs a set