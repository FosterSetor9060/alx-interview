0x07. Rotate 2D Matrix
Algorithm Specialization
Overview
In the “0x07. Rotate 2D Matrix” project, you’ll implement an in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise. This challenge requires a good understanding of matrix manipulation and in-place operations in Python.

Concepts Needed
Matrix Representation in Python:
Understand how 2D matrices are represented using lists of lists in Python.
Access and modify elements in a 2D matrix.
In-place Operations:
Perform operations on data without creating a copy of the data structure.
Understand the importance of minimizing space complexity by modifying the matrix in place.
Matrix Transposition:
Understand the concept of transposing a matrix (swapping rows and columns).
Implement matrix transposition as a step in the rotation process.
Reversing Rows in a Matrix:
Manipulate rows of a matrix by reversing their order as part of the rotation process.
Nested Loops:
Use nested loops to iterate through 2D data structures like matrices.
Modify elements within nested loops to achieve the desired rotation.
Requirements
General:
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.10)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the project folder, is mandatory
Your code should use the pycodestyle style (version 2.8.0)
You are not allowed to import any module
All modules and functions must be documented
All your files must be executable
Task
0. Rotate 2D Matrix
Given an n x n 2D matrix, rotate it 90 degrees clockwise.
Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
Example Usage
Python

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

rotate_2d_matrix(matrix)
print(matrix)
# Output:
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]
