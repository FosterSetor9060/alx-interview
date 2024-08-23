i0x04. UTF-8 Validation
Algorithm Specialization
Overview
In the “0x04. UTF-8 Validation” project, you’ll apply your knowledge of bitwise operations, understand the UTF-8 encoding scheme, and use Python programming skills to validate whether a given dataset represents a valid UTF-8 encoding.

Concepts Needed
Bitwise Operations in Python:
Understand how to manipulate bits in Python, including operations like AND (&), OR (|), XOR (^), NOT (~), and shifts (<<, >>).
Python Bitwise Operators
UTF-8 Encoding Scheme:
Familiarize yourself with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
Understand the patterns that represent a valid UTF-8 encoded character.
Resources:
UTF-8 Wikipedia
Characters, Symbols, and the Unicode Miracle
The Absolute Minimum Every Software Developer Must Know About Unicode
Data Representation:
Learn how to represent and work with data at the byte level.
Understand how to handle the least significant bits (LSB) of integers to simulate byte data.
List Manipulation in Python:
Iterate through lists, access list elements, and understand list comprehensions.
Python Lists
Boolean Logic:
Apply logical operations to make decisions within your program.
By studying these concepts and utilizing the provided resources, you’ll be well-equipped to tackle the UTF-8 validation project. You’ll effectively apply bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

Requirements
General:
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the project folder is mandatory
Your code should follow the PEP 8 style (version 1.7.x)
All your files must be executable
Task
0. UTF-8 Validation
Write a method that determines if a given data set represents a valid UTF-8 encoding.
Prototype: def validUTF8(data)
Return: True if data is a valid UTF-8 encoding, else return False
A character in UTF-8 can be 1 to 4 bytes long.
The data set can contain multiple characters.
The data will be represented by a list of integers.
Each integer represents 1 byte of data, so you only need to handle the 8 least significant bits of each integer.
Example Usage
Python

data = [65]
print(validUTF8(data))  # Output: True

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))  # Output: True

data = [229, 65, 127, 256]
print(validUTF8(data))  # Output: False
