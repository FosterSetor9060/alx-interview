Lockboxes
Problem Description
You have a set of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1, and each box may contain keys to other boxes. Your task is to determine if all the boxes can be opened.

Rules:
A key with the same number as a box opens that box.
You can assume all keys will be positive integers.
There can be keys that do not have corresponding boxes.
The first box (boxes[0]) is unlocked initially.
Approach
To solve this problem, consider the following concepts:

Lists and List Manipulation:
Understand how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
Python Lists (Python Official Documentation)
Graph Theory Basics (Optional but helpful):
Although not explicitly required, knowledge of graph theory can be useful. Think of the boxes and keys as nodes and edges in a graph.
Concepts related to traversal algorithms like Depth-First Search (DFS) or Breadth-First Search (BFS) can be applied.
Graph Theory (Khan Academy)
Algorithmic Complexity:
Understand the time and space complexity of your solution. This will help you write more efficient algorithms.
Big O Notation (GeeksforGeeks)
Recursion (May be needed):
Some solutions might require a recursive approach to traverse through the boxes and keys.
Recursion in Python (Real Python)
Queue and Stack (For BFS or DFS):
Knowing how to use queues and stacks is crucial if implementing BFS or DFS algorithms.
Python Queue and Stack (GeeksforGeeks)
Set Operations:
Use sets for keeping track of visited boxes and available keys. This can optimize the search process.
Python Sets (Python Official Documentation)
Implementation
Your implementation should include the following:

A Python script (e.g., lockboxes.py) that defines a function canUnlockAll(boxes) which takes a list of lists (boxes) as input.
The function should return True if all boxes can be opened, and False otherwise.
