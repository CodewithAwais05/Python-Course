# Chapter 7: File I/O in Python

## 📋 Overview
This chapter explains how Python interacts with files on disk — opening, reading, writing, and deleting them — along with the safer `with` syntax that handles closing files automatically.

## 🎯 Learning Objectives
By the end of this chapter, you will be able to:
- Distinguish between text files and binary files
- Open a file in different modes
- Read data from a file (entire content or line-by-line)
- Write and append data to a file
- Use the `with` statement for safe file handling
- Delete a file using the `os` module

---

## 📚 Topics Covered

### 1. File I/O in Python
Python can be used to perform operations on a file (read & write data).

**Types of Files**
| Type | Examples |
|---|---|
| Text Files | `.txt`, `.docx`, `.log`, etc. |
| Binary Files | `.mp4`, `.mov`, `.png`, `.jpeg`, etc. |

### 2. Open, Read & Close a File
A file must be opened before it can be read or written.

```python
f = open("file_name", "mode")

# e.g.
f = open("sample.txt", "r")

data = f.read()
f.close()
```

**File Modes**
| Character | Meaning |
|---|---|
| `'r'` | Open for reading (default) |
| `'w'` | Open for writing, truncating the file first |
| `'x'` | Create a new file and open it for writing |
| `'a'` | Open for writing, appending to the end if the file exists |
| `'b'` | Binary mode |
| `'t'` | Text mode (default) |
| `'+'` | Open for updating (reading and writing) |

### 3. Reading a File
```python
data = f.read()       # reads the entire file
data = f.readline()    # reads one line at a time
```

### 4. Writing to a File
```python
f = open("demo.txt", "w")
f.write("this is a new line")   # overwrites the entire file

f = open("demo.txt", "a")
f.write("this is a new line")   # adds to the end of the file
```

### 5. `with` Syntax
Automatically closes the file once the block finishes executing — a safer alternative to manual `open()`/`close()`.

```python
with open("demo.txt", "a") as f:
    data = f.read()
```

### 6. Deleting a File
Requires the `os` module — a file (like a code library) written by another programmer that provides reusable functions.

```python
import os
os.remove(filename)
```

---

## 💻 Practice Exercises
1. Create a new file `"practice.txt"` using Python. Add the following data to it:
   ```
   Hi everyone
   we are learning File I/O
   using Java.
   I like programming in Java.
   ```
2. Write a program to replace all occurrences of `"java"` with `"python"` in the file above.
3. Write a program to search whether the word `"learning"` exists in the file.
4. Write a program to find in which line of the file the word `"learning"` first occurs. Print `-1` if the word is not found.
5. From a file containing numbers separated by commas, print the count of even numbers.

---

## 🔑 Key Takeaways
- Always close a file after use — or better, use the `with` statement so it closes automatically.
- `'w'` mode overwrites file content; `'a'` mode appends to it.
- The `os` module provides system-level operations like file deletion.