# Python - Exceptions

This project focuses on understanding and working with exceptions in Python. You will explore how errors differ from exceptions, how to properly handle them, and when to use cleanup actions. This knowledge is essential for writing robust, maintainable, and bug-resistant Python programs.
 
## Project Structure
```
holbertonschool-higher_level_programming/
└── python-exceptions/
    ├── 0-safe_print_list.py
    ├── 1-safe_print_integer.py
    ├── 2-safe_print_list_integers.py
    ├── 3-safe_print_division.py
    ├── 4-list_division.py
    ├── 5-raise_exception.py
    ├── 6-raise_exception_msg.py
    └── README.md
```

## Project/Tasks Descriptions

```shell
- 0-safe_print_list.py
    │     → Safely prints a specified number of elements from a list.
    │       Avoids errors if the list is shorter than expected.

- 1-safe_print_integer.py
    │     → Safely prints an integer using try/except.
    │       Returns True if successful, False otherwise.

- 2-safe_print_list_integers.py
    │     → Prints only the integer elements of a list.
    │       Handles non-integer values gracefully using exception handling.

- 3-safe_print_division.py
    │     → Performs division and prints the result inside a try/except/finally.
    │       Always returns the division result or None on failure.

- 4-list_division.py
    │     → Divides elements of two lists index by index.
    │       Handles type errors, zero division, and out-of-range indices.
    │       Returns a new list with the results.
  
- 5-raise_exception.py
    │     → Deliberately raises a TypeError exception.
    │       Used to practice raising built-in exceptions.
  
- 6-raise_exception_msg.py
    │     → Raises a NameError exception with a custom message.
    │       Demonstrates raising exceptions with user-defined text.
```
## Learning Objectives

By the end of this project, you should be able to explain the following concepts clearly and confidently:

**General**

- Why Python programming is awesome
- The difference between errors and exceptions
- What exceptions are and how to use the
- When and why exceptions should be used
- How to correctly handle an exception
- The purpose of catching exceptions
- How to raise built-in exceptions
- When a clean-up action is needed after an exception (e.g., using finally)

## Resources

You may find the following helpful during the project:

- Errors and Exceptions (Python documentation / tutorials)
- Learn to Program 11: Static & Exception Handling
      - Start at minute 7 for the relevant portion

## Requirements

**General**

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files should end with a new line
- The first line of all scripts must be exactly:
```shell
#!/usr/bin/python3
```
- A README.md file at the project root is mandatory
- Your code must follow pycodestyle (version 2.7.*)
- All files must be executable
- File length will be tested using wc

## Author
- Yara K. Alrasheed <11982@holbertonstudents.com>
