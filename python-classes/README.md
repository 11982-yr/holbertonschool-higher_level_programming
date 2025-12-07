# Python - Classes and Objects

This project introduces the fundamental concepts of Object-Oriented Programming (OOP) in Python. Through quizzes and hands-on practice, you will learn how classes, objects, attributes, and methods work. You will also explore key principles such as encapsulation, information hiding, and properties.

The core objective of this project is learning by doing—experimenting with classes and objects, trying examples on your own, and developing a deeper understanding of Python’s object model.

## Project Structure
```shell
holbertonschool-higher_level_programming/
└── python-classes/
    ├── README.md
    ├── 0-square.py
    ├── 1-square.py
    ├── 2-square.py
    ├── 3-square.py
    ├── 4-square.py
    ├── 5-square.py
    └── 6-square.py
```

## Task Descriptions

**0. My first square**
- Creates an empty class ```Square```.
- Introduces basic class definition and structure.

**1. Square with size**
- Adds a private instance attribute ```__size```.
- The size is assigned during object instantiation but no validation is done yet.

**2. Size validation**

- Adds type and value validation for ```size``` in ```__init__```.
    - Must be an integer, otherwise raise ```TypeError```.
    - Must be >= 0, otherwise raise ```ValueError```.
- Introduces defensive programming and error handling.

**3. Area of a square**
- Adds a public method ```area()``` that returns the current square’s area.
- Demonstrates encapsulation and using private attributes internally.

**4. Access and update private attribute**
- Adds ```@property``` and ```@size.setter``` to control access to ```__size```.
- Centralizes validation logic and allows safe attribute updates.

**5. Printing a square**
- Adds ```my_print()``` to print the square using the ```#``` character.
    - Prints an empty line if size is 0.
    - Uses loops and string repetition to display the shape.

**6. Coordinates of a square**
- Introduces a second private attribute ```__position``` with its own getter/setter.
```position``` controls how the square is printed:
    - ```position[0]``` → horizontal spaces
    - ```position[1]``` → vertical spaces
    - Enhances ```my_print()``` to use both offsets.
