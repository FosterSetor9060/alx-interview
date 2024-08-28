0x05. N Queens
Algorithm Specialization
Overview
The N queens puzzle is a classic problem in computer science and mathematics. It challenges you to place N non-attacking queens on an N×N chessboard. In this project, you’ll apply the backtracking algorithm to solve the N queens problem.

Concepts Needed
Backtracking Algorithms:
Understand how backtracking algorithms explore all potential solutions to a problem and backtrack when a solution cannot be completed.
Backtracking Introduction
Recursion:
Use recursive functions to implement backtracking algorithms.
Recursion in Python
List Manipulations in Python:
Create and manipulate lists, especially to store the positions of queens on the board.
Python Lists
Python Command Line Arguments:
Handle command-line arguments using the sys module.
Command Line Arguments in Python
By studying these concepts and utilizing the provided resources, you’ll be equipped with the knowledge required to implement an efficient solution to the N queens problem using Python. This project not only tests your programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.

Requirements
General:
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the project folder is mandatory
Your code should follow the PEP 8 style (version 1.7.*)
All your files must be executable
Task
0. N Queens
The N queens puzzle challenge: Place N non-attacking queens on an N×N chessboard.
Usage: nqueens N
If the user called the program with the wrong number of arguments, print “Usage: nqueens N,” followed by a new line, and exit with status 1.
N must be an integer greater than or equal to 4.
If N is not an integer, print “N must be a number,” followed by a new line, and exit with status 1.
If N is smaller than 4, print “N must be at least 4,” followed by a new line, and exit with status 1.
The program should print every possible solution to the problem, one solution per line.
You don’t have to print the solutions in a specific order.
You are only allowed to import the sys module.
Example Usage
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]

