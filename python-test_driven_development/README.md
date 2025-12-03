# Python - Test-driven development

This project focuses on Test-Driven Development (TDD) in Python. You will learn how to write tests before writing your code, using both doctest and unittest, and how proper documentation and edge-case thinking leads to more reliable programs.


## Background Context

Starting with this project:

- You must write all documentation (modules and functions) and tests before writing the actual code.
- Intranet checks for Python projects will not be released before the project deadline.
- You are strongly encouraged to collaborate on test cases, but not on the implementation.
- Always consider all possible edge cases — don’t trust the user!
- 
This project strengthens your ability to think critically about how code behaves in unexpected situations.

holbertonschool-higher_level_programming/
│
└── python-test_driven_development/
    ├── README.md
    ├── 0-add_integer.py
    ├── 2-matrix_divided.py
    ├── 3-say_my_name.py
    ├── 4-print_square.py
    ├── 5-text_indentation.py
    ├── 6-max_integer.py        
    ├── 6-main.py              
    │
    ├── tests/
    │   ├── 0-add_integer.txt
    │   ├── 2-matrix_divided.txt
    │   ├── 3-say_my_name.txt
    │   ├── 4-print_square.txt
    │   ├── 5-text_indentation.txt
    │   ├── 6-max_integer_test.py
    └──   └── <other doctest files>.txt

## Learning Objectives

By the end of this project, you should be able to clearly explain:

**General**

- Why Python programming is awesome
- What interactive tests are
- Why tests are important
- How to write doctests in docstrings
- How to write proper documentation for each module and function
- The basic doctest flags and how to use them
- How to identify and test for edge cases
- How TDD improves code quality

## Requirements

**Python Scripts**
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files must end with a new line
- First line of every file:
```
#!/usr/bin/python3
```
- A README.md file at the project root is mandatory
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- File length will be checked using wc

## Python Test Cases (doctest)
- Allowed editors: vi, vim, emacs
- All test files must end with a new line
- All test files must be inside a directory named tests/
- All test files must be .txt files
- Run all doctests with:
```
python3 -m doctest ./tests/*
```
- All modules must have documentation:
```
python3 -c 'print(__import__("my_module").__doc__)'
```
- All functions must have documentation:
```
python3 -c 'print(__import__("my_module").my_function.__doc__)'
```
- Documentation must be meaningful sentences explaining the purpose of the module, class, or method
(The checker verifies this.)
