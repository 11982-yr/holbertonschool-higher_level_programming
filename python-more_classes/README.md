# Python - More Classes and Objects
This project continues your journey into Object-Oriented Programming (OOP) in Python.
You will learn more advanced concepts such as class attributes, static methods, class methods, printing behaviors (```__str__```, ```__repr__```), and object destruction.

## Description
- This project expands upon the basics of Python classes and objects.
- You will practice:
    - Designing more complex classes
    - Implementing class-level features
    - Differentiating object attributes vs. class attributes
    - Using properties, getters, setters
    - Overloading special methods
    - Understanding and applying OOP principles
It also includes quizzes to reinforce learning.

## Resources
- You are expected to read or watch the following:

**Object-Oriented Programming**
- Object Oriented Programming (read up to Inheritance, excluded)

**Python Class Fundamentals**
- Read only these sections of the second article:
    - General Introduction
    - First-class Everything
    - A Minimal Class in Python
    - Attributes
    - Methods
    - The ```__init__``` Method
    - Data Abstraction, Data Encapsulation, and Information Hiding
    - ```__str__``` and ```__repr__``` Methods
    - Public, Protected, and Private Attributes
    - Destructor

**Additional Topics**
- Class and Instance Attributes
- ```classmethod``` and ```staticmethod```
- Properties vs Getters and Setters (especially: Public instead of Private Attributes)
- ```str``` vs ```repr```

## Project Structure
```
holbertonschool-higher_level_programming/
└── python-more_classes/
    ├── README.md
    ├── 0-rectangle.py
    ├── 1-rectangle.py
    ├── 2-rectangle.py
    ├── 3-rectangle.py
    ├── 4-rectangle.py
    ├── 5-rectangle.py
    ├── 6-rectangle.py
    ├── 7-rectangle.py
    ├── 8-rectangle.py
    └── 9-rectangle.py
```

## Task-by-Task Description

**0. Simple Rectangle — ```0-rectangle.py```**

- Defines an empty ```Rectangle``` class.
- No attributes, no methods.
- Acts as a starting point for future tasks.

**1. Real Definition of a Rectangle — ```1-rectangle.py```**
- Adds:
        - Private attributes: ```__width```, ```__height```
        - Property getters and setters with validation
                - Must be integers
                - Must be ≥ 0
        - Constructor initializes width and height
- Introduces proper encapsulation.

**2. Area and Perimeter — ```2-rectangle.py```**
- Extends the rectangle with:
        - ```area()``` method
        - ```perimeter()``` method
                - Returns 0 if width or height is 0
- Teaches simple behavior methods.

**3. String Representation — ```3-rectangle.py```**
- Adds:
        - ```__str__``` to print the rectangle using the ```#``` character
        - ```__repr__``` returns a reproducible string: ```Rectangle(width, height)```
- Demonstrates special methods for string representation.

**4. Eval is Magic — ```4-rectangle.py```**
- Refines:
        - ```__repr__``` must return a string allowing recreation via ```eval()```
- Example:
```eval(repr(rect))  # → new Rectangle instance```
- Strengthens understanding of ```__repr__```.

**5. Detect Instance Deletion — ```5-rectangle.py```**
- Adds:
        - ```__del__``` special method
- Prints:
```Bye rectangle...```
- when an instance is deleted
- Introduces object lifecycle management.

**6. How Many Instances — ```6-rectangle.py```**
- Extends the class with:
        - Class attribute ```number_of_instances```
                - Increments in ```__init__```
                - Decrements in ```__del__```
- Teaches class attributes and tracking instances.

**7. Change Representation — ```7-rectangle.py```**
- Adds:
        - Class attribute ```print_symbol``` (default: ```#```)
        - ```__str__``` now uses ```print_symbol```
                - Can be any type (converted with ```str()```)
- Demonstrates customizable output and class-wide configuration.

**8. Compare Rectangles — ```8-rectangle.py```**
- Introduces:
        - Static method ```bigger_or_equal(rect_1, rect_2)```
                - Validates both arguments
                - Returns the rectangle with the larger area
                - Returns ```rect_1``` if equal
- Reinforces static methods and object comparisons.

**9. A Square is a Rectangle — ```9-rectangle.py```**
- Adds:
        - Class method ```square(cls, size=0)```
                - Returns ```Rectangle(size, size)```
- Introduces class methods and alternative constructors.

## Requirements
**General**
- Allowed editors: ```vi```, ```vim```, ```emacs```
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files must:
        - End with a new line
        - Be executable
        - Start with shebang:
            ```#!/usr/bin/python3```
- Code must follow pycodestyle 2.7.*
- File length will be checked using ```wc```

## Author
- Yara K. Alrasheed <11982@holbertonstudents.com>


