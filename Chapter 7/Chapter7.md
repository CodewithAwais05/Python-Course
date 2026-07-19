# Chapter 7: File Input/Output in Python

A complete guide to reading from and writing to files in Python.

---

## 📖 Overview
File I/O (Input/Output) allows a program to:
- **Read** data from external files
- **Write** or **append** data to files
- Store data permanently, beyond the program's runtime

---

## 📂 Opening & Closing Files

### The `open()` Function
```python
file = open("data.txt", "r")   # open in read mode
# ... work with the file ...
file.close()                   # always close when done
```

### File Modes
| Mode | Meaning |
|---|---|
| `"r"` | Read (default) — file must exist |
| `"w"` | Write — creates file if missing, **overwrites** existing content |
| `"a"` | Append — creates file if missing, adds to end without erasing |
| `"r+"` | Read and write |
| `"rb"` / `"wb"` | Read/write in binary mode (for non-text files) |

### Why Closing Matters
- Frees system resources.
- Ensures all written data is properly saved (flushed) to disk.
- Forgetting to close can cause data loss or file-locking issues.

---

## 📖 Reading Files

### Reading Methods
| Method | Description |
|---|---|
| `.read()` | reads the entire file as a single string |
| `.read(n)` | reads the first `n` characters |
| `.readline()` | reads a single line at a time |
| `.readlines()` | reads all lines into a list of strings |

```python
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
```

### Looping Through a File Line by Line
```python
file = open("data.txt", "r")
for line in file:
    print(line.strip())   # strip() removes trailing newline
file.close()
```

---

## ✍️ Writing & Appending

### Writing (overwrites existing content)
```python
file = open("data.txt", "w")
file.write("Hello, World!\n")
file.close()
```

### Appending (adds without erasing)
```python
file = open("data.txt", "a")
file.write("New line added.\n")
file.close()
```

### Writing Multiple Lines
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
file = open("data.txt", "w")
file.writelines(lines)
file.close()
```

---

## 🛡️ Using `with` Statement (Best Practice)

```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
# file is automatically closed here, even if an error occurs
```

### Why Use `with`?
- Automatically handles closing the file — no need to call `.close()` manually.
- Safer: closes the file even if an exception occurs during processing.
- Cleaner and more Pythonic than manual open/close.

---

## 🗂️ Working with File Paths
- **Relative path:** `"data.txt"` — relative to the current working directory.
- **Absolute path:** `"C:/Users/Name/Documents/data.txt"` — full path from root.
- Use `os.path` or `pathlib` for more robust, cross-platform path handling.

```python
import os
print(os.path.exists("data.txt"))   # check if file exists
```

---

## 🗑️ Deleting a File (using the `os` module)

- A **module** is like a code library — a file written by another programmer that generally has functions we can use.
- To delete a file, Python doesn't have a built-in keyword — instead, we use the `os` module.

```python
import os
os.remove(filename)
```

### Key Points
- `os.remove(filename)` permanently deletes the specified file from disk.
- The file must exist, otherwise Python raises a `FileNotFoundError`.
- Good practice: check if the file exists first using `os.path.exists()` before removing it, to avoid errors.

```python
import os

if os.path.exists("data.txt"):
    os.remove("data.txt")
else:
    print("File does not exist.")
```

---

## 📊 Read vs Write vs Append — Quick Comparison
| Mode | Creates file if missing? | Erases existing content? | Cursor position |
|---|---|---|---|
| `r` | No (error if missing) | No | start |
| `w` | Yes | Yes | start |
| `a` | Yes | No | end |

---

## ✅ Chapter Checklist
- [ ] Open a file in read, write, and append modes
- [ ] Use `.read()`, `.readline()`, `.readlines()`
- [ ] Write and append text to a file
- [ ] Loop through a file line by line
- [ ] Use the `with` statement for safe file handling
- [ ] Check file existence using `os.path`
- [ ] Delete a file using `os.remove()`