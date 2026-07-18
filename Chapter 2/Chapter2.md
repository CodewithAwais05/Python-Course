**Strings**
- Sequence of characters, written in `' '` or `" "`.
- Indexed from `0`; negative indexing (`-1` = last character).
- Slicing: `s[start:end]` → gets a substring (end index excluded).
**Common string methods**
| Method | Use |
|---|---|
| `.upper()` / `.lower()` | change case |
| `.title()` | capitalize each word |
| `.strip()` | remove leading/trailing spaces |
| `.replace(old, new)` | replace substring |
| `.split()` | break string into a list of words |
| `.join()` | combine list into a string |
| `.find()` / `.index()` | locate substring |
| `.isdigit()` / `.isalpha()` | check content type |
| `len(s)` | length of string |
 
- Strings are **immutable** — can't change a character directly; must create a new string.
- String concatenation: `+`; repetition: `*`.
**Conditional Statements**
- `if`, `elif`, `else` — control flow based on conditions.
- Syntax relies on **indentation** (no braces `{}` like other languages).
```python
if condition:
    # code
elif another_condition:
    # code
else:
    # code
```
- Conditions evaluate to `True`/`False`.
- Can combine conditions using `and`, `or`, `not`.
- Nested if statements: an `if` inside another `if`.
**Key concept:** Indentation is not optional in Python — it defines code blocks. Wrong indentation = error.
 
---