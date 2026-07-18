**Variable**
- A name that refers to a value stored in memory.
- No need to declare type explicitly — Python is *dynamically typed*.
- Rule: `variable_name = value`
**Rules for naming variables**
- Must start with a letter or underscore (`_`), not a digit.
- Can contain letters, digits, underscores — no spaces or special symbols.
- Case-sensitive (`age` and `Age` are different).
- Cannot use Python keywords (`if`, `for`, `class`, etc.).
**Basic Datatypes**
| Type | Example | Meaning |
|---|---|---|
| `int` | `5`, `-3` | whole numbers |
| `float` | `3.14`, `-0.5` | decimal numbers |
| `str` | `"hello"` | text, in quotes |
| `bool` | `True`, `False` | logical values |
 
**Type checking & conversion**
- `type(x)` → tells datatype of `x`.
- Type casting: `int()`, `float()`, `str()`, `bool()` — convert between types.
- `input()` always returns a **string**, even if the user types a number — must cast it (`int(input())`).
**Operators**
- Arithmetic: `+  -  *  /  //  %  **`
  - `/` → always gives float (true division).
  - `//` → floor division (drops decimal).
  - `%` → modulus (remainder).
  - `**` → power/exponent.
- Comparison: `==  !=  >  <  >=  <=` → return `bool`.
- Logical: `and`, `or`, `not`.
**Key concept:** operations between different types can auto-convert (`int + float = float`), but `str + int` gives an error — must cast explicitly.
 
---