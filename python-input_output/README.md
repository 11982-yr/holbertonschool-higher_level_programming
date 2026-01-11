# Python – Input / Output

This project is part of the Higher Level Programming curriculum at Holberton School and focuses on file handling, input/output operations, and data serialization in Python.

The goal of this project is to understand how Python reads from and writes to files, how data can be stored persistently, and how objects can be converted to and from JSON format.

## Learning Objectives
By completing this project, you should be able to:
* Read and write files in Python
* Use the ```with``` statement for file handling
* Understand file encoding and modes
* Serialize and deserialize data using JSON
* Convert Python objects to dictionaries
* Work with command-line scripts that manipulate files
* Handle standard input and output streams

## Files Description

| File                       | Description                                                                 |
| -------------------------- | --------------------------------------------------------------------------- |
| `0-read_file.py`           | Reads and prints the contents of a text file                                |
| `1-write_file.py`          | Writes a string to a text file and returns the number of characters written |
| `2-append_write.py`        | Appends a string to a text file                                             |
| `3-to_json_string.py`      | Converts a Python object to a JSON string                                   |
| `4-from_json_string.py`    | Converts a JSON string to a Python object                                   |
| `5-save_to_json_file.py`   | Saves a Python object to a JSON file                                        |
| `6-load_from_json_file.py` | Loads a Python object from a JSON file                                      |
| `7-add_item.py`            | Script that adds command-line arguments to a JSON file                      |
| `8-class_to_json.py`       | Returns a dictionary description of a simple object                         |
| `9-student.py`             | Defines a `Student` class with JSON serialization                           |
| `10-student.py`            | Enhances `Student` class with selective attribute serialization             |
| `11-student.py`            | Adds reloading capability from JSON to `Student`                            |
| `12-pascal_triangle.py`    | Generates Pascal’s triangle                                                 |
| `100-append_after.py`      | Inserts text after specific lines in a file                                 |
| `101-stats.py`             | Reads stdin and computes log statistics                                     |
| `README.md`                | Project documentation                                                       |

## Requirements
* Python 3.10+
* Ubuntu 22.04 LTS
* Code follows PEP8 / pycodestyle
* All files end with a newline
* First line of each Python file:
```bash
#!/usr/bin/python3
```
* All scripts are executable

## Usage
* Most files can be tested by running them directly:
```bash
./0-read_file.py
```
* Some scripts require command-line arguments:
```bash
./7-add_item.py item1 item2 item3
```
* The ```101-stats.py``` script reads from stdin:
```bash
cat access.log | ./101-stats.py
```

**Concepts Covered**
* File I/O
* JSON serialization
* Object persistence
* Command-line argument handling
* Standard input/output streams
* Data transformation

## Author
**Yara K. Alrasheed**
📧 Email: 11982@holbertonschool.com
🐙 GitHub: 11982-yr
