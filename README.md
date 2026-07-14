# Python Practice Code

A collection of Python practice scripts covering core language concepts — from strings and formatting to lists, tuples, dictionaries, sets, control flow, functions, exception handling, and OOP. Each topic is broken into small, focused files to make it easy to study individual concepts.

---

## Quick Glance (Pictorial Overview)

```mermaid
flowchart TD
    A[python-code] --> B[Strings & Basics]
    A --> C[Dictionary/]
    A --> D[list_tuple/]
    A --> E[set/]
    A --> F["class/ (OOP)"]
    A --> G[fundaments_programming/]

    B --> B1[raw_string.py]
    B --> B2[string_format.py]
    B --> B3["test.py (if/elif/else)"]

    C --> C1[dict_data.py]
    C --> C2["practice_dict.py (keys/values/del)"]
    C --> C3["practice_set.py (set ops)"]

    D --> D1["List methods: append, insert,
    extend, pop, remove, sort, slice..."]
    D --> D2["Tuple methods: index, slice,
    count, sum/min/max/len"]

    E --> E1["set.py (union | intersection & update)"]
    E --> E2["searching_in_set.py (in)"]

    F --> F1["rectangle_class.py (attributes)"]
    F --> F2["circle_class.py + main.py
    (methods, matplotlib draw)"]
    F --> F3["Points.py (multiple objects,
    enumerate, scope)"]

    G --> G1["Loops: for, while,
    break/continue, enumerate"]
    G --> G2["functions.py (def, return,
    scope, sorted)"]
    G --> G3["exception_handling*.py
    (try/except/else/finally)"]
    G --> G4["TextAnalyzer class
    (word frequency)"]
```

---

## Project Structure

```
python-code/
├── raw_string.py          # Raw strings and escape characters
├── string_format.py       # String formatting techniques
├── test.py                # Basic if/elif/else conditionals
├── file.txt               # Sample text file
│
├── Dictionary/
│   ├── dict_data.py       # Dictionary data definitions (shared data)
│   ├── practice_dict.py   # Dictionary operations and methods
│   └── practice_set.py    # Set operations and methods
│
├── list_tuple/
│   ├── test_data.py               # Shared test data for list/tuple scripts
│   ├── list.py                    # List basics and comparison with tuples
│   ├── list_append.py             # append() method
│   ├── list_copy.py               # copy() — shallow copy of a list
│   ├── list_method.py             # count() method
│   ├── insert_method.py           # insert() method
│   ├── extend_method.py           # extend() method
│   ├── pop_method.py              # pop() method
│   ├── remove_method.py           # remove() method
│   ├── del_method.py              # del statement
│   ├── delete_from_list.py        # Deleting elements + split()
│   ├── sort.py                    # sort() — ascending and descending
│   ├── slice.py                   # List slicing syntax
│   ├── reverse_method.py          # reverse() method
│   ├── clone_list_syntax.py       # Reference copy vs. clone ([:])
│   ├── use_split_as_delimiter.py  # split() with a delimiter
│   ├── tuple.py                   # Tuple basics, indexing, slicing
│   ├── nested_tuple.py            # Nested tuples and access
│   ├── tuple_count.py             # count() on tuples
│   └── tuple_sum_min_max_len.py   # sum(), min(), max(), len() on tuples
│
├── set/
│   ├── set.py                     # Set creation, union, intersection, update
│   └── searching_in_set.py        # Membership testing with `in`
│
├── class/
│   ├── rectangle_class.py         # Rectangle class — constructor & attributes
│   ├── circle_class.py            # Circle class — methods + matplotlib drawing
│   ├── main.py                    # Driver script for Circle (instantiate, call methods)
│   └── Points.py                  # Points class, enumerate, variable scope
│
└── fundaments_programming/
    ├── for_loop.py             # range(), iterating lists
    ├── for_loop_2.py           # Iterating by index vs. by value, mutating a list
    ├── enumerated_for_loop.py  # enumerate() for index + value
    ├── while_loop.py           # while loops with different increments
    ├── break_continue_loop.py  # break and continue statements
    ├── functions.py            # def, return values, scope, sorted()
    ├── addition_of_numbers.py  # Simple function definitions (add variants)
    ├── exception_handling.py   # try/except/else/finally with file I/O
    ├── exception_handling_2.py # try/except for ZeroDivisionError, NameError, IndexError, ValueError
    ├── test_analyzer.py        # TextAnalyzer class — cleans text & builds word-frequency map
    └── text_analysis.py        # Driver script using TextAnalyzer + if/else, while
```

---

## Topics Covered

### Strings (root level)

| File | Concept |
|---|---|
| `raw_string.py` | Escape sequences, raw strings with `r""`, and quoting characters |
| `string_format.py` | Three formatting styles: f-strings, `.format()`, and `%` operator |
| `test.py` | `if / elif / else` conditionals |

---

### Dictionary (`Dictionary/`)

| File | Concept |
|---|---|
| `dict_data.py` | Defines reusable dictionaries with mixed key/value types |
| `practice_dict.py` | Accessing values by key, `.keys()`, `.values()`, `del()` |
| `practice_set.py` | Creating sets, `.add()`, `.remove()`, set operations: `&`, `.difference()`, `.intersection()`, `.union()`, `.issubset()`, `.issuperset()` |

