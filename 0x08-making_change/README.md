0x08. Making Change
Algorithm Specialization
Overview
The “0x08. Making Change” project tackles a classic problem from the domain of dynamic programming and greedy algorithms: the coin change problem. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. This project challenges you to apply your understanding of algorithms to devise a solution that is not only correct but also efficient.

Concepts Needed
Greedy Algorithms:
Understand how greedy algorithms work and why they are suitable for the coin change problem.
Recognize the limitations of greedy algorithms and scenarios where they might not provide the optimal solution.
Dynamic Programming:
Understand basic principles of dynamic programming as a method to solve optimization problems.
Grasp the concept of overlapping subproblems and optimal substructure in the context of the coin change problem.
Algorithmic Complexity:
Analyze the time and space complexity of algorithms.
Strive for solutions with lower complexity to meet runtime constraints.
Problem-Solving Strategies:
Break down the problem into smaller, manageable sub-problems.
Compare iterative vs. recursive approaches to dynamic programming.
Python Programming:
Manipulate lists and use list comprehensions.
Implement functions with efficient looping and conditional statements.
Requirements
General:
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.x)
All your files must be executable
Tasks
0. Change Comes from Within
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of coin in the list
Your solution’s runtime will be evaluated in this task
Example Usage
Python

