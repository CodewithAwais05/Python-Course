**Lists**
- Ordered, **mutable** (changeable) collection: `my_list = [1, 2, 3]`
- Can hold mixed datatypes: `[1, "hi", 3.5, True]`
- Indexed from `0`; supports negative indexing and slicing like strings.
**Common list methods**
| Method | Use |
|---|---|
| `.append(x)` | add item to end |
| `.insert(i, x)` | add item at index `i` |
| `.remove(x)` | remove first matching value |
| `.pop(i)` | remove & return item at index (default last) |
| `.sort()` | sort in place |
| `.reverse()` | reverse in place |
| `len(list)` | number of items |
| `in` | check membership (`3 in my_list`) |
 
**Tuples**
- Ordered, **immutable** (cannot be changed after creation): `my_tuple = (1, 2, 3)`
- Same indexing/slicing rules as lists.
- Used when data shouldn't change (e.g., coordinates, fixed records).
- Can't `.append()`, `.remove()`, or modify elements directly.
- Faster than lists due to immutability.
**Lists vs Tuples**
| Feature | List | Tuple |
|---|---|---|
| Mutable? | Yes | No |
| Syntax | `[ ]` | `( )` |
| Speed | Slower | Faster |
| Use case | Data that changes | Fixed/constant data |
 
**Key concept:** If you try to modify a tuple, Python raises a `TypeError` — this immutability is the whole point of using one.
 
---