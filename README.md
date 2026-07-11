# Python Practice Code

A collection of Python practice scripts covering core language concepts — from strings and formatting to lists, tuples, dictionaries, and sets. Each topic is broken into small, focused files to make it easy to study individual concepts.

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
└── list_tuple/
    ├── test_data.py               # Shared test data for list/tuple scripts
    ├── list.py                    # List basics and comparison with tuples
    ├── list_append.py             # append() method
    ├── list_copy.py               # copy() — shallow copy of a list
    ├── list_method.py             # count() method
    ├── insert_method.py           # insert() method
    ├── extend_method.py           # extend() method
    ├── pop_method.py              # pop() method
    ├── remove_method.py           # remove() method
    ├── del_method.py              # del statement
    ├── delete_from_list.py        # Deleting elements + split()
    ├── sort.py                    # sort() — ascending and descending
    ├── slice.py                   # List slicing syntax
    ├── reverse_method.py          # reverse() method
    ├── clone_list_syntax.py       # Reference copy vs. clone ([:])
    ├── use_split_as_delimiter.py  # split() with a delimiter
    ├── tuple.py                   # Tuple basics, indexing, slicing
    ├── nested_tuple.py            # Nested tuples and access
    ├── tuple_count.py             # count() on tuples
    └── tuple_sum_min_max_len.py   # sum(), min(), max(), len() on tuples
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

## Key Concepts at a Glance

- **Lists are mutable** — elements can be changed after creation.
- **Tuples are immutable** — once created, elements cannot be reassigned.
- **Sets** automatically remove duplicates and support mathematical set operations.
- **Dictionaries** store key-value pairs; keys can be strings, numbers, or tuples.
- **Raw strings** (`r"..."`) treat backslashes literally — useful for file paths.
- **Cloning a list** with `[:]` creates an independent copy; assigning with `=` only copies the reference.

---

## Prerequisites

- Python 3.x

No external packages are required. All scripts use the Python standard library.

---

## Running the Scripts

Run any script directly from the terminal:

```bash
python raw_string.py
python string_format.py
python Dictionary/practice_dict.py
python list_tuple/sort.py
```

> Some scripts in `list_tuple/` import shared data from `test_data.py` or `del_method.py`, so run them from within the `list_tuple/` directory or adjust the Python path accordingly.