---

### Lists & Tuples (`list_tuple/`)

#### List Methods

| File | Method / Concept |
|---|---|
| `list.py` | List vs tuple — mutability, concatenation, slicing, `extend()`, `append()` |
| `list_append.py` | `append()` — adds a single element to the end |
| `list_copy.py` | `copy()` — creates a shallow copy |
| `list_method.py` | `count()` — counts occurrences of an element |
| `insert_method.py` | `insert(index, element)` — inserts at a position |
| `extend_method.py` | `extend(iterable)` — adds multiple elements |
| `pop_method.py` | `pop(index)` — removes and returns element at index |
| `remove_method.py` | `remove(value)` — removes first occurrence of a value |
| `del_method.py` | `del list[index]` — removes element by index |
| `delete_from_list.py` | `del()` with `split()` to create lists from strings |
| `sort.py` | `sort()` ascending; `sort(reverse=True)` descending |
| `slice.py` | Slicing syntax: `[start:stop]`, `[:stop]`, `[start:]` |
| `reverse_method.py` | `reverse()` — reverses a list in place |
| `clone_list_syntax.py` | Reference copy (`B = A`) vs. true clone (`B = A[:]`) |
| `use_split_as_delimiter.py` | `split(",")` — splitting a string into a list using a delimiter |

#### Tuple Methods

| File | Method / Concept |
|---|---|
| `tuple.py` | Tuple creation, indexing, negative indexing, slicing, concatenation |
| `nested_tuple.py` | Nested tuples and accessing inner elements |
| `tuple_count.py` | `count()` — counts occurrences in a tuple |
| `tuple_sum_min_max_len.py` | `sum()`, `min()`, `max()`, `len()` on numeric tuples |

---

### Sets (`set/`)

| File | Concept |
|---|---|
| `set.py` | Set creation, `.union()` / `\|`, `.intersection()` / `&`, `.update()` (note: `+` is not supported on sets) |
| `searching_in_set.py` | Membership testing with the `in` operator |

---

### Object-Oriented Programming (`class/`)

| File | Concept |
|---|---|
| `rectangle_class.py` | Defining a class with `__init__` and storing attributes (`color`, `height`, `width`) |
| `circle_class.py` | A class with instance methods (`add_radius()`, `draw_circle()`) and a `matplotlib`-based visualization |
| `main.py` | Driver script — creates a `Circle`, reads/updates attributes, calls methods, inspects with `dir()` / `type()` |
| `Points.py` | Multiple class instances, mutating an instance attribute, `enumerate(..., start=1)`, and local vs. global variable scope |

---

### Fundamentals of Programming (`fundaments_programming/`)

| File | Concept |
|---|---|
| `for_loop.py` | `range()` variants, iterating over lists |
| `for_loop_2.py` | Iterating by index vs. by value; mutating list elements during iteration |
| `enumerated_for_loop.py` | `enumerate()` to get index + value together |
| `while_loop.py` | `while` loops with different step increments |
| `break_continue_loop.py` | `break` to exit a loop early, `continue` to skip an iteration |
| `functions.py` | Function definitions, `return`, variable scope (local vs. global), `sorted()` |
| `addition_of_numbers.py` | Simple function variants for adding two numbers |
| `exception_handling.py` | `try / except / else / finally` with file I/O (`IOError`) |
| `exception_handling_2.py` | Handling `ZeroDivisionError`, `NameError`, `IndexError`, `ValueError` |
| `test_analyzer.py` | `TextAnalyzer` class — normalizes text (lowercase, strips punctuation) and builds a word-frequency map |
| `text_analysis.py` | Driver script for `TextAnalyzer`; also covers `if/else` and `while` on simple state |

---

## Key Concepts at a Glance

- **Lists are mutable** — elements can be changed after creation.
- **Tuples are immutable** — once created, elements cannot be reassigned.
- **Sets** automatically remove duplicates and support mathematical set operations (`union`, `intersection`, `update`) — but not `+`.
- **Dictionaries** store key-value pairs; keys can be strings, numbers, or tuples.
- **Raw strings** (`r"..."`) treat backslashes literally — useful for file paths.
- **Cloning a list** with `[:]` creates an independent copy; assigning with `=` only copies the reference.
- **Classes** bundle state (attributes set in `__init__`) with behavior (methods); each instance keeps its own copy of the attributes.
- **Exception handling** follows `try → except → else → finally`: `else` runs only if no exception occurred, `finally` always runs.
- **`enumerate()`** gives you both the index and the value while looping, optionally starting from a custom number.

---

## Prerequisites

- Python 3.x
- `matplotlib` (only needed for `class/circle_class.py`, which draws a circle) — install with `pip install matplotlib`

All other scripts use only the Python standard library.

---

## Running the Scripts

Run any script directly from the terminal:

```bash
python raw_string.py
python string_format.py
python Dictionary/practice_dict.py
python list_tuple/sort.py
python set/set.py
python class/main.py
python fundaments_programming/for_loop.py
```

> Some scripts import shared data/classes from sibling files (e.g. `list_tuple/test_data.py`, `class/circle_class.py`, `fundaments_programming/test_analyzer.py`), so run them from the repository root or adjust the Python path accordingly.
