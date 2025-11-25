# Python - import & modules

This project is part of the Foundations v2.1 Curriculum and introduces the basics of importing functions, using modules, handling command-line arguments, and writing Python scripts that follow good practices.

## Learning Objectives

At the end of this project, you should be able to explain:

**General**

- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function dir()
- How to prevent code from executing when imported (using if __name__ == "__main__":)
- How to use command-line arguments in Python programs

## Requirements
**General**

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 22.04 LTS using Python 3.10
- All files should end with a new line
- The first line of every file must be:
```bash
#!/usr/bin/python3
```
- A README.md at the root of the project is mandatory
- Code must follow pycodestyle (v2.7.*)
- All files must be executable
- File lengths will be tested with wc

## Project Structure
```bash
holbertonschool-higher_level_programming/
└── python-import_modules/
    ├── README.md
    │
    ├── 0-add.py
    ├── 1-calculation.py
    ├── 2-args.py
    ├── 3-infinite_add.py
    ├── 4-hidden_discovery.py
    ├── 5-variable_load.py
    ├── 100-my_calculator.py
    ├── 101-easy_print.py
    ├── 102-magic_calculation.py
    └── 103-fast_alphabet.py
```
**Extra note:**
- hidden_4.pyc is not stored inside the repo — it is downloaded into /tmp/ at runtime for Task 4:
```bash
/tmp/hidden_4.pyc
```

## Task Overview
**0. Import a simple function from a simple file**

Write a script that imports add(a, b) from add_0.py, assigns values to a and b, and prints the sum.

**1. My first toolbox!**

Import math functions (add, sub, mul, div) from calculator_1.py, perform operations on a = 10 and b = 5, and print the results.

**2. How to make a script dynamic!**

Print the number of arguments and a numbered list of all arguments passed to the script.

**3. Infinite addition**

Add all command-line arguments (integers), no matter how many, and print the result.

**4. Who are you?**

Print all names defined in the module hidden_4.pyc (excluding names starting with __), sorted alphabetically.

**5. Everything can be imported**

Import variable a from variable_load_5.py and print its value.

**6. Build my own calculator! (Advanced)**

A script that:
- Uses command-line arguments: ./100-my_calculator.py a operator b
- Validates arguments
- Performs +, -, *, /
- Prints formatted output

**7. Easy print (Advanced)**

Print #pythoniscool without using:
- print
- eval
- open
- import sys

**8. ByteCode → Python #3 (Advanced)**

Reproduce a function from bytecode. Implement:
```bash
def magic_calculation(a, b):
```
to match provided bytecode behavior.

**9. Fast alphabet (Advanced)**

Print the uppercase alphabet without:
- Loops
- Conditionals
- String literals
- str.join()
- System calls

**Author**

Yara K. Alrasheed <11982@holbertonschool.com>
