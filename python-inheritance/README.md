# Python – Inheritance

This project is part of the Higher Level Programming curriculum at Holberton School and focuses on understanding inheritance in Python.

The goal of this project is to learn how classes can inherit attributes and methods from other classes, how to override behavior, and how to work with Python’s built-in tools for checking object relationships.

## Learning Objectives
By completing this project, you should be able to:

* Understand what inheritance is and why it is useful
* Create child classes that inherit from parent classes
* Override methods in subclasses
* Use ```isinstance()``` and ```issubclass()```
* Understand method resolution order (MRO)
* Work with abstract-like base classes
* Control attribute access and behavior dynamically

## Files Description

| File                    | Description                                                        |
| ----------------------- | ------------------------------------------------------------------ |
| `0-lookup.py`           | Returns a list of available attributes and methods of an object    |
| `1-my_list.py`          | Defines a class that inherits from `list` and adds a custom method |
| `2-is_same_class.py`    | Checks if an object is exactly an instance of a specified class    |
| `3-is_kind_of_class.py` | Checks if an object is an instance of, or inherits from, a class   |
| `4-inherits_from.py`    | Checks if an object is an instance of a subclass                   |
| `5-base_geometry.py`    | Defines an empty `BaseGeometry` class                              |
| `6-base_geometry.py`    | Adds an `area()` method to `BaseGeometry`                          |
| `7-base_geometry.py`    | Adds integer validation to `BaseGeometry`                          |
| `8-rectangle.py`        | Defines a `Rectangle` class inheriting from `BaseGeometry`         |
| `9-rectangle.py`        | Implements a fully functional `Rectangle` class                    |
| `10-square.py`          | Defines a `Square` class inheriting from `Rectangle`               |
| `11-square.py`          | Enhances `Square` with string representation                       |
| `100-my_int.py`         | Defines a class that inverts equality operators                    |
| `101-add_attribute.py`  | Adds attributes dynamically to objects                             |
| `tests/`                | Contains test files used to validate the implementation            |

## Requirements
* Python 3.10+
* Ubuntu 22.04 LTS
* Code follows PEP8 style guidelines
* All files end with a newline
* First line of each Python file:
```bash
#!/usr/bin/python3
```
* All scripts are executable

## Usage Example
```bash
./3-is_kind_of_class.py
```
> Each file can be tested individually using the provided test files or custom test cases.

## Concepts Covered
* Class inheritance
* Method overriding
* Encapsulation
* Abstract base behavior
* Dynamic attribute assignment
* Operator overloading

## Author
**Yara K. Alrasheed**
📧 Email: 11982@holbertonschool.com
🐙 GitHub: 11982-yr
